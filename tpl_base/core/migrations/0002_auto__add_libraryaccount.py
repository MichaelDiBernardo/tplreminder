# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LibraryAccount'
        db.create_table('core_libraryaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('card_number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pin', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_check', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('core', ['LibraryAccount'])


    def backwards(self, orm):
        # Deleting model 'LibraryAccount'
        db.delete_table('core_libraryaccount')


    models = {
        'core.libraryaccount': {
            'Meta': {'object_name': 'LibraryAccount'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']