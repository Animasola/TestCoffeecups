# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelLog'
        db.create_table('testapp_modellog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('id_zap', self.gf('django.db.models.fields.IntegerField')()),
            ('change_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('testapp', ['ModelLog'])


    def backwards(self, orm):
        # Deleting model 'ModelLog'
        db.delete_table('testapp_modellog')


    models = {
        'testapp.modellog': {
            'Meta': {'object_name': 'ModelLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'change_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_zap': ('django.db.models.fields.IntegerField', [], {}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'req_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'req_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['testapp']