"""
Django settings for buchiDjango3 project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#アップロード系のモデルフィールド用に。
LOCAL_FILE_DIR = BASE_DIR + '\_upload_files'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1a5bf340-7da8-4717-b4bf-7862261755ab'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them

    'buchi_wk.apps.buchi_wkConfig',

    'polls.apps.pollsConfig',
    # アプリケーションをプロジェクトに含めるには、構成クラスへの参照を 
    # INSTALLED_APPS 設定に追加する必要があります。 
    # pollsConfig クラスは、 polls/apps.py にあるので、
    # ドットつなぎのパスは 'polls.apps.PollsConfig' となります。

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buchiDjango3.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/

# Django がどのようにテンプレートをロードしレンダリングするかが書かれています。
# デフォルトの設定ファイルでは、 DjangoTemplates バックエンドが設定されており、
# その APP_DIRS のオプションが True になっています。規約により、DjangoTemplates は
# INSTALLED_APPS のそれぞれの "templates" サブディレクトリを検索します。

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 管理画面用に トップに作ったフォルダを追記。

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

WSGI_APPLICATION = 'buchiDjango3.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
    #ENGINE -- 
    #　'django.db.backends.sqlite3'
    #　'django.db.backends.postgresql'
    #　'django.db.backends.mysql' 
    #　'django.db.backends.oracle' 
    #　のいずれか。その他のバックエンド も利用可能です。

    #NAME -- データベースの名前です。
    #　SQLite を使用している場合、データベースはコンピュータ上のファイルになります。
    #　その場合、NAME には、そのファイルのファイル名を含んだ絶対パスを指定する必要があります。
    #　デフォルト値は os.path.join(BASE_DIR, 'db.sqlite3') で、プロジェクトのディレクトリに保存されます。
    #　SQLite を使っていない場合、 USER や PASSWORD そして HOST などの 追加設定を加える必要があります。



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'        #'en-us'

TIME_ZONE = 'Asia/Tokyo'    #'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

