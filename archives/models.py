# coding=utf-8

from django.db import models

class Intervenant(models.Model):
    biographie = models.TextField(blank=True)
    horodatage_creation = models.TextField(blank=True)
    horodatage_modification = models.TextField(blank=True)
    #kp_id_intervenant = models.CharField(max_length=255, db_column='kp_ID_intervenant', blank=True, primary_key=True) # Field name made lowercase.
    #kp_id_intervenant = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255, db_column='Nom', blank=True) # Field name made lowercase.
    prenom = models.CharField(max_length=255, db_column=u'Prénom', blank=True) # Field name made lowercase.
    prenom_nom = models.CharField(max_length=255, blank=True)
    web_1 = models.CharField(max_length=255, blank=True)
    web_2 = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.prenom, self.nom)

    class Meta:
        db_table = u'intervenant'

class Langue(models.Model):
    #kp_id_langue = models.CharField(max_length=255, db_column='kp_ID_langue', blank=True, primary_key=True) # Field name made lowercase.
    #kp_id_langue = models.IntegerField(primary_key=True)
    languageterm = models.CharField(max_length=255, db_column='languageTerm', blank=True) # Field name made lowercase.

    def __unicode__(self):
        return u'%s' % (self.languageterm)

    class Meta:
        db_table = u'langue'

class Lieu(models.Model):
    #kp_id_lieu = models.CharField(max_length=255, db_column='kp_ID_lieu', blank=True, primary_key=True) # Field name made lowercase.
    #kp_id_lieu = models.IntegerField(primary_key=True)
    placeterm = models.CharField(max_length="255", db_column='placeTerm', blank=True) # Field name made lowercase.
    salle = models.CharField(max_length="255", blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.placeterm, self.salle)

    class Meta:
        db_table = u'lieu'

