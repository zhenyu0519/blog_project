"""
Django settings for blog_project project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm2xjx$nysl^5bqivefirtsuek3x@m=llivf0vz&)77y!7=4n(3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    # add this app in order to use disqus
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add my own app
    'blog_app',
    # add the rich text editor
    'ckeditor',
    # add storage
    'storages',
    # add the disqus comment
    'disqus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'blog_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blogdatabase',
        'USER':'jeffery',
        'PASSWORD':'1234uiop',
        # aws mysql endpoint
        'HOST':'jefferypersonal.nt5fjebdro3.us-east-1.rds.amazonaws.com', #default 127.0.0.1
        'POST':'3306', #default 3306
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# AWS S3 setting
AWS_ACCESS_KEY_ID = 'AKIAJGQINBFXYF4FW65'
AWS_SECRET_ACCESS_KEY = 'XCq82gTr2FancJOpqQfPCXDIaOXcM7TrfV6qsdo'
AWS_STORAGE_BUCKET_NAME = 'jz-blogv2-assets'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
# AWS_LOCATION = 'static'

# This setting defines the additional locations the staticfiles
# app will traverse if the FileSystemFinder finder is enabled,
# e.g. if you use the collectstatic or findstatic management command or use the static file serving view.
STATICFILES_DIRS=[
os.path.join(BASE_DIR, 'static')
]

#static setting for static files
STATIC_URL = 'https://%s/static/' % (AWS_S3_CUSTOM_DOMAIN)
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

# STATIC_URL = '/static/'

# media setting for uploading files
MEDIA_URL = 'https://%s/media/' % (AWS_S3_CUSTOM_DOMAIN)
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'



CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

# Disqus comment system setting
DISQUS_API_KEY = '9aDAxQHmTGKPR9tuT5JobOkpsqWhXQpKofFAGnkZzrJJm1mAQ0bG2lFooka0UJk'
DISQUS_WEBSITE_SHORTNAME = 'zhenyu'