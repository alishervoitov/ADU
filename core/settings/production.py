from .base import *  # noqa

###################################################################
# General
###################################################################

DEBUG = False

# Production server uchun ALLOWED_HOSTS
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "api.1vs1.uz", 
    "185.133.251.101", 
]

###################################################################
# Static files (Production)
###################################################################

# Static files collect qilish uchun
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/adu/static/'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/adu/media/'

###################################################################
# Database (Production)
###################################################################

# Production database settings .env fayldan olinadi
# Lekin qo'shimcha sozlamalar:
DATABASES['default'].update({
    'CONN_MAX_AGE': 60,
    'OPTIONS': {
        'MAX_CONNS': 20,
        'charset': 'utf8mb4',
    }
})

###################################################################
# Django security
###################################################################

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "https://api.1vs1.uz", 
]

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = False  
CORS_ALLOWED_ORIGINS = [
    "https://1vs1.uz", 
    "http://localhost:3000", 
]
CORS_ALLOW_CREDENTIALS = True

###################################################################
# Logging
###################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/www/adu/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


