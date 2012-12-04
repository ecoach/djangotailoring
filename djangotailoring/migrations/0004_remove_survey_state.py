# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SurveyState'
        db.delete_table('djangotailoring_surveystate')

    def backwards(self, orm):     
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
    
    
    models = {
        'djangotailoring.serializedsubjectdata': {
            'Meta': {'object_name': 'SerializedSubjectData'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_data': ('django.db.models.fields.TextField', [], {'db_column': "'primary_data'"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'user_id'"})
        }
    }

    complete_apps = ['djangotailoring']
