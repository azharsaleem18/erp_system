import os
import environ
from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env("DJANGO_SECRET_KEY", default="b+$7gt57sj%w#63ebkrz$n9^0g@+*#yv5-9dr0-(76_d")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
AUTH_USER_MODEL = 'custom_auth.CustomUser'
DOCKERIZED = env.bool("DOCKERIZED", default=False)


# CORS Configuration (Allow frontend domain)
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:3000"])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=True)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',  # ASGI Server for WebRTC
    'channels',  # WebSockets support
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django.contrib.humanize',
    'rest_framework_gis',
    'django.contrib.gis',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'accounting',
    'appraisals',
    'approvals',
    'attendances',
    'custom_auth',
    'dashboards',
    'discuss',
    'documents',
    'employees',
    'expenses',
    'fleet',
    'helpdesk',
    'inventory',
    'payroll',
    'projects',
    'purchase',
    'requisition',
    'sales',
    'timeoff',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Use ASGI for WebRTC instead of WSGI
ASGI_APPLICATION = "core.asgi.application"

#WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("POSTGRES_DB", default="azhar_erp_sys"),
        "USER": env("POSTGRES_USER", default="postgres"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="admin"),
        "HOST": "db" if DOCKERIZED else "localhost",  # Use "db" in Docker, "localhost" locally
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Dubai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Where `collectstatic` collects files
MEDIA_ROOT = os.path.join(BASE_DIR, "media") # Where uploaded files are stored

# Ensure directories exist
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(MEDIA_ROOT, exist_ok=True)

# Allow serving static files when DEBUG=False
if not DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST = env("EMAIL_HOST", default="smtp.office365.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="yourmail@yourdomain.com")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="yourpassword")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="Your Company Name <yourmail@yourdomain.com>")
EMAIL_TIMEOUT = env.int("EMAIL_TIMEOUT", default=10)

# Email Providers (IMAP and SMTP settings)
EMAIL_PROVIDERS = {
    "gmail": {
        "IMAP_SERVER": "imap.gmail.com",
        "SMTP_SERVER": "smtp.gmail.com",
        "IMAP_PORT": 993,
        "SMTP_PORT": 587,
    },
    "outlook": {
        "IMAP_SERVER": "outlook.office365.com",
        "SMTP_SERVER": "smtp.office365.com",
        "IMAP_PORT": 993,
        "SMTP_PORT": 587,
    },
    "yahoo": {
        "IMAP_SERVER": "imap.mail.yahoo.com",
        "SMTP_SERVER": "smtp.mail.yahoo.com",
        "IMAP_PORT": 993,
        "SMTP_PORT": 587,
    }
}


REST_FRAMEWORK = {
    # Default Renderers (Remove BrowsableAPIRenderer in production)
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",  # Remove this in production
    ],

    # Authentication Classes (Use JWT for secure authentication)
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    # Permission Classes (Only registered and verified employees can access)
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    # Pagination (Adjust as per business needs)
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,  # Adjust based on API usage

    # Throttling (To prevent brute force and abuse)
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "user": "100000/day",  # Authenticated users can make 1000 requests/day
        "anon": "50/day",  # Reduce anonymous requests to static pages
    },

    # Exception Handling (Improved custom exception handler)
    "EXCEPTION_HANDLER": "core.utils.custom_exception_handler",

    
    # Content Negotiation (Optional: If supporting multiple content types in future)
    "DEFAULT_CONTENT_NEGOTIATION_CLASS": "rest_framework.negotiation.DefaultContentNegotiation",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "COOKIE_SECURE": env.bool("COOKIE_SECURE", default=False),  # In production use True
    "COOKIE_HTTPONLY": True,
    "COOKIE_SAMESITE": "Lax",
}