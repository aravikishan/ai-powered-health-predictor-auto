# AI-Powered Health Predictor Auto

## Overview
The AI-Powered Health Predictor Auto is an innovative application designed to provide users with personalized health insights and recommendations. By leveraging artificial intelligence, this project aims to analyze user health data and offer actionable advice to promote healthier lifestyles. This tool is particularly beneficial for individuals looking to understand their health risks and receive tailored health tips without needing a professional consultation. The application serves as a bridge between users and valuable health information, making it accessible and easy to understand.

The project addresses the growing need for accessible health information by utilizing a user-friendly interface where individuals can input their health data, such as age, weight, height, medical history, and lifestyle factors. The application then predicts potential health risks and offers recommendations to mitigate these risks. Additionally, users can access general health tips to enhance their well-being.

## Features
- **User Health Data Input**: Allows users to input personal health information including age, weight, height, medical history, and lifestyle factors.
- **Health Risk Prediction**: Utilizes AI to predict health risk levels based on user input, categorizing risk as 'Low' or 'High'.
- **Personalized Recommendations**: Provides tailored recommendations such as exercise and diet tips to improve health outcomes.
- **Health Tips Database**: Offers a collection of general health tips stored in a SQLite database, accessible via the application.
- **Responsive Design**: Features a responsive web interface that adapts to various screen sizes, ensuring accessibility on different devices.
- **Static and Dynamic Content**: Combines static HTML templates with dynamic content rendering using FastAPI and Jinja2.
- **API Endpoints**: Exposes several API endpoints for health data prediction and retrieval of health tips.

## Tech Stack
| Component         | Technology  |
|-------------------|-------------|
| Backend Framework | FastAPI     |
| Server            | Uvicorn     |
| Templating Engine | Jinja2      |
| Database          | SQLite      |
| Frontend          | HTML, CSS   |
| Scripting         | JavaScript  |

## Architecture
The project architecture is structured to efficiently serve both static and dynamic content. The backend, built with FastAPI, handles API requests and serves HTML templates using Jinja2. The SQLite database stores user health data and health tips, which are accessed via API endpoints. The data flow begins with user input, processed by the backend to generate predictions and recommendations, which are then displayed on the frontend.

```plaintext
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|   User Input     +----->+   FastAPI API    +----->+   SQLite DB      |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
        |                        |                        |
        v                        v                        v
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  HTML Templates  |<-----+   Jinja2 Templ.  |<-----+  Health Tips     |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-health-predictor-auto.git
   cd ai-powered-health-predictor-auto
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
2. Visit the application in your browser at `http://localhost:8000`

## API Endpoints
| Method | Path                    | Description                                     |
|--------|-------------------------|-------------------------------------------------|
| GET    | `/`                     | Home page with project overview.                |
| GET    | `/predict`              | Page for inputting health data for prediction.  |
| POST   | `/api/predict`          | API endpoint for predicting health risks.       |
| GET    | `/recommendations`      | Page displaying general health recommendations. |
| GET    | `/api/recommendations`  | API endpoint for retrieving recommendations.    |
| GET    | `/about`                | About page with project information.            |
| GET    | `/contact`              | Contact page with a form to reach out.          |
| GET    | `/api/health-tips`      | API endpoint for retrieving health tips.        |

## Project Structure
```plaintext
.
├── Dockerfile                  # Infrastructure file for Docker setup
├── app.py                      # Main application file with FastAPI routes
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the application
├── static
│   ├── css
│   │   └── style.css           # Main stylesheet for the application
│   └── js
│       └── main.js             # JavaScript for client-side interactions
└── templates
    ├── about.html              # Template for the About page
    ├── contact.html            # Template for the Contact page
    ├── index.html              # Template for the Home page
    ├── predict.html            # Template for the Prediction page
    └── recommendations.html    # Template for the Recommendations page
```

## Screenshots
*Screenshots of the application interface will be added here.*

## Docker Deployment
To deploy the application using Docker, follow these steps:
1. Build the Docker image:
   ```bash
   docker build -t ai-powered-health-predictor .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 ai-powered-health-predictor
   ```

## Contributing
We welcome contributions to enhance the AI-Powered Health Predictor Auto. Please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with clear and descriptive messages.
- Push your changes to your fork.
- Submit a pull request detailing your changes.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.