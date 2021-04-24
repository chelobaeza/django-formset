from pathlib import Path

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
