import os, django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-zaoa2a(+2o9&i+f#k*e^n*+kfln-m0_j#oes@2ob4ua8#(4fi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: strict it, when complete development. Dima.
ALLOWED_HOSTS = ['*']


# Application definition
# CORS_ORIGIN_ALLOW_ALL=True

INSTALLED_APPS = [
    'modeltranslation',
    'rest_framework',
    'ckeditor',
    'corsheaders',
    # 'uzbplaces',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'live_support',


    # 'simple_mail',
    'news.apps.NewsConfig',
    'tenders.apps.TendersConfig',
    'interactive.apps.InteractiveConfig',
    # 'docs_files.apps.DocsFilesConfig',
    'ungfiles.apps.UngfilesConfig',
    'pagenavbar.apps.PagenavbarConfig',
    'djangoapp',
    'django_filters',

]


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 9,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL=True

ROOT_URLCONF = 'djangoapp.urls'

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

WSGI_APPLICATION = 'djangoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NewUng',
#         'USER': 'postgres',
#         'PASSWORD': 'V1ctor=>me',
#         'HOST': '127.0.0.1', 
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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



# MAIL_HOST = 'stmp.gmail.com'
# EMAIL_PORT = '587'
# # EMAIL_HOST_USER = ''
# EMAIL_HOST_USER = 'cmuzaffarmirzo@gmail.com'
# # EMAIL_HOST_PASSWORD = ''
# EMAIL_HOST_PASSWORD = 'V1ctor=>me'
# EMAIL_USE_TLS = True
# # EMAIL_USE_SSL = False
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# # MAILER_EMAIL_BACKEND = EMAIL_BACKEND



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

gettext = lambda s: s

LANGUAGE_CODE = 'ru'

EXTRA_LANG_INFO = {
    'uz': {
        'bidi': False,
        'code': 'uz',
        'name': 'Uzbek',
        'name_local': 'Uzbek',
    },
}
LANGUAGES = (
    ('uz', gettext('Uzbek')),
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
    # ('uz', gettext('Uzbek')),
)

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'en')

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL =    '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
    'toolbar': 'None',

    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # os.path.join(BASE_DIR, "media"),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
MAIL_HOST = 'stmp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'cmuzaffarmirzo@gmail.com'
EMAIL_HOST_PASSWORD = 'V1ctor=>me'
EMAIL_USE_TLS = True

# EMAIL_USE_SSL = False





# LOGGING = {
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#         },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }