from .base import *  # noqa

###################################################################
# General
###################################################################

DEBUG = False

# Production server uchun ALLOWED_HOSTS
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'api.1vs1.uz', 
    '1vs1.uz',
    '185.133.251.101', 
    'adu.1vs1.uz',
    # google 
    '.google.com',
    'www.mamatmusayev.uz',
    'mamatmusayev.uz',
    'adu.mamatmusayev.uz',
    'api.adu.mamatmusayev.uz',
    '5.189.138.155',
]

###################################################################
# Static files (Production)
###################################################################

# Static files collect qilish uchun
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = (BASE_DIR / "staticfiles",)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

###################################################################
# Database (Production)
###################################################################

# Production database settings .env fayldan olinadi
# Lekin qo'shimcha sozlamalar:
DATABASES['default'].update({
    'CONN_MAX_AGE': 60,
})

###################################################################
# Django security
###################################################################

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    'https://api.1vs1.uz', 
    'https://1vs1.uz',
    'https://adu.1vs1.uz',
    # google.com
    'https://*.google.com',
    'https://mamatmusayev.uz',
    'https://adu.mamatmusayev.uz',
    'https://api.adu.mamatmusayev.uz',
    
]

# Security headers
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = False  
CORS_ALLOWED_ORIGINS = [
    'https://1vs1.uz', 
    'https://adu.1vs1.uz',
    'https://adu.mamatmusayev.uz',
    'http://localhost:3000', 
    'http://5.189.138.155:3000', 
]
CORS_ALLOW_CREDENTIALS = True

###################################################################
# Logging
###################################################################
LOG_LEVEL = 'ERROR'
logs_path = BASE_DIR / 'logs'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {pathname}:{lineno} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{logs_path}/django.log',
        },
        # -- telegram bot handler
        'telegrambot_alert': {
            'level': LOG_LEVEL,
            'class': 'apps.logger.handlers.TelegramBotAlertHandler',
            'formatter': 'verbose',
        },
        # Console handler
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        # -- celery log handler
        'celery_log_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
            'filename': f'{logs_path}/celery.log',
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        # -- Error logger
        'error_request_logger': {
            'handlers': ['file', 'console', 'telegrambot_alert'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        # -- Celery logger
        'celery_logger': {
            'handlers': ['celery_log_file', 'console', 'telegrambot_alert'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}


