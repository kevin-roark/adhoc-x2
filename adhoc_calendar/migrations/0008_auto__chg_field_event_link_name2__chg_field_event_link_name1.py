# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Event.link_name2'
        db.alter_column('adhoc_calendar_event', 'link_name2', self.gf('django.db.models.fields.CharField')(max_length=140, null=True))

        # Changing field 'Event.link_name1'
        db.alter_column('adhoc_calendar_event', 'link_name1', self.gf('django.db.models.fields.CharField')(max_length=140, null=True))


    def backwards(self, orm):
        
        # Changing field 'Event.link_name2'
        db.alter_column('adhoc_calendar_event', 'link_name2', self.gf('django.db.models.fields.CharField')(default='Tickets', max_length=140))

        # Changing field 'Event.link_name1'
        db.alter_column('adhoc_calendar_event', 'link_name1', self.gf('django.db.models.fields.CharField')(default='RSVP', max_length=140))


    models = {
        'adhoc_calendar.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adhoc_calendar.EventImage']", 'null': 'True', 'blank': 'True'}),
            'link_name1': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'link_name2': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url1': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
