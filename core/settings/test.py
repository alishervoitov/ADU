from .base import *  # Base settings'dan import qiling

# Test uchun SQLite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # RAM'da test database
    }
}

# Test tezligini oshirish uchun
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Logging'ni o'chirish
LOGGING_CONFIG = None

# Cache'ni o'chirish
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Static files
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Debug rejimi
DEBUG = False

# Test rejimi
TESTING = True