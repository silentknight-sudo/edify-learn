import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import os
from typing import List, Dict

class MLModel:
    def __init__(self):
        self.model = None
        self.topics_data = {
            "python": {
                "beginner": [
                    {"title": "Python Basics", "description": "Variables, data types, and basic operations", "estimated_hours": 8},
                    {"title": "Control Flow", "description": "If statements, loops, and basic program flow", "estimated_hours": 10},
                    {"title": "Functions", "description": "Writing and using functions", "estimated_hours": 8}
                ],
                "intermediate": [
                    {"title": "Object-Oriented Programming", "description": "Classes, objects, and inheritance", "estimated_hours": 15},
                    {"title": "File Handling", "description": "Reading and writing files", "estimated_hours": 8},
                    {"title": "Error Handling", "description": "Try-except blocks and debugging", "estimated_hours": 10}
                ],
                "advanced": [
                    {"title": "Decorators & Generators", "description": "Advanced Python features", "estimated_hours": 12},
                    {"title": "Multithreading", "description": "Concurrent programming", "estimated_hours": 15},
                    {"title": "Design Patterns", "description": "Common Python design patterns", "estimated_hours": 20}
                ]
            },
            "machine_learning": {
                "beginner": [
                    {"title": "Math Foundations", "description": "Statistics and linear algebra basics", "estimated_hours": 15},
                    {"title": "Python for Data Science", "description": "NumPy and Pandas", "estimated_hours": 12},
                    {"title": "Data Preprocessing", "description": "Cleaning and preparing data", "estimated_hours": 10}
                ],
                "intermediate": [
                    {"title": "Supervised Learning", "description": "Classification and regression", "estimated_hours": 20},
                    {"title": "Model Evaluation", "description": "Metrics and validation techniques", "estimated_hours": 15},
                    {"title": "Feature Engineering", "description": "Creating and selecting features", "estimated_hours": 12}
                ],
                "advanced": [
                    {"title": "Deep Learning", "description": "Neural networks and deep architectures", "estimated_hours": 25},
                    {"title": "Natural Language Processing", "description": "Text processing and analysis", "estimated_hours": 20},
                    {"title": "MLOps", "description": "Deploying ML models", "estimated_hours": 18}
                ]
            },
            "web_development": {
                "beginner": [
                    {"title": "HTML & CSS", "description": "Web page structure and styling", "estimated_hours": 15},
                    {"title": "JavaScript Basics", "description": "DOM manipulation and events", "estimated_hours": 20},
                    {"title": "Responsive Design", "description": "Mobile-first development", "estimated_hours": 10}
                ],
                "intermediate": [
                    {"title": "Frontend Frameworks", "description": "React or Vue.js basics", "estimated_hours": 25},
                    {"title": "Backend Basics", "description": "Node.js and Express", "estimated_hours": 20},
                    {"title": "Databases", "description": "SQL and MongoDB", "estimated_hours": 15}
                ],
                "advanced": [
                    {"title": "Full Stack Development", "description": "Building complete applications", "estimated_hours": 30},
                    {"title": "Web Security", "description": "Security best practices", "estimated_hours": 20},
                    {"title": "Performance Optimization", "description": "Improving web app performance", "estimated_hours": 15}
                ]
            }
        }
        self.initialize_model()

    def initialize_model(self):
        """Initialize and train the model with sample data"""
        try:
            # Load sample dataset
            dataset_path = os.path.join(os.path.dirname(__file__), 'dataset/dataset.csv')
            if os.path.exists(dataset_path):
                df = pd.read_csv(dataset_path)
            else:
                # Create sample data if dataset doesn't exist
                df = self._create_sample_data()
                # Save the sample dataset
                os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
                df.to_csv(dataset_path, index=False)

            # Train a simple clustering model
            features = df[['activity_score', 'learning_preference']].values
            self.model = KMeans(n_clusters=3, random_state=42)
            self.model.fit(features)

        except Exception as e:
            print(f"Error initializing model: {str(e)}")
            self.model = None

    def _create_sample_data(self):
        """Create sample data for demonstration"""
        np.random.seed(42)
        n_samples = 100
        
        data = {
            'user_id': range(1, n_samples + 1),
            'activity_score': np.random.uniform(0, 100, n_samples),
            'learning_preference': np.random.uniform(0, 100, n_samples)
        }
        
        return pd.DataFrame(data)

    def get_topic_roadmap(self, topic: str) -> Dict:
        """Get the learning roadmap for a specific topic"""
        topic = topic.lower()
        if topic in self.topics_data:
            return {
                "success": True,
                "topic": topic,
                "roadmap": self.topics_data[topic]
            }
        else:
            return {
                "success": False,
                "error": f"Topic '{topic}' not found. Available topics: {', '.join(self.topics_data.keys())}"
            }

    def get_recommendations(self, topic: str = None):
        """Generate personalized learning recommendations"""
        if self.model is None:
            raise Exception("Model not initialized")

        # Sample user data (in production, this would come from user interaction)
        sample_user = np.array([[75, 60]])  # activity_score, learning_preference
        
        # Get the cluster for this user
        cluster = self.model.predict(sample_user)[0]
        
        # If topic is specified, return topic-specific recommendations
        if topic and topic.lower() in self.topics_data:
            levels = ["beginner", "intermediate", "advanced"]
            return self.topics_data[topic.lower()][levels[cluster]]
        
        # Otherwise return general recommendations
        recommendations = {
            0: [  # Beginner cluster
                {
                    "title": "Programming Fundamentals",
                    "description": "Learn basic programming concepts",
                    "difficulty": "Beginner",
                    "estimated_hours": 10
                },
                {
                    "title": "Basic Mathematics",
                    "description": "Essential math for programming",
                    "difficulty": "Beginner",
                    "estimated_hours": 8
                }
            ],
            1: [  # Intermediate cluster
                {
                    "title": "Data Structures",
                    "description": "Common data structures and algorithms",
                    "difficulty": "Intermediate",
                    "estimated_hours": 15
                },
                {
                    "title": "Software Design",
                    "description": "Basic software design principles",
                    "difficulty": "Intermediate",
                    "estimated_hours": 12
                }
            ],
            2: [  # Advanced cluster
                {
                    "title": "System Architecture",
                    "description": "Advanced system design concepts",
                    "difficulty": "Advanced",
                    "estimated_hours": 20
                },
                {
                    "title": "Performance Optimization",
                    "description": "Optimizing code and systems",
                    "difficulty": "Advanced",
                    "estimated_hours": 18
                }
            ]
        }

        return recommendations[cluster]

# Create a global instance
model = MLModel()

def get_recommendations(topic: str = None):
    """Global function to get recommendations"""
    return model.get_recommendations(topic)

def get_topic_roadmap(topic: str):
    """Global function to get topic roadmap"""
    return model.get_topic_roadmap(topic)