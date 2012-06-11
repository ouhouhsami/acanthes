# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Langue'
        db.create_table(u'langue', (
            ('kp_id_langue', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='kp_ID_langue')),
            ('languageterm', self.gf('django.db.models.fields.TextField')(db_column='languageTerm', blank=True)),
        ))
        db.send_create_signal('archives', ['Langue'])

        # Adding model 'Orchestre'
        db.create_table(u'orchestre', (
            ('kp_id_formation', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='kp_ID_formation')),
            ('musiciens', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('nom_complet', self.gf('django.db.models.fields.TextField')(db_column='nom complet', blank=True)),
            ('nom_chef', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('prenom_chef', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('role_chef', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sous_titre', self.gf('django.db.models.fields.TextField')(db_column='sous titre', blank=True)),
        ))
        db.send_create_signal('archives', ['Orchestre'])

        # Adding model 'Lieu'
        db.create_table(u'lieu', (
            ('kp_id_lieu', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='kp_ID_lieu')),
            ('placeterm', self.gf('django.db.models.fields.TextField')(db_column='placeTerm', blank=True)),
            ('salle', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archives', ['Lieu'])

        # Adding model 'Intervenant'
        db.create_table(u'intervenant', (
            ('biographie', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('horodatage_creation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('horodatage_modification', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('kp_id_intervenant', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='kp_ID_intervenant')),
            ('nom', self.gf('django.db.models.fields.TextField')(db_column='Nom', blank=True)),
            ('prenom', self.gf('django.db.models.fields.TextField')(db_column=u'Pr\xe9nom', blank=True)),
            ('prenom_nom', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('web_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('web_2', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archives', ['Intervenant'])


        # Changing field 'Audio.remarque'
        db.alter_column(u'audio', 'remarque', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.url_ecoute_intranet_adresse'
        db.alter_column(u'audio', 'url_ecoute_intranet_adresse', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.subtitle'
        db.alter_column(u'audio', 'subTitle', self.gf('django.db.models.fields.TextField')(db_column='subTitle'))

        # Changing field 'Audio.lien_test_web'
        db.alter_column(u'audio', 'lien_test_web', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.total_durees'
        db.alter_column(u'audio', 'total_durees', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_physicaldescription_form'
        db.alter_column(u'audio', 'oai_physicalDescription_form', self.gf('django.db.models.fields.TextField')(db_column='oai_physicalDescription_form'))

        # Changing field 'Audio.kf_id_orchestre'
        db.alter_column(u'audio', 'kf_ID_orchestre', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_orchestre'))

        # Changing field 'Audio.oai_origininfo_publisher'
        db.alter_column(u'audio', 'oai_originInfo_publisher', self.gf('django.db.models.fields.TextField')(db_column='oai_originInfo_publisher'))

        # Changing field 'Audio.oai_targetaudience'
        db.alter_column(u'audio', 'oai_targetAudience', self.gf('django.db.models.fields.TextField')(db_column='oai_targetAudience'))

        # Changing field 'Audio.abstract'
        db.alter_column(u'audio', 'abstract', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_origininfo_place'
        db.alter_column(u'audio', 'oai_originInfo_place', self.gf('django.db.models.fields.TextField')(db_column='oai_originInfo_place'))

        # Changing field 'Audio.horodatage_creation'
        db.alter_column(u'audio', 'horodatage_creation', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_location_physicallocation'
        db.alter_column(u'audio', 'oai_location_physicalLocation', self.gf('django.db.models.fields.TextField')(db_column='oai_location_physicalLocation'))

        # Changing field 'Audio.physicaldescription'
        db.alter_column(u'audio', 'physicalDescription', self.gf('django.db.models.fields.TextField')(db_column='physicalDescription'))

        # Changing field 'Audio.type_ircam'
        db.alter_column(u'audio', 'type_ircam', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.duree'
        db.alter_column(u'audio', 'duree', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_publication'
        db.alter_column(u'audio', 'oai_publication', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.dateissued_portail'
        db.alter_column(u'audio', 'dateIssued_portail', self.gf('django.db.models.fields.TextField')(db_column='dateIssued_portail'))

        # Changing field 'Audio.oai_titleinfo_title'
        db.alter_column(u'audio', 'oai_titleInfo_title', self.gf('django.db.models.fields.TextField')(db_column='oai_titleInfo_title'))

        # Changing field 'Audio.acanthes'
        db.alter_column(u'audio', 'acanthes', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.typeofresource'
        db.alter_column(u'audio', 'typeOfResource', self.gf('django.db.models.fields.TextField')(db_column='typeOfResource'))

        # Changing field 'Audio.oai_id'
        db.alter_column(u'audio', 'oai_id', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.url_ecoute_extranet'
        db.alter_column(u'audio', 'url_ecoute_extranet', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_recordinfo_languageofcataloging_languageterm'
        db.alter_column(u'audio', 'oai_recordInfo_languageOfCataloging_languageTerm', self.gf('django.db.models.fields.TextField')(db_column='oai_recordInfo_languageOfCataloging_languageTerm'))

        # Changing field 'Audio.kf_id_langue_1'
        db.alter_column(u'audio', 'kf_ID_langue_1', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_1'))

        # Changing field 'Audio.oai_abstract'
        db.alter_column(u'audio', 'oai_abstract', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.kf_id_langue_3'
        db.alter_column(u'audio', 'kf_ID_langue_3', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_3'))

        # Changing field 'Audio.kf_id_langue_2'
        db.alter_column(u'audio', 'kf_ID_langue_2', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_2'))

        # Changing field 'Audio.oai_typeofresource'
        db.alter_column(u'audio', 'oai_typeOfResource', self.gf('django.db.models.fields.TextField')(db_column='oai_typeOfResource'))

        # Changing field 'Audio.url_ecoute_internet'
        db.alter_column(u'audio', 'url_ecoute_internet', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.url_ecoute_intranet'
        db.alter_column(u'audio', 'url_ecoute_intranet', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_location_url_full'
        db.alter_column(u'audio', 'oai_location_url_full', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.date_enregistrement'
        db.alter_column(u'audio', 'date_enregistrement', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_physicaldescription_digitalorigin'
        db.alter_column(u'audio', 'oai_physicalDescription_digitalOrigin', self.gf('django.db.models.fields.TextField')(db_column='oai_physicalDescription_digitalOrigin'))

        # Changing field 'Audio.oai_origininfo_datecaptured'
        db.alter_column(u'audio', 'oai_originInfo_dateCaptured', self.gf('django.db.models.fields.TextField')(db_column='oai_originInfo_dateCaptured'))

        # Changing field 'Audio.oai_recordinfo_recordcreationdate'
        db.alter_column(u'audio', 'oai_recordInfo_recordCreationDate', self.gf('django.db.models.fields.TextField')(db_column='oai_recordInfo_recordCreationDate'))

        # Changing field 'Audio.oai_recordinfo_recordchangedate'
        db.alter_column(u'audio', 'oai_recordInfo_recordChangeDate', self.gf('django.db.models.fields.TextField')(db_column='oai_recordInfo_recordChangeDate'))

        # Changing field 'Audio.horodatage_modification'
        db.alter_column(u'audio', 'horodatage_modification', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_recordinfo_recordcontentsource'
        db.alter_column(u'audio', 'oai_recordInfo_recordContentSource', self.gf('django.db.models.fields.TextField')(db_column='oai_recordInfo_recordContentSource'))

        # Changing field 'Audio.genre'
        db.alter_column(u'audio', 'genre', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.details_intranet_actuel_acda'
        db.alter_column(u'audio', 'details_intranet_actuel_ACDA', self.gf('django.db.models.fields.TextField')(db_column='details_intranet_actuel_ACDA'))

        # Changing field 'Audio.annee'
        db.alter_column(u'audio', 'annee', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_language_languageterm_3'
        db.alter_column(u'audio', 'oai_language_languageTerm_3', self.gf('django.db.models.fields.TextField')(db_column='oai_language_languageTerm_3'))

        # Changing field 'Audio.oai_language_languageterm_2'
        db.alter_column(u'audio', 'oai_language_languageTerm_2', self.gf('django.db.models.fields.TextField')(db_column='oai_language_languageTerm_2'))

        # Changing field 'Audio.oai_language_languageterm_1'
        db.alter_column(u'audio', 'oai_language_languageTerm_1', self.gf('django.db.models.fields.TextField')(db_column='oai_language_languageTerm_1'))

        # Changing field 'Audio.type_document'
        db.alter_column(u'audio', 'type_document', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.url_export_ircam'
        db.alter_column(u'audio', 'url_export IRCAM', self.gf('django.db.models.fields.TextField')(db_column='url_export IRCAM'))

        # Changing field 'Audio.oai_web_oai_mods'
        db.alter_column(u'audio', 'oai_WEB_OAI_MODS', self.gf('django.db.models.fields.TextField')(db_column='oai_WEB_OAI_MODS'))

        # Changing field 'Audio.kf_id_intervenant_principal'
        db.alter_column(u'audio', 'kf_ID_intervenant_principal', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_intervenant_principal'))

        # Changing field 'Audio.kf_id_lieu'
        db.alter_column(u'audio', 'kf_ID_lieu', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_lieu'))

        # Changing field 'Audio.oai_physicaldescription_internetmediatype'
        db.alter_column(u'audio', 'oai_physicalDescription_internetMediaType', self.gf('django.db.models.fields.TextField')(db_column='oai_physicalDescription_internetMediaType'))

        # Changing field 'Audio.chemin_fichier'
        db.alter_column(u'audio', 'chemin_fichier', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_accesscondition'
        db.alter_column(u'audio', 'oai_accessCondition', self.gf('django.db.models.fields.TextField')(db_column='oai_accessCondition'))

        # Changing field 'Audio.oai_recordinfo_recordidentifier'
        db.alter_column(u'audio', 'oai_recordInfo_recordIdentifier', self.gf('django.db.models.fields.TextField')(db_column='oai_recordInfo_recordIdentifier'))

        # Changing field 'Audio.oai_location_url_preview'
        db.alter_column(u'audio', 'oai_location_url_preview', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Audio.oai_genre'
        db.alter_column(u'audio', 'oai_genre', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'Langue'
        db.delete_table(u'langue')

        # Deleting model 'Orchestre'
        db.delete_table(u'orchestre')

        # Deleting model 'Lieu'
        db.delete_table(u'lieu')

        # Deleting model 'Intervenant'
        db.delete_table(u'intervenant')


        # Changing field 'Audio.remarque'
        db.alter_column(u'audio', 'remarque', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.url_ecoute_intranet_adresse'
        db.alter_column(u'audio', 'url_ecoute_intranet_adresse', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.subtitle'
        db.alter_column(u'audio', 'subTitle', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='subTitle'))

        # Changing field 'Audio.lien_test_web'
        db.alter_column(u'audio', 'lien_test_web', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.total_durees'
        db.alter_column(u'audio', 'total_durees', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_physicaldescription_form'
        db.alter_column(u'audio', 'oai_physicalDescription_form', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_form'))

        # Changing field 'Audio.kf_id_orchestre'
        db.alter_column(u'audio', 'kf_ID_orchestre', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_orchestre'))

        # Changing field 'Audio.oai_origininfo_publisher'
        db.alter_column(u'audio', 'oai_originInfo_publisher', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_publisher'))

        # Changing field 'Audio.oai_targetaudience'
        db.alter_column(u'audio', 'oai_targetAudience', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_targetAudience'))

        # Changing field 'Audio.abstract'
        db.alter_column(u'audio', 'abstract', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_origininfo_place'
        db.alter_column(u'audio', 'oai_originInfo_place', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_place'))

        # Changing field 'Audio.horodatage_creation'
        db.alter_column(u'audio', 'horodatage_creation', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_location_physicallocation'
        db.alter_column(u'audio', 'oai_location_physicalLocation', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_location_physicalLocation'))

        # Changing field 'Audio.physicaldescription'
        db.alter_column(u'audio', 'physicalDescription', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='physicalDescription'))

        # Changing field 'Audio.type_ircam'
        db.alter_column(u'audio', 'type_ircam', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.duree'
        db.alter_column(u'audio', 'duree', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_publication'
        db.alter_column(u'audio', 'oai_publication', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.dateissued_portail'
        db.alter_column(u'audio', 'dateIssued_portail', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='dateIssued_portail'))

        # Changing field 'Audio.oai_titleinfo_title'
        db.alter_column(u'audio', 'oai_titleInfo_title', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_titleInfo_title'))

        # Changing field 'Audio.acanthes'
        db.alter_column(u'audio', 'acanthes', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.typeofresource'
        db.alter_column(u'audio', 'typeOfResource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='typeOfResource'))

        # Changing field 'Audio.oai_id'
        db.alter_column(u'audio', 'oai_id', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.url_ecoute_extranet'
        db.alter_column(u'audio', 'url_ecoute_extranet', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_recordinfo_languageofcataloging_languageterm'
        db.alter_column(u'audio', 'oai_recordInfo_languageOfCataloging_languageTerm', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_languageOfCataloging_languageTerm'))

        # Changing field 'Audio.kf_id_langue_1'
        db.alter_column(u'audio', 'kf_ID_langue_1', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_1'))

        # Changing field 'Audio.oai_abstract'
        db.alter_column(u'audio', 'oai_abstract', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.kf_id_langue_3'
        db.alter_column(u'audio', 'kf_ID_langue_3', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_3'))

        # Changing field 'Audio.kf_id_langue_2'
        db.alter_column(u'audio', 'kf_ID_langue_2', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_2'))

        # Changing field 'Audio.oai_typeofresource'
        db.alter_column(u'audio', 'oai_typeOfResource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_typeOfResource'))

        # Changing field 'Audio.url_ecoute_internet'
        db.alter_column(u'audio', 'url_ecoute_internet', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.url_ecoute_intranet'
        db.alter_column(u'audio', 'url_ecoute_intranet', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_location_url_full'
        db.alter_column(u'audio', 'oai_location_url_full', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.date_enregistrement'
        db.alter_column(u'audio', 'date_enregistrement', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_physicaldescription_digitalorigin'
        db.alter_column(u'audio', 'oai_physicalDescription_digitalOrigin', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_digitalOrigin'))

        # Changing field 'Audio.oai_origininfo_datecaptured'
        db.alter_column(u'audio', 'oai_originInfo_dateCaptured', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_dateCaptured'))

        # Changing field 'Audio.oai_recordinfo_recordcreationdate'
        db.alter_column(u'audio', 'oai_recordInfo_recordCreationDate', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordCreationDate'))

        # Changing field 'Audio.oai_recordinfo_recordchangedate'
        db.alter_column(u'audio', 'oai_recordInfo_recordChangeDate', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordChangeDate'))

        # Changing field 'Audio.horodatage_modification'
        db.alter_column(u'audio', 'horodatage_modification', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_recordinfo_recordcontentsource'
        db.alter_column(u'audio', 'oai_recordInfo_recordContentSource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordContentSource'))

        # Changing field 'Audio.genre'
        db.alter_column(u'audio', 'genre', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.details_intranet_actuel_acda'
        db.alter_column(u'audio', 'details_intranet_actuel_ACDA', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='details_intranet_actuel_ACDA'))

        # Changing field 'Audio.annee'
        db.alter_column(u'audio', 'annee', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_language_languageterm_3'
        db.alter_column(u'audio', 'oai_language_languageTerm_3', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_3'))

        # Changing field 'Audio.oai_language_languageterm_2'
        db.alter_column(u'audio', 'oai_language_languageTerm_2', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_2'))

        # Changing field 'Audio.oai_language_languageterm_1'
        db.alter_column(u'audio', 'oai_language_languageTerm_1', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_1'))

        # Changing field 'Audio.type_document'
        db.alter_column(u'audio', 'type_document', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.url_export_ircam'
        db.alter_column(u'audio', 'url_export IRCAM', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='url_export IRCAM'))

        # Changing field 'Audio.oai_web_oai_mods'
        db.alter_column(u'audio', 'oai_WEB_OAI_MODS', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_WEB_OAI_MODS'))

        # Changing field 'Audio.kf_id_intervenant_principal'
        db.alter_column(u'audio', 'kf_ID_intervenant_principal', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_intervenant_principal'))

        # Changing field 'Audio.kf_id_lieu'
        db.alter_column(u'audio', 'kf_ID_lieu', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_lieu'))

        # Changing field 'Audio.oai_physicaldescription_internetmediatype'
        db.alter_column(u'audio', 'oai_physicalDescription_internetMediaType', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_internetMediaType'))

        # Changing field 'Audio.chemin_fichier'
        db.alter_column(u'audio', 'chemin_fichier', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_accesscondition'
        db.alter_column(u'audio', 'oai_accessCondition', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_accessCondition'))

        # Changing field 'Audio.oai_recordinfo_recordidentifier'
        db.alter_column(u'audio', 'oai_recordInfo_recordIdentifier', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordIdentifier'))

        # Changing field 'Audio.oai_location_url_preview'
        db.alter_column(u'audio', 'oai_location_url_preview', self.gf('django.db.models.fields.CharField')(max_length=15000))

        # Changing field 'Audio.oai_genre'
        db.alter_column(u'audio', 'oai_genre', self.gf('django.db.models.fields.CharField')(max_length=15000))

    models = {
        'archives.audio': {
            'Meta': {'object_name': 'Audio', 'db_table': "u'audio'"},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'acanthes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'annee': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'chemin_fichier': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_enregistrement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dateissued_portail': ('django.db.models.fields.TextField', [], {'db_column': "'dateIssued_portail'", 'blank': 'True'}),
            'details_intranet_actuel_acda': ('django.db.models.fields.TextField', [], {'db_column': "'details_intranet_actuel_ACDA'", 'blank': 'True'}),
            'duree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'horodatage_creation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'horodatage_modification': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id_archive_audio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'ID_archive_audio'"}),
            'kf_id_intervenant_principal': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_intervenant_principal'", 'blank': 'True'}),
            'kf_id_langue_1': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_langue_1'", 'blank': 'True'}),
            'kf_id_langue_2': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_langue_2'", 'blank': 'True'}),
            'kf_id_langue_3': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_langue_3'", 'blank': 'True'}),
            'kf_id_lieu': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_lieu'", 'blank': 'True'}),
            'kf_id_orchestre': ('django.db.models.fields.TextField', [], {'db_column': "'kf_ID_orchestre'", 'blank': 'True'}),
            'lien_test_web': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_accesscondition': ('django.db.models.fields.TextField', [], {'db_column': "'oai_accessCondition'", 'blank': 'True'}),
            'oai_genre': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_language_languageterm_1': ('django.db.models.fields.TextField', [], {'db_column': "'oai_language_languageTerm_1'", 'blank': 'True'}),
            'oai_language_languageterm_2': ('django.db.models.fields.TextField', [], {'db_column': "'oai_language_languageTerm_2'", 'blank': 'True'}),
            'oai_language_languageterm_3': ('django.db.models.fields.TextField', [], {'db_column': "'oai_language_languageTerm_3'", 'blank': 'True'}),
            'oai_location_physicallocation': ('django.db.models.fields.TextField', [], {'db_column': "'oai_location_physicalLocation'", 'blank': 'True'}),
            'oai_location_url_full': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_location_url_preview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_origininfo_datecaptured': ('django.db.models.fields.TextField', [], {'db_column': "'oai_originInfo_dateCaptured'", 'blank': 'True'}),
            'oai_origininfo_place': ('django.db.models.fields.TextField', [], {'db_column': "'oai_originInfo_place'", 'blank': 'True'}),
            'oai_origininfo_publisher': ('django.db.models.fields.TextField', [], {'db_column': "'oai_originInfo_publisher'", 'blank': 'True'}),
            'oai_physicaldescription_digitalorigin': ('django.db.models.fields.TextField', [], {'db_column': "'oai_physicalDescription_digitalOrigin'", 'blank': 'True'}),
            'oai_physicaldescription_form': ('django.db.models.fields.TextField', [], {'db_column': "'oai_physicalDescription_form'", 'blank': 'True'}),
            'oai_physicaldescription_internetmediatype': ('django.db.models.fields.TextField', [], {'db_column': "'oai_physicalDescription_internetMediaType'", 'blank': 'True'}),
            'oai_publication': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oai_recordinfo_languageofcataloging_languageterm': ('django.db.models.fields.TextField', [], {'db_column': "'oai_recordInfo_languageOfCataloging_languageTerm'", 'blank': 'True'}),
            'oai_recordinfo_recordchangedate': ('django.db.models.fields.TextField', [], {'db_column': "'oai_recordInfo_recordChangeDate'", 'blank': 'True'}),
            'oai_recordinfo_recordcontentsource': ('django.db.models.fields.TextField', [], {'db_column': "'oai_recordInfo_recordContentSource'", 'blank': 'True'}),
            'oai_recordinfo_recordcreationdate': ('django.db.models.fields.TextField', [], {'db_column': "'oai_recordInfo_recordCreationDate'", 'blank': 'True'}),
            'oai_recordinfo_recordidentifier': ('django.db.models.fields.TextField', [], {'db_column': "'oai_recordInfo_recordIdentifier'", 'blank': 'True'}),
            'oai_targetaudience': ('django.db.models.fields.TextField', [], {'db_column': "'oai_targetAudience'", 'blank': 'True'}),
            'oai_titleinfo_title': ('django.db.models.fields.TextField', [], {'db_column': "'oai_titleInfo_title'", 'blank': 'True'}),
            'oai_typeofresource': ('django.db.models.fields.TextField', [], {'db_column': "'oai_typeOfResource'", 'blank': 'True'}),
            'oai_web_oai_mods': ('django.db.models.fields.TextField', [], {'db_column': "'oai_WEB_OAI_MODS'", 'blank': 'True'}),
            'physicaldescription': ('django.db.models.fields.TextField', [], {'db_column': "'physicalDescription'", 'blank': 'True'}),
            'remarque': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'db_column': "'subTitle'", 'blank': 'True'}),
            'total_durees': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type_document': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type_ircam': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'typeofresource': ('django.db.models.fields.TextField', [], {'db_column': "'typeOfResource'", 'blank': 'True'}),
            'url_ecoute_extranet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url_ecoute_internet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url_ecoute_intranet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url_ecoute_intranet_adresse': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url_export_ircam': ('django.db.models.fields.TextField', [], {'db_column': "'url_export IRCAM'", 'blank': 'True'})
        },
        'archives.intervenant': {
            'Meta': {'object_name': 'Intervenant', 'db_table': "u'intervenant'"},
            'biographie': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'horodatage_creation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'horodatage_modification': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'kp_id_intervenant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'kp_ID_intervenant'"}),
            'nom': ('django.db.models.fields.TextField', [], {'db_column': "'Nom'", 'blank': 'True'}),
            'prenom': ('django.db.models.fields.TextField', [], {'db_column': "u'Pr\\xe9nom'", 'blank': 'True'}),
            'prenom_nom': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'web_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'web_2': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'archives.langue': {
            'Meta': {'object_name': 'Langue', 'db_table': "u'langue'"},
            'kp_id_langue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'kp_ID_langue'"}),
            'languageterm': ('django.db.models.fields.TextField', [], {'db_column': "'languageTerm'", 'blank': 'True'})
        },
        'archives.lieu': {
            'Meta': {'object_name': 'Lieu', 'db_table': "u'lieu'"},
            'kp_id_lieu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'kp_ID_lieu'"}),
            'placeterm': ('django.db.models.fields.TextField', [], {'db_column': "'placeTerm'", 'blank': 'True'}),
            'salle': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'archives.orchestre': {
            'Meta': {'object_name': 'Orchestre', 'db_table': "u'orchestre'"},
            'kp_id_formation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'kp_ID_formation'"}),
            'musiciens': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nom_chef': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nom_complet': ('django.db.models.fields.TextField', [], {'db_column': "'nom complet'", 'blank': 'True'}),
            'prenom_chef': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'role_chef': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sous_titre': ('django.db.models.fields.TextField', [], {'db_column': "'sous titre'", 'blank': 'True'})
        }
    }

    complete_apps = ['archives']