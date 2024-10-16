# Quiz Master

A Django-based web application for creating and taking quizzes.

## Features

- Create and manage quizzes
- Take quizzes with multiple-choice questions
- Navigate between questions easily
- View quiz results

## Installation

1. Clone the repository:
   ```
   https://github.com/rohitjoshi21/QuizMaster
   cd QuizMaster
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Login using organization account to add and update quizzes.
2. Navigate to `http://localhost:8000/` to view and take quizzes.

## Screenshots

Here are some screenshots of the Quiz Master application:

1. Home Page

   <img src="medias/screenshots/00home.png" alt="Home Page" width="600"/>

2. Signing Up

   <img src="medias/screenshots/01signup.png" alt="Signing Up" width="600"/>

3. Quizzes

   <img src="medias/screenshots/02quizzes.png" alt="Quizzes" width="600"/>

4. Quiz Ongoing

   <img src="medias/screenshots/04livequiz.png" alt="Quiz Ongoing" width="600"/>

5. User Dashboard

   <img src="medias/screenshots/05dashboard.png" alt="User Dashboard" width="600"/>

6. Leaderboard

   <img src="medias/screenshots/06leaderboard.png" alt="Leaderboard" width="600"/>

7. Adding Quiz

   <img src="medias/screenshots/07addquiz.png" alt="Adding Quiz" width="600"/>

## To Do

1. Save the quiz result for each user in database. DONE
2. Add data and visualization in dashboard. DONE
3. Write script to load questions from csv into database. DONE
4. Add css to login and signup pages. DONE
5. Implement leaderboard DONE
6. Create organization page for student monitoring and analysis. Partially Done