FitBuddy 2.0 – AI Fitness Plan Generator

About the Project

FitBuddy 2.0 is an AI-powered fitness plan generator that creates personalized fitness and nutrition suggestions based on user details, fitness goals, experience levels, and dietary preferences.

The application uses Google's Gemini AI to generate fitness guidance and presents the results through a simple web interface.

Features

- Personalized fitness plan generation
- AI-powered recommendations using Gemini
- Fitness goals and experience-level selection
- Dietary preference support
- Simple and user-friendly interface

Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- SQLite
- SQLAlchemy

Project Structure

FitBuddy-2.0/
├── app/
│   ├── __init__.py
│   ├── ai_service.py
│   ├── database.py
│   ├── main.py
│   └── models.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── .gitignore
└── requirements.txt

Installation and Setup

1. Clone the repository

git clone https://github.com/yuvasri-03/FitBuddy-2.0.git
cd FitBuddy-2.0

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment on Windows

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Configure the Gemini API key

Create a ".env" file in the project root and add your own Gemini API key:

GEMINI_API_KEY=your_api_key_here

Never upload your actual API key to GitHub.

6. Run the application

uvicorn app.main:app --reload

Open "http://127.0.0.1:8000" in your browser.

Future Enhancements

- Fitness progress tracking
- Exercise form analysis using computer vision
- More personalized workout recommendations
- Fitness progress analytics

Disclaimer

FitBuddy provides general fitness and nutrition suggestions for informational purposes only. It does not replace advice from qualified healthcare professionals.

Author

Developed as an AI-powered fitness application project.
