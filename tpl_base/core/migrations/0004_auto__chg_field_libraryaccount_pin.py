# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LibraryAccount.pin'
        db.alter_column('core_libraryaccount', 'pin', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'LibraryAccount.pin'
        db.alter_column('core_libraryaccount', 'pin', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'core.libraryaccount': {
            'Meta': {'object_name': 'LibraryAccount'},
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['core']