# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReqsHistory.req_priority'
        db.add_column('testapp_reqshistory', 'req_priority',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReqsHistory.req_priority'
        db.delete_column('testapp_reqshistory', 'req_priority')


    models = {
        'testapp.modellog': {
            'Meta': {'object_name': 'ModelLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'change_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'target_instance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'testapp.myinfo': {
            'Meta': {'object_name': 'MyInfo'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'my_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_cont': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'testapp.reqshistory': {
            'Meta': {'object_name': 'ReqsHistory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req_ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'req_priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'req_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'req_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['testapp']