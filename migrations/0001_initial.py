# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SerializedSubjectData'
        db.create_table('djangotailoring_serializedsubjectdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='user_id')),
            ('primary_data', self.gf('django.db.models.fields.TextField')(db_column='primary_data')),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('djangotailoring', ['SerializedSubjectData'])


    def backwards(self, orm):
        # Deleting model 'SerializedSubjectData'
        db.delete_table('djangotailoring_serializedsubjectdata')


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