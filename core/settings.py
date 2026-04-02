import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Security
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = True  # Change to False in production

ALLOWED_HOSTS = [
    "https://growthappmiddleware.onrender.com",
    "growthappmiddleware.onrender.com",
    "growthappfrontend.onrender.com",
    "localhost",
    "127.0.0.1",
]

# 📦 Installed Apps
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'tasks',
    'progress',
]

# 🔧 Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MUST be first

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 CORS CONFIG (FINAL FIX)
CORS_ALLOWED_ORIGINS = [
    "https://growthappfrontend.onrender.com",
    "https://growthappmiddleware.onrender.com",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

# 🔐 CSRF (IMPORTANT for production)
CSRF_TRUSTED_ORIGINS = [
    "https://growthappfrontend.onrender.com",
    "https://growthappmiddleware.onrender.com",
]

ROOT_URLCONF = 'core.urls'

# 🧩 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# 🗄️ Database (SQLite for now)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Custom User Model
AUTH_USER_MODEL = 'users.User'

# ⚡ Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# 🔥 JWT SETTINGS
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# 🌍 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📁 Static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ⚡ WhiteNoise config (for Render)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 🔒 Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
