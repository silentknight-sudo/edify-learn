from flask import Flask, jsonify, request, render_template
import sys
import os
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from ml.learning_path_model import LearningPathGenerator

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize the learning path generator
learning_path_generator = LearningPathGenerator()

@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Get list of all topics"""
    try:
        topics = learning_path_generator.get_all_topics()
        return jsonify({
            'success': True,
            'topics': topics
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/topics/<topic>', methods=['GET'])
def get_topic_roadmap(topic):
    """Get roadmap for a predefined topic"""
    try:
        print(f"Received topic: {topic}")  # Debugging log
        result = learning_path_generator.generate_roadmap(topic)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/', methods=['GET'])
def home():
    """Home route"""
    return render_template('index.html')

@app.route('/roadmap', methods=['GET'])
def roadmap():
    """Serve the roadmap page"""
    return render_template('roadmap.html')

@app.route('/video', methods=['GET'])
def video():
    """Serve the video page"""
    return render_template('video.html')

@app.route('/api/generate-roadmap', methods=['POST'])
def generate_custom_roadmap():
    """Generate roadmap for custom topic"""
    try:
        data = request.get_json()
        if not data or 'topic' not in data:
            return jsonify({
                'success': False,
                'error': 'Topic is required'
            }), 400

        topic = data['topic']
        result = learning_path_generator.generate_roadmap(topic)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.after_request
def after_request(response):
    """Add CORS headers"""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)
