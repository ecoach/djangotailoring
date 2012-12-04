# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SurveyState.valid'
        db.add_column('surveys_surveystate', 'valid', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SurveyState.valid'
        db.delete_column('surveys_surveystate', 'valid')


    models = {
        'surveys.surveystate': {
            'Meta': {'object_name': 'SurveyState'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_page_data': ('djangotailoring.surveys.fields.JSONField', [], {'default': "'{}'"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page_msgid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'previous_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'followed_by_set'", 'null': 'True', 'to': "orm['surveys.SurveyState']"}),
            'running_subject_data': ('djangotailoring.surveys.fields.JSONField', [], {'default': "'{}'"}),
            'survey_id': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'validation_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['surveys']
