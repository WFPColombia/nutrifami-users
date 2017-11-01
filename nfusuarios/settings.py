"""
Django settings for nfusuarios project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import platform

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@uh_sy4kzizdba^f&-ai&0&e4u8t*je0f)@iu-!lt(pvj!4v@l'

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
if platform.linux_distribution()[2] == 'Maipo':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "usuarios.nutrifami.org"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'social_django',
    'rest_social_auth',
    'corsheaders',

    'usuarios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'nfusuarios.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'nfusuarios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if platform.linux_distribution()[2] == 'Maipo':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nfusuarios',
            'USER': 'nfusuarios',
            'PASSWORD': 'nfusuarios.pro.2017.web',
            'HOST': 'nutrifami.cwy5i3r1f6xk.us-east-1.rds.amazonaws.com',
            'PORT': '3306',
        }
    }
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            #'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            #'rest_framework.authentication.TokenAuthentication',
            #'rest_framework.authentication.SessionAuthentication',
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nfusuarios',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        )
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'usuarios.CustomUser'

# DRF settings

# social auth settings
# valid redirect domain for all apps: http://restsocialexample.com:8000/
if platform.linux_distribution()[2] == 'Maipo':
    SOCIAL_AUTH_FACEBOOK_KEY = '126883721233688'
    SOCIAL_AUTH_FACEBOOK_SECRET = 'e3c68fe71f6fdb66a52e34cb4e40aaa2'
else:
    SOCIAL_AUTH_FACEBOOK_KEY = '277975186032137'
    SOCIAL_AUTH_FACEBOOK_SECRET = '2c166031eb9032b92d1aa149e5fd1f2c'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': ','.join([
        # public_profile
        'id', 'cover', 'name', 'first_name', 'last_name', 'age_range', 'link',
        'gender', 'locale', 'picture', 'timezone', 'updated_time', 'verified',
        # extra fields
        'email',
    ]),
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '898085701705-07ja94k2e3r3b81oqg2baih6q63ih8i3.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'GwoNQ4ALS0evf1vVZBgRbEJq'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', ]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'usuarios.social_pipeline.auto_logout',  # custom action
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'usuarios.social_pipeline.check_for_email',  # custom action
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'usuarios.social_pipeline.save_avatar',  # custom action
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'rest_social_auth': {
            'handlers': ['console', ],
            'level': "DEBUG",
        },
    }
}


CORS_ORIGIN_ALLOW_ALL = True
