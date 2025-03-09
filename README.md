# PyQuiz

PyQuiz is a web-based quiz application built using Django. The quiz presents users with randomly selected questions, records their scores, and maintains a leaderboard.

## Features
- User authentication (Sign Up, Login, Logout)
- Randomized quiz questions with multiple-choice answers
- Correct/Incorrect answer feedback
- Score tracking for each user
- Leaderboard displaying top performers

## Technologies Used
- Python
- Django
- HTML, CSS, JavaScript
- Bootstrap (for styling)

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python (>= 3.8)
- Django
- PostgreSQL (for production) or SQLite (for local testing)

### Clone the Repository
```sh
git clone https://github.com/olzavadovskyi/PyQuiz.git
cd PyQuiz
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Create a Superuser
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### Run the Development Server
```sh
python manage.py runserver
```
Access the project at `http://127.0.0.1:8000/`.

## Usage
1. Register an account or log in.
2. Click "Start Quiz" to begin answering questions.
3. After answering each question, feedback will be shown (Correct/Wrong).
4. View your score at the end of the quiz.
5. Check the leaderboard to see top scorers.

## Project Structure
```
PyQuiz/
├── expensetracker/         # Django project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI application
│
├── qstable/                # Main quiz app
│   ├── models.py           # Database models (Users, Questions, Choices, Scores)
│   ├── views.py            # Views (Login, Quiz, Leaderboard, etc.)
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Main layout
│   │   ├── index.html      # Homepage
│   │   ├── login.html      # Login page
│   │   ├── signup.html     # Signup page
│   │   ├── quiz.html       # Quiz page
│   │   ├── leaderboard.html # Leaderboard page
│   ├── static/             # CSS, JS, Images
│
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```


## Contact
For any questions or support, reach out via ol.zavadovskyi@gmail.com or open an issue in the repository.

