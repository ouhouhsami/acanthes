# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Audio'
        db.create_table(u'audio', (
            ('id_archive_audio', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True, db_column='ID_archive_audio')),
            ('annee', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('date_enregistrement', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='subTitle', blank=True)),
            ('duree', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('total_durees', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('remarque', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('url_export_ircam', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='url_export IRCAM', blank=True)),
            ('type_ircam', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('acanthes', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('type_document', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('kf_id_langue_1', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_1', blank=True)),
            ('kf_id_langue_2', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_2', blank=True)),
            ('kf_id_langue_3', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_langue_3', blank=True)),
            ('kf_id_intervenant_principal', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_intervenant_principal', blank=True)),
            ('kf_id_lieu', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_lieu', blank=True)),
            ('typeofresource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='typeOfResource', blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('physicaldescription', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='physicalDescription', blank=True)),
            ('kf_id_orchestre', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='kf_ID_orchestre', blank=True)),
            ('url_ecoute_intranet_adresse', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('details_intranet_actuel_acda', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='details_intranet_actuel_ACDA', blank=True)),
            ('url_ecoute_intranet', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('url_ecoute_internet', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('url_ecoute_extranet', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('horodatage_creation', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('horodatage_modification', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('dateissued_portail', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='dateIssued_portail', blank=True)),
            ('lien_test_web', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('chemin_fichier', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_web_oai_mods', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_WEB_OAI_MODS', blank=True)),
            ('oai_id', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_titleinfo_title', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_titleInfo_title', blank=True)),
            ('oai_typeofresource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_typeOfResource', blank=True)),
            ('oai_genre', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_origininfo_place', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_place', blank=True)),
            ('oai_origininfo_publisher', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_publisher', blank=True)),
            ('oai_origininfo_datecaptured', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_originInfo_dateCaptured', blank=True)),
            ('oai_language_languageterm_1', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_1', blank=True)),
            ('oai_language_languageterm_2', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_2', blank=True)),
            ('oai_language_languageterm_3', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_language_languageTerm_3', blank=True)),
            ('oai_physicaldescription_form', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_form', blank=True)),
            ('oai_physicaldescription_internetmediatype', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_internetMediaType', blank=True)),
            ('oai_physicaldescription_digitalorigin', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_physicalDescription_digitalOrigin', blank=True)),
            ('oai_abstract', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_targetaudience', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_targetAudience', blank=True)),
            ('oai_location_url_preview', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_location_url_full', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
            ('oai_location_physicallocation', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_location_physicalLocation', blank=True)),
            ('oai_accesscondition', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_accessCondition', blank=True)),
            ('oai_recordinfo_recordcontentsource', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordContentSource', blank=True)),
            ('oai_recordinfo_recordcreationdate', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordCreationDate', blank=True)),
            ('oai_recordinfo_recordchangedate', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordChangeDate', blank=True)),
            ('oai_recordinfo_recordidentifier', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_recordIdentifier', blank=True)),
            ('oai_recordinfo_languageofcataloging_languageterm', self.gf('django.db.models.fields.CharField')(max_length=15000, db_column='oai_recordInfo_languageOfCataloging_languageTerm', blank=True)),
            ('oai_publication', self.gf('django.db.models.fields.CharField')(max_length=15000, blank=True)),
        ))
        db.send_create_signal('archives', ['Audio'])


    def backwards(self, orm):
        # Deleting model 'Audio'
        db.delete_table(u'audio')


    models = {
        'archives.audio': {
            'Meta': {'object_name': 'Audio', 'db_table': "u'audio'"},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'acanthes': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'annee': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'chemin_fichier': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'date_enregistrement': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'dateissued_portail': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'dateIssued_portail'", 'blank': 'True'}),
            'details_intranet_actuel_acda': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'details_intranet_actuel_ACDA'", 'blank': 'True'}),
            'duree': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'horodatage_creation': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'horodatage_modification': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'id_archive_audio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True', 'db_column': "'ID_archive_audio'"}),
            'kf_id_intervenant_principal': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_intervenant_principal'", 'blank': 'True'}),
            'kf_id_langue_1': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_langue_1'", 'blank': 'True'}),
            'kf_id_langue_2': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_langue_2'", 'blank': 'True'}),
            'kf_id_langue_3': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_langue_3'", 'blank': 'True'}),
            'kf_id_lieu': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_lieu'", 'blank': 'True'}),
            'kf_id_orchestre': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'kf_ID_orchestre'", 'blank': 'True'}),
            'lien_test_web': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_abstract': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_accesscondition': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_accessCondition'", 'blank': 'True'}),
            'oai_genre': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_id': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_language_languageterm_1': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_language_languageTerm_1'", 'blank': 'True'}),
            'oai_language_languageterm_2': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_language_languageTerm_2'", 'blank': 'True'}),
            'oai_language_languageterm_3': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_language_languageTerm_3'", 'blank': 'True'}),
            'oai_location_physicallocation': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_location_physicalLocation'", 'blank': 'True'}),
            'oai_location_url_full': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_location_url_preview': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_origininfo_datecaptured': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_originInfo_dateCaptured'", 'blank': 'True'}),
            'oai_origininfo_place': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_originInfo_place'", 'blank': 'True'}),
            'oai_origininfo_publisher': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_originInfo_publisher'", 'blank': 'True'}),
            'oai_physicaldescription_digitalorigin': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_physicalDescription_digitalOrigin'", 'blank': 'True'}),
            'oai_physicaldescription_form': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_physicalDescription_form'", 'blank': 'True'}),
            'oai_physicaldescription_internetmediatype': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_physicalDescription_internetMediaType'", 'blank': 'True'}),
            'oai_publication': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'oai_recordinfo_languageofcataloging_languageterm': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_recordInfo_languageOfCataloging_languageTerm'", 'blank': 'True'}),
            'oai_recordinfo_recordchangedate': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_recordInfo_recordChangeDate'", 'blank': 'True'}),
            'oai_recordinfo_recordcontentsource': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_recordInfo_recordContentSource'", 'blank': 'True'}),
            'oai_recordinfo_recordcreationdate': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_recordInfo_recordCreationDate'", 'blank': 'True'}),
            'oai_recordinfo_recordidentifier': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_recordInfo_recordIdentifier'", 'blank': 'True'}),
            'oai_targetaudience': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_targetAudience'", 'blank': 'True'}),
            'oai_titleinfo_title': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_titleInfo_title'", 'blank': 'True'}),
            'oai_typeofresource': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_typeOfResource'", 'blank': 'True'}),
            'oai_web_oai_mods': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'oai_WEB_OAI_MODS'", 'blank': 'True'}),
            'physicaldescription': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'physicalDescription'", 'blank': 'True'}),
            'remarque': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'subTitle'", 'blank': 'True'}),
            'total_durees': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'type_document': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'type_ircam': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'typeofresource': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'typeOfResource'", 'blank': 'True'}),
            'url_ecoute_extranet': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'url_ecoute_internet': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'url_ecoute_intranet': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'url_ecoute_intranet_adresse': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'blank': 'True'}),
            'url_export_ircam': ('django.db.models.fields.CharField', [], {'max_length': '15000', 'db_column': "'url_export IRCAM'", 'blank': 'True'})
        }
    }

    complete_apps = ['archives']