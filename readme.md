# Django Blog Project

Simple django blog app that allows users to create edit and delete posts.

## Credits

Inspiration from: [roadmap.sh](https://roadmap.sh/projects/personal-blog)
CSS inspiration and like 80 of the lines from [midnight-discord](https://github.com/refact0r/midnight-discord/blob/master/midnight.css)


## Features

- User registration and authentication
- Create, edit, and delete blog posts
- Admin panel for content management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/sp41414/blogproject.git
   cd blogproject
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Setup the database
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (admin)
   ```bash
   python manage.py createsuperuser
   ```

7. Generate a new secret key
   - Open `settings.py`
   - Replace SECRET_KEY with a new one
   - You can generate a new key using:
     ```python
     from django.core.management.utils import get_random_secret_key
     print(get_random_secret_key())
     ```

## Running the Development Server

```bash
python manage.py runserver
```

The blog will be available at http://127.0.0.1:8000/

## Security Notes

- **IMPORTANT**: The default `SECRET_KEY` in settings.py should be changed before deployment
- Debug mode should be set to `False` in production
- Review the [Django deployment checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/) before deploying

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
6. I probably wont see it
