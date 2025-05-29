from pathlib import Path
import os
from datetime import timedelta
import environ
 


#env=environ.Env(DEBUG=(bool, False))
env = environ.Env(
    DEBUG=(bool, False),
    EMAIL_PORT=(int, 2525),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR/".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'contas.User'

APPS = [
    'comunidade',
    'processo',
    'postagem',
    'contas',
    'consulta',
    'blog',
    'suporte',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'behave_django',
    #'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
    'drf_yasg',
    "djoser",
    'django_extensions',
    'django_filters',

    
] + APPS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'PAGE_SIZE': 5,
}



CORS_ALLOW_ALL_ORIGINS = True  
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",  
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
] 
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s %(bold_white)s|%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(bold_white)s|%(reset)s %(cyan)s%(name)s%(reset)s %(bold_white)s|%(reset)s %(message)s',
            'log_colors': {
                'DEBUG': 'purple',
                'INFO': 'blue',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            'secondary_log_colors': {},
            'style': '%'
        },
        'simple': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(levelname)s %(message)s%(reset)s',
            'log_colors': {
                'DEBUG': 'purple',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'INFO',
    },
}
WSGI_APPLICATION = 'backend.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'projuridico',          # substitua aqui
         'USER': 'postgres',       # substitua aqui
         'PASSWORD': 'postgres',     # substitua aqui
         'HOST': 'localhost',          # ex: your-stack.tembo.io
         'PORT': '5433',                   # normalmente 5432
     }
 }


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
    "SIGNING_KEY": env("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}


DJOSER = {
    'LOGIN_FIELD':'email',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_RETYPE':True,
    'USERNAME_RESET_CONFIRM_URL':'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL':'activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL':True,
    'SERIALIZERS': {
        'user_create': 'contas.api.serializer.CreateUserSerializer',
        'user': 'contas.api.serializer.UserReturnSerializer', 
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'current_user': 'contas.api.serializer.UserReturnSerializer',
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
DOMAIN = env("DOMAIN")
SITE_NAME = "ProJuridico"