class Orchestre(models.Model):
    #kp_id_formation = models.CharField(max_length=255, db_column='kp_ID_formation', blank=True, primary_key=True) # Field name made lowercase.
    #kp_id_formation = models.IntegerField(primary_key=True)
    musiciens = models.TextField(blank=True)
    nom_complet = models.CharField(max_length="255", db_column='nom complet', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    nom_chef = models.CharField(max_length="255", blank=True)
    prenom_chef = models.CharField(max_length="255", blank=True)
    role_chef = models.CharField(max_length="255", blank=True)
    sous_titre = models.TextField(db_column='sous titre', blank=True) # Field renamed to remove spaces. Field name made lowercase.

    def __unicode__(self):
        return u'%s' % (self.nom_complet)

    class Meta:
        db_table = u'orchestre'

class Audio(models.Model):
    #id_archive_audio = models.CharField(max_length=255, db_column='ID_archive_audio', blank=True, primary_key=True) # Field name made lowercase.
    #id_archive_audio = models.IntegerField(primary_key=True)
    annee = models.CharField("Year", max_length=255, blank=True)
    date_enregistrement = models.TextField(blank=True)
    subtitle = models.TextField(db_column='subTitle', blank=True) # Field name made lowercase.
    duree = models.TextField(blank=True)
    total_durees = models.TextField(blank=True)
    remarque = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    url_export_ircam = models.TextField(db_column='url_export IRCAM', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    type_ircam = models.TextField(blank=True)
    acanthes = models.TextField(blank=True)
    type_document = models.CharField(max_length=255, blank=True)
    #kf_id_langue_1 = models.TextField(db_column='kf_ID_langue_1', blank=True) # Field name made lowercase.
    #kf_id_langue_2 = models.TextField(db_column='kf_ID_langue_2', blank=True) # Field name made lowercase.
    #kf_id_langue_3 = models.TextField(db_column='kf_ID_langue_3', blank=True) # Field name made lowercase.
    kf_id_langue_1 = models.ForeignKey(Langue, db_column='kf_ID_langue_1', blank=True, related_name='langue_1', null=True) # Field name made lowercase.
    kf_id_langue_2 = models.ForeignKey(Langue, db_column='kf_ID_langue_2', blank=True, related_name='langue_2', null=True) # Field name made lowercase.
    kf_id_langue_3 = models.ForeignKey(Langue, db_column='kf_ID_langue_3', blank=True, related_name='langue_3', null=True) # Field name made lowercase.
    #kf_id_intervenant_principal = models.TextField(db_column='kf_ID_intervenant_principal', blank=True) # Field name made lowercase.
    kf_id_intervenant_principal = models.ForeignKey(Intervenant, db_column='kf_ID_intervenant_principal', null=True, blank=True) # Field name made lowercase.
    #kf_id_lieu = models.TextField(db_column='kf_ID_lieu', blank=True) # Field name made lowercase.
    kf_id_lieu = models.ForeignKey(Lieu, db_column='kf_ID_lieu', null=True, blank=True) # Field name made lowercase.
    typeofresource = models.CharField(max_length=255, db_column='typeOfResource', null=True, blank=True) # Field name made lowercase.
    genre = models.CharField(max_length=255, blank=True)
    physicaldescription = models.CharField(max_length=255, db_column='physicalDescription', blank=True) # Field name made lowercase.
    #kf_id_orchestre = models.TextField(db_column='kf_ID_orchestre', blank=True) # Field name made lowercase.
    kf_id_orchestre = models.ForeignKey(Orchestre, db_column='kf_ID_orchestre', null=True, blank=True) # Field name made lowercase.
    url_ecoute_intranet_adresse = models.FileField(blank=True, upload_to="ACDA/audio_mp3/")
    details_intranet_actuel_acda = models.TextField(db_column='details_intranet_actuel_ACDA', blank=True) # Field name made lowercase.
    url_ecoute_intranet = models.TextField(blank=True)
    url_ecoute_internet = models.TextField(blank=True)
    url_ecoute_extranet = models.TextField(blank=True)
    horodatage_creation = models.TextField(blank=True)
    horodatage_modification = models.TextField(blank=True)
    dateissued_portail = models.TextField(db_column='dateIssued_portail', blank=True) # Field name made lowercase.
    lien_test_web = models.TextField(blank=True)
    chemin_fichier = models.TextField(blank=True)
    # oai
    oai_web_oai_mods = models.TextField(db_column='oai_WEB_OAI_MODS', blank=True) # Field name made lowercase.
    oai_id = models.TextField(blank=True)
    oai_titleinfo_title = models.TextField(db_column='oai_titleInfo_title', blank=True) # Field name made lowercase.
    oai_typeofresource = models.TextField(db_column='oai_typeOfResource', blank=True) # Field name made lowercase.
    oai_genre = models.TextField(blank=True)
    oai_origininfo_place = models.TextField(db_column='oai_originInfo_place', blank=True) # Field name made lowercase.
    oai_origininfo_publisher = models.TextField(db_column='oai_originInfo_publisher', blank=True) # Field name made lowercase.
    oai_origininfo_datecaptured = models.TextField(db_column='oai_originInfo_dateCaptured', blank=True) # Field name made lowercase.
    oai_language_languageterm_1 = models.TextField(db_column='oai_language_languageTerm_1', blank=True) # Field name made lowercase.
    oai_language_languageterm_2 = models.TextField(db_column='oai_language_languageTerm_2', blank=True) # Field name made lowercase.
    oai_language_languageterm_3 = models.TextField(db_column='oai_language_languageTerm_3', blank=True) # Field name made lowercase.
    oai_physicaldescription_form = models.TextField(db_column='oai_physicalDescription_form', blank=True) # Field name made lowercase.
    oai_physicaldescription_internetmediatype = models.TextField(db_column='oai_physicalDescription_internetMediaType', blank=True) # Field name made lowercase.
    oai_physicaldescription_digitalorigin = models.TextField(db_column='oai_physicalDescription_digitalOrigin', blank=True) # Field name made lowercase.
    oai_abstract = models.TextField(blank=True)
    oai_targetaudience = models.TextField(db_column='oai_targetAudience', blank=True) # Field name made lowercase.
    oai_location_url_preview = models.TextField(blank=True)
    oai_location_url_full = models.TextField(blank=True)
    oai_location_physicallocation = models.TextField(db_column='oai_location_physicalLocation', blank=True) # Field name made lowercase.
    oai_accesscondition = models.TextField(db_column='oai_accessCondition', blank=True) # Field name made lowercase.
    oai_recordinfo_recordcontentsource = models.TextField(db_column='oai_recordInfo_recordContentSource', blank=True) # Field name made lowercase.
    oai_recordinfo_recordcreationdate = models.TextField(db_column='oai_recordInfo_recordCreationDate', blank=True) # Field name made lowercase.
    oai_recordinfo_recordchangedate = models.TextField(db_column='oai_recordInfo_recordChangeDate', blank=True) # Field name made lowercase.
    oai_recordinfo_recordidentifier = models.TextField(db_column='oai_recordInfo_recordIdentifier', blank=True) # Field name made lowercase.
    oai_recordinfo_languageofcataloging_languageterm = models.TextField(db_column='oai_recordInfo_languageOfCataloging_languageTerm', blank=True) # Field name made lowercase.
    oai_publication = models.TextField(blank=True)
    # fin OAI
    # debut joli code
    intervenants = models.ManyToManyField(Intervenant, through='IntervenantAudio', related_name="intervenants_audio")

    def __unicode__(self):
        return u'%s %s' % (self.id, self.annee)

    class Meta:
        db_table = u'audio'

class IntervenantAudio(models.Model):
    intervenant = models.ForeignKey(Intervenant)
    audio = models.ForeignKey(Audio)
    role = models.CharField(max_length=255, blank=True, null=True)
    ordre = models.IntegerField(blank=True, null=True)

'''
when files
class Files(models.Model):
    title = models.CharField(max_length=255)
    file_type =  partition ...
    file ... filefield
'''