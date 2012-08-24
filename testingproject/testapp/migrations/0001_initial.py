# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyInfo'
        db.create_table('testapp_myinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_cont', self.gf('django.db.models.fields.TextField')()),
            ('my_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('testapp', ['MyInfo'])

        # Adding model 'ReqsHistory'
        db.create_table('testapp_reqshistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('req_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('req_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('req_ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('req_priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('testapp', ['ReqsHistory'])

        # Adding model 'ModelLog'
        db.create_table('testapp_modellog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('target_instance', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('change_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('testapp', ['ModelLog'])


    def backwards(self, orm):
        # Deleting model 'MyInfo'
        db.delete_table('testapp_myinfo')

        # Deleting model 'ReqsHistory'
        db.delete_table('testapp_reqshistory')

        # Deleting model 'ModelLog'
        db.delete_table('testapp_modellog')


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