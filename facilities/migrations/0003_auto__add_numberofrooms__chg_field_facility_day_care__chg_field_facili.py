# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NumberOfRooms'
        db.create_table('facilities_numberofrooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('room_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Room'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('facilities', ['NumberOfRooms'])


        # Changing field 'Facility.day_care'
        db.alter_column('facilities_facility', 'day_care', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Facility.palliative'
        db.alter_column('facilities_facility', 'palliative', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Facility.respite'
        db.alter_column('facilities_facility', 'respite', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'Room.bathroom'
        db.add_column('facilities_room', 'bathroom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3, blank=True),
                      keep_default=False)

        # Adding field 'Room.bathroom_has_shower'
        db.add_column('facilities_room', 'bathroom_has_shower',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Room.bathroom_has_bath'
        db.add_column('facilities_room', 'bathroom_has_bath',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Room.basin'
        db.add_column('facilities_room', 'basin',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'NumberOfRooms'
        db.delete_table('facilities_numberofrooms')


        # Changing field 'Facility.day_care'
        db.alter_column('facilities_facility', 'day_care', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Facility.palliative'
        db.alter_column('facilities_facility', 'palliative', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Facility.respite'
        db.alter_column('facilities_facility', 'respite', self.gf('django.db.models.fields.BooleanField')())
        # Deleting field 'Room.bathroom'
        db.delete_column('facilities_room', 'bathroom')

        # Deleting field 'Room.bathroom_has_shower'
        db.delete_column('facilities_room', 'bathroom_has_shower')

        # Deleting field 'Room.bathroom_has_bath'
        db.delete_column('facilities_room', 'bathroom_has_bath')

        # Deleting field 'Room.basin'
        db.delete_column('facilities_room', 'basin')


    models = {
        'facilities.address': {
            'Meta': {'ordering': "['street']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.City']"}),
            'embedded_map': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Province']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.facility': {
            'Meta': {'ordering': "['name']", 'object_name': 'Facility'},
            'affiliated': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'assisted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Person']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'day_care': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'dementia': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'frailcare': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'independent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institution_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.InstitutionType']", 'null': 'True', 'blank': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'managing_organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.ManagingOrganisation']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'palliative': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'physical_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'physical'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'postal_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'postal'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'psychiatric': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'respite': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'facilities.institutiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'InstitutionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'facilities.managingorganisation': {
            'Meta': {'ordering': "['name']", 'object_name': 'ManagingOrganisation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.numberofrooms': {
            'Meta': {'object_name': 'NumberOfRooms'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'room_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Room']"})
        },
        'facilities.person': {
            'Meta': {'ordering': "['last', 'first']", 'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Address']", 'null': 'True', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'facilities.province': {
            'Meta': {'ordering': "['name']", 'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.room': {
            'Meta': {'object_name': 'Room'},
            'basin': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bathroom': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'bathroom_has_bath': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bathroom_has_shower': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'beds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['facilities']