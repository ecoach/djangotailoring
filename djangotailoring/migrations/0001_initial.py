# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'SerializedSubjectData'
        db.create_table('djangotailoring_serializedsubjectdata', (
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='user_id')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_data', self.gf('django.db.models.fields.TextField')(db_column='primary_data')),
        ))
        db.send_create_signal('djangotailoring', ['SerializedSubjectData'])

        # Adding model 'SurveyState'
        db.create_table('djangotailoring_surveystate', (
            ('validation_errors', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pagemsgid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('userid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('previous_state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='followed_by_set', null=True, to=orm['djangotailoring.SurveyState'])),
            ('latest_page_data', self.gf('django.db.models.fields.TextField')(default='{}')),
            ('surveyid', self.gf('django.db.models.fields.TextField')()),
            ('subject_data', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('djangotailoring', ['SurveyState'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'SerializedSubjectData'
        db.delete_table('djangotailoring_serializedsubjectdata')

        # Deleting model 'SurveyState'
        db.delete_table('djangotailoring_surveystate')
    
    
    models = {
        'djangotailoring.serializedsubjectdata': {
            'Meta': {'object_name': 'SerializedSubjectData'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_data': ('django.db.models.fields.TextField', [], {'db_column': "'primary_data'"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'user_id'"})
        },
        'djangotailoring.surveystate': {
            'Meta': {'object_name': 'SurveyState'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_page_data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pagemsgid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'previous_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'followed_by_set'", 'null': 'True', 'to': "orm['djangotailoring.SurveyState']"}),
            'subject_data': ('django.db.models.fields.TextField', [], {}),
            'surveyid': ('django.db.models.fields.TextField', [], {}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'validation_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }
    
    complete_apps = ['djangotailoring']
