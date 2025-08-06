import django_filters
from apps.structure.models import HomePageText


class HomePageTextFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        choices=[
            ('main', 'Asosiy Sahifasi'),
            ('global', 'Global'),
            ('academic', 'Akademic'),
            ('history', 'Tarix')
        ],
        help_text='Filter by type of HomePageText'
    )

    class Meta:
        model = HomePageText
        fields = ['type']
