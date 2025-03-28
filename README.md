# Edify Learn

A modern educational platform with AI-powered learning paths and interactive features.

## Features

- Interactive learning roadmaps with three difficulty levels
- Video recording and playback functionality
- AI-powered personalized recommendations
- Modern neon-themed UI
- Responsive design for all devices

## Tech Stack

- Frontend:
  - HTML5
  - Tailwind CSS
  - JavaScript
  - Font Awesome icons
  - Google Fonts
- Backend:
  - Flask (Python)
  - scikit-learn for ML functionality
- Data:
  - Local CSV dataset
  - Browser's MediaRecorder API for video functionality

## Setup

1. Install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Project Structure

```
edify-learn/
├── index.html           # Landing page
├── roadmap.html         # Learning roadmap page
├── video.html          # Video recording page
├── assets/
│   ├── css/
│   │   └── style.css   # Custom styles
│   └── js/
│       └── main.js     # Frontend functionality
├── backend/
│   ├── app.py          # Flask application
│   └── requirements.txt # Python dependencies
└── ml/
    ├── model.py        # ML model implementation
    └── dataset/
        └── dataset.csv # Sample dataset
```

## Key Features

### Learning Roadmap
- Three difficulty levels: Beginner, Intermediate, and Advanced
- Interactive progress tracking
- Personalized learning paths based on user performance
- Visual timeline representation of learning journey

### Video Lab
- HD video recording capabilities
- Instant download functionality
- Session history tracking
- Camera and microphone integration
- User-friendly controls

### AI Recommendations
- Personalized learning suggestions using KMeans clustering
- Progress-based recommendations
- Adaptive learning paths
- Real-time updates based on user interaction

### Modern UI/UX
- Neon-themed design elements
- Responsive layout for all devices
- Smooth animations and transitions
- Intuitive navigation
- Accessible design patterns

## Browser Compatibility

The application is tested and supported on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Security

- All video recording requires explicit user permission
- Data is processed locally
- No external API dependencies
- Secure Flask configuration

## Future Enhancements

- User authentication system
- Cloud storage for recorded sessions
- Advanced ML models for better recommendations
- Additional learning resources and paths
- Community features and peer learning

## License

MIT License - feel free to use this project for your own learning and development.