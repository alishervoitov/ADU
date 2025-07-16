from django.utils.translation import get_language as django_get_language
from django.utils.translation import get_language_from_request

def get_language(request=None):
    if request:
        current_language = get_language_from_request(request)
    else:
        current_language = django_get_language()

    return current_language