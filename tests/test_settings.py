from pathlib import Path

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS += [
    'formset',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
