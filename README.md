# Quiz App

A Django-based web application for creating and taking quizzes.

## Features

- Create and manage quizzes
- Take quizzes with multiple-choice questions
- Navigate between questions easily
- View quiz results

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
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

1. Access the admin panel at `http://localhost:8000/admin/` to create quizzes and questions.
2. Navigate to `http://localhost:8000/` to view and take quizzes.

## Project Structure

- `quiz/` - Main Django app directory
  - `models.py` - Database models for Quiz and Question
  - `views.py` - View functions for rendering quizzes and processing answers
  - `urls.py` - URL configurations for the quiz app
- `templates/` - HTML templates
  - `studentbase.html` - Base template for student views
  - `quiz_view.html` - Template for displaying quiz questions
- `static/` - Static files (CSS, JavaScript, images)
  - `dashboard/quiz_view.css` - Styles for the quiz view

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Django documentation
- Contributors and maintainers of dependencies used in this project
