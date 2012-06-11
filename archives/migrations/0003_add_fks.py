# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Audio.kf_id_orchestre'
        db.alter_column(u'audio', 'kf_ID_orchestre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archives.Orchestre'], db_column='kf_ID_orchestre'))
        # Adding index on 'Audio', fields ['kf_id_orchestre']
        db.create_index(u'audio', ['kf_ID_orchestre'])


        # Changing field 'Audio.kf_id_langue_1'
        db.alter_column(u'audio', 'kf_ID_langue_1', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archives.Langue'], db_column='kf_ID_langue_1'))
        # Adding index on 'Audio', fields ['kf_id_langue_1']
        db.create_index(u'audio', ['kf_ID_langue_1'])


        # Changing field 'Audio.kf_id_langue_3'
        db.alter_column(u'audio', 'kf_ID_langue_3', self.gf('django.db.models.fields.related.ForeignKey')(db_column='kf_ID_langue_3', to=orm['archives.Langue']))
        # Adding index on 'Audio', fields ['kf_id_langue_3']
        db.create_index(u'audio', ['kf_ID_langue_3'])


        # Changing field 'Audio.kf_id_langue_2'
        db.alter_column(u'audio', 'kf_ID_langue_2', self.gf('django.db.models.fields.related.ForeignKey')(db_column='kf_ID_langue_2', to=orm['archives.Langue']))
        # Adding index on 'Audio', fields ['kf_id_langue_2']
        db.create_index(u'audio', ['kf_ID_langue_2'])


        # Changing field 'Audio.kf_id_intervenant_principal'
        db.alter_column(u'audio', 'kf_ID_intervenant_principal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archives.Intervenant'], db_column='kf_ID_intervenant_principal'))
        # Adding index on 'Audio', fields ['kf_id_intervenant_principal']
        db.create_index(u'audio', ['kf_ID_intervenant_principal'])


        # Changing field 'Audio.kf_id_lieu'
        db.alter_column(u'audio', 'kf_ID_lieu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archives.Lieu'], db_column='kf_ID_lieu'))
        # Adding index on 'Audio', fields ['kf_id_lieu']
        db.create_index(u'audio', ['kf_ID_lieu'])


    def backwards(self, orm):
        # Removing index on 'Audio', fields ['kf_id_lieu']
        db.delete_index(u'audio', ['kf_ID_lieu'])

        # Removing index on 'Audio', fields ['kf_id_intervenant_principal']
        db.delete_index(u'audio', ['kf_ID_intervenant_principal'])

        # Removing index on 'Audio', fields ['kf_id_langue_2']
        db.delete_index(u'audio', ['kf_ID_langue_2'])

        # Removing index on 'Audio', fields ['kf_id_langue_3']
        db.delete_index(u'audio', ['kf_ID_langue_3'])

        # Removing index on 'Audio', fields ['kf_id_langue_1']
        db.delete_index(u'audio', ['kf_ID_langue_1'])

        # Removing index on 'Audio', fields ['kf_id_orchestre']
        db.delete_index(u'audio', ['kf_ID_orchestre'])


        # Changing field 'Audio.kf_id_orchestre'
        db.alter_column(u'audio', 'kf_ID_orchestre', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_orchestre'))

        # Changing field 'Audio.kf_id_langue_1'
        db.alter_column(u'audio', 'kf_ID_langue_1', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_1'))

        # Changing field 'Audio.kf_id_langue_3'
        db.alter_column(u'audio', 'kf_ID_langue_3', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_3'))

        # Changing field 'Audio.kf_id_langue_2'
        db.alter_column(u'audio', 'kf_ID_langue_2', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_langue_2'))

        # Changing field 'Audio.kf_id_intervenant_principal'
        db.alter_column(u'audio', 'kf_ID_intervenant_principal', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_intervenant_principal'))

        # Changing field 'Audio.kf_id_lieu'
        db.alter_column(u'audio', 'kf_ID_lieu', self.gf('django.db.models.fields.TextField')(db_column='kf_ID_lieu'))

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
            'kf_id_intervenant_principal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archives.Intervenant']", 'db_column': "'kf_ID_intervenant_principal'", 'blank': 'True'}),
            'kf_id_langue_1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archives.Langue']", 'db_column': "'kf_ID_langue_1'", 'blank': 'True'}),
            'kf_id_langue_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'langue_2'", 'blank': 'True', 'db_column': "'kf_ID_langue_2'", 'to': "orm['archives.Langue']"}),
            'kf_id_langue_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'langue_3'", 'blank': 'True', 'db_column': "'kf_ID_langue_3'", 'to': "orm['archives.Langue']"}),
            'kf_id_lieu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archives.Lieu']", 'db_column': "'kf_ID_lieu'", 'blank': 'True'}),
            'kf_id_orchestre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archives.Orchestre']", 'db_column': "'kf_ID_orchestre'", 'blank': 'True'}),
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