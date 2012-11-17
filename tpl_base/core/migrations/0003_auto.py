# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'LibraryAccount', fields ['card_number']
        db.create_index('core_libraryaccount', ['card_number'])


    def backwards(self, orm):
        # Removing index on 'LibraryAccount', fields ['card_number']
        db.delete_index('core_libraryaccount', ['card_number'])


    models = {
        'core.libraryaccount': {
            'Meta': {'object_name': 'LibraryAccount'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']