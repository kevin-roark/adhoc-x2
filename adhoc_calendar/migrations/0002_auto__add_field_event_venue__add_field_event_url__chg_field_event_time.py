# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Event.venue'
        db.add_column('adhoc_calendar_event', 'venue', self.gf('django.db.models.fields.CharField')(default='285 Kent', max_length=255), keep_default=False)

        # Adding field 'Event.url'
        db.add_column('adhoc_calendar_event', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Changing field 'Event.timestamp'
        db.alter_column('adhoc_calendar_event', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Deleting field 'Event.venue'
        db.delete_column('adhoc_calendar_event', 'venue')

        # Deleting field 'Event.url'
        db.delete_column('adhoc_calendar_event', 'url')

        # Changing field 'Event.timestamp'
        db.alter_column('adhoc_calendar_event', 'timestamp', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'adhoc_calendar.event': {
            'Meta': {'object_name': 'Event'},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adhoc_calendar.EventImage']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'adhoc_calendar.eventimage': {
            'Meta': {'object_name': 'EventImage'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['adhoc_calendar']
