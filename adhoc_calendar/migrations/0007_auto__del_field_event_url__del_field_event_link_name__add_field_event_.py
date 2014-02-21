# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.url'
        db.delete_column('adhoc_calendar_event', 'url')

        # Deleting field 'Event.link_name'
        db.delete_column('adhoc_calendar_event', 'link_name')

        # Adding field 'Event.address'
        db.add_column('adhoc_calendar_event', 'address', self.gf('django.db.models.fields.TextField')(default='526 W. 114th St. New York, NY'), keep_default=False)

        # Adding field 'Event.url1'
        db.add_column('adhoc_calendar_event', 'url1', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Event.link_name1'
        db.add_column('adhoc_calendar_event', 'link_name1', self.gf('django.db.models.fields.CharField')(default='RSVP', max_length=140), keep_default=False)

        # Adding field 'Event.url2'
        db.add_column('adhoc_calendar_event', 'url2', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Event.link_name2'
        db.add_column('adhoc_calendar_event', 'link_name2', self.gf('django.db.models.fields.CharField')(default='Tickets', max_length=140), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Event.url'
        db.add_column('adhoc_calendar_event', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Event.link_name'
        db.add_column('adhoc_calendar_event', 'link_name', self.gf('django.db.models.fields.CharField')(default='RSVP', max_length=140), keep_default=False)

        # Deleting field 'Event.address'
        db.delete_column('adhoc_calendar_event', 'address')

        # Deleting field 'Event.url1'
        db.delete_column('adhoc_calendar_event', 'url1')

        # Deleting field 'Event.link_name1'
        db.delete_column('adhoc_calendar_event', 'link_name1')

        # Deleting field 'Event.url2'
        db.delete_column('adhoc_calendar_event', 'url2')

        # Deleting field 'Event.link_name2'
        db.delete_column('adhoc_calendar_event', 'link_name2')


    models = {
        'adhoc_calendar.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adhoc_calendar.EventImage']", 'null': 'True', 'blank': 'True'}),
            'link_name1': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'link_name2': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
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
