# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):
    
    def mark_youngest_child_as_true(self, state):
        children = list(state.followed_by_set.order_by('-modified').all())
        if len(children):
            youngest = children[0]
            youngest.valid = True
            youngest.save()
            self.mark_youngest_child_as_true(youngest)
    
    def forwards(self, orm):
        for startstate in orm['surveys.SurveyState'].objects.filter(
                previous_state=None).all():
            startstate.valid = True
            startstate.save()
            self.mark_youngest_child_as_true(startstate)
    
    
    def backwards(self, orm):
        "Write your backwards methods here."
    
    
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
