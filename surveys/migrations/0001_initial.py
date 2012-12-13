# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SurveyState'
        db.create_table('surveys_surveystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('survey_id', self.gf('django.db.models.fields.TextField')()),
            ('page_msgid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('running_subject_data', self.gf('djangotailoring.surveys.fields.JSONField')(default='{}')),
            ('latest_page_data', self.gf('djangotailoring.surveys.fields.JSONField')(default='{}')),
            ('validation_errors', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='followed_by_set', null=True, to=orm['surveys.SurveyState'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('surveys', ['SurveyState'])


    def backwards(self, orm):
        
        # Deleting model 'SurveyState'
        db.delete_table('surveys_surveystate')


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
            'validation_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['surveys']
