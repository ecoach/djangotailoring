# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.utils import simplejson as json

from django.db.models.fields import DateTimeField

def kill_auto_now_features(modelclass):
    datetime_fields = [f for f in modelclass._meta.fields
                       if isinstance(f, DateTimeField)]
    for f in datetime_fields:
        f.auto_now_add = False
        f.auto_now = False

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."


    def backwards(self, orm):
        state_map = {}
        old_SurveyState = orm['djangotailoring.SurveyState']
        new_SurveyState = orm['surveys.SurveyState']
        kill_auto_now_features(old_SurveyState)
        kill_auto_now_features(new_SurveyState)
        for new_state in new_SurveyState.objects.all():
            old_state = old_SurveyState.objects.create(
                userid=new_state.user_id,
                surveyid=new_state.survey_id,
                pagemsgid=new_state.page_msgid,
                latest_page_data=new_state.latest_page_data,
                validation_errors=new_state.validation_errors,
                created=new_state.created,
                modified=new_state.modified
            )
            state_map[new_state] = old_state
        # re-map the previous_state pointers
        for new_state, old_state in state_map.items():
            if new_state.previous_state is not None:
                old_state.previous_state = state_map[new_state.previous_state]
            # re-build the subject_data
            # NOTE: this is a lossy conversion, assumes the destination source is 
            # the empty source.
            old_state.subject_data = json.dumps({'':new_state.running_subject_data})
            old_state.save()
        


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
