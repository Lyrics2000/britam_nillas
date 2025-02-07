
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$clti#^#lf^&uo7rgf2u@_xaq24vryr179bnyumgo42m9&2%v7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "corsheaders",
    'home',
    'logs'
   

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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'
DEV_ENV =  True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# BASE_URL = "http://brapi_nilassuat.britamgroup.com:17172/BRITAMBASIC/ODataV4/OnlinePortal_"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

CORS_ALLOW_CREDENTIALS = True
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static_file/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_file'),
]

STATIC_ROOT = os.path.join('static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media_cdn')

# api_nilas_BASE_URL  = "http://brapi_nilassuat.britamgroup.com:17172/BRITAMBASIC/ODataV4/OnlinePortal_"
# USERNAME = "erp"
# PASSWORD  = "Pass@7046."

INDEV = True

if INDEV:
    BASE_URL  = "http://10.10.3.197:9099"
    USERNAME = "sladmin"
    PASSWORD  = "sladmin123"
else:
    BASE_URL = "http://172.26.0.35:8143/BRITAMBASIC/ODataV4/OnlinePortal_"
    USERNAME = "portal"
    PASSWORD  = "S92^$&@1z7yfocd3/SjUZt"


# Roles for API views
API_NILAS_CREATE_MEMBER = "API_NILAS_CREATE_MEMBER"
API_NILAS_CREATE_NOMINEE = "API_NILAS_CREATE_NOMINEE"
API_NILAS_CREATE_FINANCIAL_INFO = "API_NILAS_CREATE_FINANCIAL_INFO"
API_NILAS_CREATE_MEMBER_LIFESTYLE = "API_NILAS_CREATE_MEMBER_LIFESTYLE"
API_NILAS_PRODUCT_SEARCH = "API_NILAS_PRODUCT_SEARCH"
API_NILAS_CREATE_QUOTE = "API_NILAS_CREATE_QUOTE"
API_NILAS_SAVE_APPLICATION = "API_NILAS_SAVE_APPLICATION"
API_NILAS_PAYOUT_DETAILS = "API_NILAS_PAYOUT_DETAILS"
API_NILAS_CREATE_PAYMENT_DETAILS = "API_NILAS_CREATE_PAYMENT_DETAILS"
API_NILAS_GET_ALL_PLAN = "API_NILAS_GET_ALL_PLAN"
API_NILAS_GET_ALL_PRODUCT_BY_PLAN_NO = "API_NILAS_GET_ALL_PRODUCT_BY_PLAN_NO"
API_NILAS_GET_FREQUENCY = "API_NILAS_GET_FREQUENCY"
API_NILAS_GET_DURATIONS = "API_NILAS_GET_DURATIONS"
API_NILAS_CUSTOMER_SEARCH = "API_NILAS_CUSTOMER_SEARCH"
API_NILAS_GET_PREMIUM_LIMITS = "API_NILAS_GET_PREMIUM_LIMITS"
API_NILAS_CREATE_PAYOUT_MODE = "API_NILAS_CREATE_PAYOUT_MODE"
API_NILAS_IDENTIFICATION_DETAILS = "API_NILAS_IDENTIFICATION_DETAILS"
API_NILAS_DOCUMENTS_UPLOAD = "API_NILAS_DOCUMENTS_UPLOAD"
API_NILAS_PAYER_DETAILS = "API_NILAS_PAYER_DETAILS"
API_NILAS_INITIAL_PAYMENT_DETAILS = "API_NILAS_INITIAL_PAYMENT_DETAILS"
API_NILAS_PAYMENT_DETAILS = "API_NILAS_PAYMENT_DETAILS"
API_NILAS_GENERATE_APPLICATION_ID = "API_NILAS_GENERATE_APPLICATION_ID"
API_NILAS_INSURED_DETAILS = "API_NILAS_INSURED_DETAILS"
API_NILAS_UPDATE_FINANCIAL_INFO = "API_NILAS_UPDATE_FINANCIAL_INFO"
API_NILAS_SUBMIT_MEDICALS = "API_NILAS_SUBMIT_MEDICALS"
API_NILAS_SUBMIT_ADDITIONAL_MEDICALS = "API_NILAS_SUBMIT_ADDITIONAL_MEDICALS"
API_NILAS_BENEFICIARY_DETAILS = "API_NILAS_BENEFICIARY_DETAILS"




API_NILAS_NOMINEE_DETAILS = "API_NILAS_NOMINEE_DETAILS"
API_NILAS_FINAL_SUBMISSION_CASE_APPLICATION = "API_NILAS_FINAL_SUBMISSION_CASE_APPLICATION"
API_NILAS_SUBSEQUENT_PAYMENT = "API_NILAS_SUBSEQUENT_PAYMENT"
API_NILAS_AS_CODE_RELATIONSHIPS = "API_NILAS_AS_CODE_RELATIONSHIPS"
API_NILAS_AS_CODE_BRITAM_OCCUPATION = "API_NILAS_AS_CODE_BRITAM_OCCUPATION"
API_NILAS_AS_CODE_CLIENT_PREFIX = "API_NILAS_AS_CODE_CLIENT_PREFIX"
API_NILAS_AS_CODE_MARITAL_STATUS = "API_NILAS_AS_CODE_MARITAL_STATUS"
API_NILAS_GET_CLIENTS = "API_NILAS_GET_CLIENTS"
API_NILAS_GET_CASE = "API_NILAS_GET_CASE"
API_NILAS_FILTER_BY_AGENT_ID = "API_NILAS_FILTER_BY_AGENT_ID"



API_NILAS_PROCESS_PARTIAL = "API_NILAS_PROCESS_PARTIAL"
API_NILAS_GET_PARTIAL = "API_NILAS_GET_PARTIAL"
API_NILAS_UPDATE_PAYOUT = "API_NILAS_UPDATE_PAYOUT"
API_NILAS_GET_MONTHLY_STATEMENTS = "API_NILAS_GET_MONTHLY_STATEMENTS"
API_NILAS_GET_TAX_CERTIFICATE = "API_NILAS_GET_TAX_CERTIFICATE"
API_NILAS_PREMIUM_RENEWAL = "API_NILAS_PREMIUM_RENEWAL"
API_NILAS_GET_BANK_ACCOUNTS = "API_NILAS_GET_BANK_ACCOUNTS"
API_NILAS_GET_BENEFICIARIES = "API_NILAS_GET_BENEFICIARIES"
API_NILAS_GET_BANK_ACCOUNT_POLICIES = "API_NILAS_GET_BANK_ACCOUNT_POLICIES"
API_NILAS_GET_POLICY_DETAILS = "API_NILAS_GET_POLICY_DETAILS"
API_NILAS_GET_BENEFITS = "API_NILAS_GET_BENEFITS"











# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
