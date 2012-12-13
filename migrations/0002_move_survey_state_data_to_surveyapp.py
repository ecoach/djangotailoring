# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from django.db.models.fields import DateTimeField

# copied from djangotailoring.surveys.models.SurveyState
def rebuild_running_subject_data(new_state):
    if new_state.previous_state is not None:
        running_data = rebuild_running_subject_data(new_state.previous_state)
    else:
        running_data = new_state.running_subject_data.copy()
    running_data.update(new_state.latest_page_data)
    return running_data

def kill_auto_now_features(modelclass):
    datetime_fields = [f for f in modelclass._meta.fields
                       if isinstance(f, DateTimeField)]
    for f in datetime_fields:
        f.auto_now_add = False
        f.auto_now = False

class Migration(DataMigration):
    
    depends_on = (
        ('surveys', '0001_initial'),
    )
    
    def forwards(self, orm):
        state_map = {}
        old_SurveyState = orm['djangotailoring.SurveyState']
        new_SurveyState = orm['surveys.SurveyState']
        kill_auto_now_features(old_SurveyState)
        kill_auto_now_features(new_SurveyState)
        for old_state in old_SurveyState.objects.all():
            new_state = new_SurveyState.objects.create(
                user_id=old_state.userid,
                survey_id=old_state.surveyid,
                page_msgid=old_state.pagemsgid,
                latest_page_data=old_state.latest_page_data,
                validation_errors=old_state.validation_errors,
                created=old_state.created,
                modified=old_state.modified
            )
            state_map[old_state] = new_state
        # re-map the previous_state pointers
        for old_state, new_state in state_map.items():
            if old_state.previous_state is not None:
                new_state.previous_state = state_map[old_state.previous_state]
            # re-build the running_subject_data
            new_state.running_subject_data = rebuild_running_subject_data(
                new_state)
            new_state.save()
    
    
    def backwards(self, orm):
        pass
    
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
        },
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

    complete_apps = ['surveys', 'djangotailoring']
