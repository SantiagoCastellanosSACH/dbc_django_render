"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy # type: ignore
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'django-insecure-4_r#52!y2^+k3kbp#7o)-(9r@j&twsurkk!_m=k#^2b)cic5g&'
SECRET_KEY = os.environ.get("SECRET_KEY")
# "django-insecure-4_r#52!y2^+k3kbp#7o)-(9r@j&twsurkk!_m=k#^2b)cic5g&"

# SECURITY WARNING: don't run with debug turned on in production!

#DEBUG = True
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS","").split(",")
#ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = os.environ.get("TRUSTED_ORIGINS","").split(",")

# https://dbc-django-render-1.onrender.com


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'whitenoise.runserver_nostatic',#pip install whitenoise
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms', #pip install django-crispy-forms
    "crispy_bootstrap5", #pip install crispy-bootstrap5
    'bootstrap5',
    'contratos',
    'cargos',
    'personas',
    'sstpersonas',
    'sstempresa',


]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5" 


JAZZMIN_SETTINGS = {



    "site_brand": "Administración",

    "site_logo": "img/icono-logo.png",
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#pip install whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main/templates'],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbc_prueba',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1', 
        'PORT': '3306',   
    }
}

#database_url = os.environ.get("DATABASE_URL")
#DATABASES["default"] = dj_database_url.parse(database_url)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT= "/static"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL= 'login'
LOGIN_REDIRECT_URL= reverse_lazy ('principal')

#SESSION_COOKIE_AGE = 600    
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGOUT_REDIRECT_URL = 'admin:index'