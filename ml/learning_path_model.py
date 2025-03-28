import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

class LearningPathGenerator:
    def __init__(self):
        # Get the absolute path to the dataset
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dataset_paths = [
            os.path.join(current_dir, 'dataset', 'Learning_Pathway_Index.csv'),
            os.path.join(current_dir, 'dataset', 'Additional_Topics.csv'),
        ]  # Closing bracket added here

        # Load and preprocess the datasets
        dataframes = []
        for path in dataset_paths:
            df = pd.read_csv(path)
            dataframes.append(df)
        self.df = pd.concat(dataframes, ignore_index=True)

        # Load and preprocess the dataset
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
        # Combine relevant columns for better topic matching
        self.df['combined_text'] = self.df['Topic'].fillna('') + ' ' + \
                                    self.df['Description'].fillna('') + ' ' + \
                                    self.df['Keywords'].fillna('')
        
        # Create TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['combined_text'])

    def generate_roadmap(self, topic):
        # Convert topic to vector
        topic_vector = self.vectorizer.transform([topic])
        
        # Calculate similarity scores
        similarity_scores = cosine_similarity(topic_vector, self.tfidf_matrix)
        
        # Check if any relevant entries were found
        if similarity_scores[0].max() == 0:
            return {
                'success': False,
                'error': 'No relevant topics found for the given input.'
            }
        
        top_indices = similarity_scores[0].argsort()[-10:][::-1]
        relevant_entries = self.df.iloc[top_indices]
        
        # Organize content by difficulty level
        roadmap = {
            'beginner': [],
            'intermediate': [],
            'advanced': []
        }
        
        # Helper function to determine difficulty level
        def get_difficulty(row):
            keywords = str(row['Keywords']).lower()
            description = str(row['Description']).lower()
            
            if any(word in keywords + description for word in ['basic', 'fundamental', 'introduction', 'beginner']):
                return 'beginner'
            elif any(word in keywords + description for word in ['advanced', 'expert', 'complex']):
                return 'advanced'
            else:
                return 'intermediate'

        # Organize content into difficulty levels
        for _, entry in relevant_entries.iterrows():
            difficulty = get_difficulty(entry)
            
            roadmap_item = {
                'title': entry['Topic'],
                'description': entry['Description'] if pd.notna(entry['Description']) else 'Learn about ' + entry['Topic'],
                'estimated_hours': np.random.randint(4, 21),  # Random estimate between 4-20 hours
                'keywords': entry['Keywords'] if pd.notna(entry['Keywords']) else '',
                'resources': entry['Resources'] if pd.notna(entry['Resources']) else ''
            }
            
            roadmap[difficulty].append(roadmap_item)

        return {
            'success': True,
            'roadmap': roadmap
        }

    def get_all_topics(self):
        # Return list of all topics from both datasets
        common_topics = [
            'python',
            'machine_learning',
            'web_development',
            'data_science',
            'artificial_intelligence',
            'cloud_computing',
            'cybersecurity',
            'mobile_development',
            'devops',
            'blockchain'
        ]
        additional_topics = self.df['Topic'].unique().tolist()
        return common_topics + additional_topics
        return common_topics
