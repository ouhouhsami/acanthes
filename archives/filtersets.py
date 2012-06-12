import datetime
import django_filters
from archives.models import *


YEAR_CHOICES = [(x,x) for x in range(1977,datetime.datetime.now().year+1)]
YEAR_CHOICES = [('', '---------')]+ YEAR_CHOICES

class AudioFilterSet(django_filters.FilterSet):
    annee = django_filters.ChoiceFilter(label="Year", choices= YEAR_CHOICES, required=False)
    kf_id_lieu = django_filters.ModelChoiceFilter(label="Place", queryset=Lieu.objects.all())
    kf_id_intervenant_principal = django_filters.ModelChoiceFilter(label="Keynote speaker", queryset=Intervenant.objects.all())
    kf_id_orchestre = django_filters.ModelChoiceFilter(label="Orchestra", queryset=Orchestre.objects.all())
    intervenants = django_filters.ModelMultipleChoiceFilter(label="Participants", queryset=Intervenant.objects.all())
    class Meta:
        model = Audio
        fields = ['annee', 'kf_id_lieu', 'kf_id_intervenant_principal', 'kf_id_orchestre', 'kf_id_lieu', 'intervenants']