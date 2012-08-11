# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReqsHistory'
        db.create_table('testapp_reqshistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('req_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('req_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('req_ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('testapp', ['ReqsHistory'])


    def backwards(self, orm):
        # Deleting model 'ReqsHistory'
        db.delete_table('testapp_reqshistory')


    models = {
        'testapp.myinfo': {
            'Meta': {'object_name': 'MyInfo'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['testapp']