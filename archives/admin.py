from django.contrib import admin
from archives.models import *

class IntervenantAudioInline(admin.TabularInline):
    model = IntervenantAudio
    extra = 1

class AudioAdmin(admin.ModelAdmin):
    inlines = (IntervenantAudioInline,)
    list_display = ('id', 'annee', 'genre', 'url_ecoute_intranet_adresse' )
    list_filter = ('annee', )
    exclude = ('duree', 'total_durees', 'chemin_fichier', 'lien_test_web', 'dateissued_portail', 'horodatage_modification', 
    'url_export_ircam', 'type_ircam', 'date_enregistrement', 'acanthes', 
    'horodatage_creation', 'url_ecoute_extranet', 'url_ecoute_internet', 'url_ecoute_intranet', 'details_intranet_actuel_acda',
    'oai_web_oai_mods', 'oai_id', 'oai_titleinfo_title', 'oai_typeofresource', 'oai_genre', 'oai_origininfo_place', 
    'oai_origininfo_publisher', 'oai_origininfo_datecaptured', 'oai_language_languageterm_1', 'oai_language_languageterm_2', 
    'oai_language_languageterm_3', 'oai_physicaldescription_form', 'oai_physicaldescription_internetmediatype', 'oai_physicaldescription_digitalorigin',
    'oai_abstract', 'oai_targetaudience', 'oai_location_url_preview', 'oai_location_url_full', 'oai_location_physicallocation', 'oai_accesscondition', 
    'oai_recordinfo_recordcontentsource', 'oai_recordinfo_recordcreationdate', 'oai_recordinfo_recordchangedate', 'oai_recordinfo_recordidentifier', 
    'oai_recordinfo_languageofcataloging_languageterm', 'oai_publication')

class IntervenantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom')
    exclude = ('horodatage_creation', 'horodatage_modification')

class LangueAdmin(admin.ModelAdmin):
    list_display = ('languageterm',)

class LieuAdmin(admin.ModelAdmin):
    list_display = ('placeterm', 'salle')

class OrchestreAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'sous_titre')






admin.site.register(Audio, AudioAdmin)
admin.site.register(Intervenant, IntervenantAdmin)
admin.site.register(Langue, LangueAdmin)
admin.site.register(Lieu, LieuAdmin)
admin.site.register(Orchestre, OrchestreAdmin)