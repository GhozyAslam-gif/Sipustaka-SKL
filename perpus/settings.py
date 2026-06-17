import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-z%f9q0e+e(8p@&cc#(8iqaw!4)64jb_+bc7mk5&jk_er8*#d=!')

# Di Vercel sebaiknya True dulu saat uji coba, jika sudah lancar bisa diubah ke False
DEBUG = False

# Wajib agar domain dari Vercel bisa mengakses Django kamu
ALLOWED_HOSTS = ['GhozyAslam.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perpustkaan',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Tetap pertahankan untuk menghandle CSS/JS di Vercel
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'perpus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'perpus.wsgi.application'



# Cek apakah project sedang berjalan di server PythonAnywhere atau di komputer lokal
if 'PYTHONANYWHERE_SITE' in os.environ:
    # 1. PENGATURAN DATABASE DI SERVER PYTHONANYWHERE
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'perpus_db',       # Sesuaikan dengan nama DB yang dibuat di PythonAnywhere
            'USER': 'GhozyAslam',      # Biasanya menggunakan username PythonAnywhere Anda
            'PASSWORD': '1234',        # Password DB di PythonAnywhere
            'HOST': 'GhozyAslam-postgres.postgres.pythonanywhere-services.com',
            'PORT': '15432',
        }
    }
else:
    # 2. PENGATURAN DATABASE DI LAPTOP/PC LOKAL ANDA
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'perpus_db',       # Nama database postgres di laptop Anda
            'USER': 'postgres',        # Username postgres di laptop Anda
            'PASSWORD': '1234',        # Password postgres di laptop Anda
            'HOST': 'localhost',       # Wajib localhost untuk komputer sendiri
            'PORT': '5432',            # Port default postgres lokal adalah 5432
        }
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Pengaturan lokasi static files khusus untuk Vercel Serverless
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'