import os
from django.conf import settings
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
SECRET_KEY = '1342aykut'


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
DEBUG = 'True'


ALLOWED_HOSTS = [
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'feed.apps.FeedConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'stdimage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'places',
    'django_google_maps',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyPage.urls'

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

WSGI_APPLICATION = 'MyPage.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'postgres',
      'USER':'postgres',
      'PASSWORD':'918273645cantas',
      'HOST':'localhost',
      'PORT':'5432',
   }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


CLOUDINARY_STORAGE = {
'CLOUD_NAME':'dbfmaljuh',
'API_KEY': '376978896398661',
'API_SECRET':'KrzQ85sllTsD3653LefJX_Y-yxk'
}

PLACES_MAPS_API_KEY='AIzaSyDlmWzOETT386SR5lq2ADFMvsejrrycmoE'
PLACES_MAP_WIDGET_HEIGHT=300
PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'


#GOOGLE_MAPS_API_KEY = 'AIzaSyAquU4Qndrd6E2Twym-us1L18oFT39w39A'


CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'


CKEDITOR_CONFIGS = {
'portal_config': {
    # 'skin': 'moono',
    # 'skin': 'office2013',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_YourCustomToolbarConfig': [
        {'name': 'document', 'items': [
            'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'
        ]},
        {'name': 'clipboard', 'items': [
            'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'
        ]},
        {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
        {'name': 'forms',
         'items': [
             'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
             'Select', 'Button', 'ImageButton', 'HiddenField'
         ]},
        '/',
        {'name': 'basicstyles',
         'items': [
             'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
             'Superscript', '-', 'RemoveFormat'
         ]},
        {'name': 'paragraph',
         'items': [
             'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
             '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft',
             'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
             'BidiLtr', 'BidiRtl', 'Language'
         ]},
        {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        {'name': 'insert',
         'items': [
             'Image', 'Table', 'HorizontalRule',
             'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'
         ]},
        '/',
        {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
        {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        {'name': 'about', 'items': ['About']},
        '/',  # put this to force next toolbar on new line
        {'name': 'yourcustomtools', 'items': [
            # put the name of your editor.ui.addButton here
            'Preview',
            'Maximize',

        ]},
    ],
    'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
    # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
    # 'height': 291,
    # 'width': '100%',
    # 'filebrowserWindowHeight': 725,
    # 'filebrowserWindowWidth': 940,
    # 'toolbarCanCollapse': True,
    # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
    'tabSpaces': 4,
    'extraPlugins': ','.join([
        'uploadimage',  # the upload image feature
        # your extra plugins here
        'div',
        'autolink',
        'autoembed',
        'embedsemantic',
        'autogrow',
        # 'devtools',
        'widget',
        'lineutils',
        'clipboard',
        'dialog',
        'dialogui',
        'elementspath'
    ]),
    }
}