# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table('facilities_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('facilities', ['Room'])

        # Deleting field 'Facility.four_beds'
        db.delete_column('facilities_facility', 'four_beds')

        # Deleting field 'Facility.three_beds'
        db.delete_column('facilities_facility', 'three_beds')

        # Deleting field 'Facility.one_beds'
        db.delete_column('facilities_facility', 'one_beds')

        # Deleting field 'Facility.two_beds'
        db.delete_column('facilities_facility', 'two_beds')

        # Deleting field 'Facility.five_beds'
        db.delete_column('facilities_facility', 'five_beds')

        # Deleting field 'Facility.gt_six_beds'
        db.delete_column('facilities_facility', 'gt_six_beds')

        # Deleting field 'Facility.six_beds'
        db.delete_column('facilities_facility', 'six_beds')


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table('facilities_room')

        # Adding field 'Facility.four_beds'
        db.add_column('facilities_facility', 'four_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.three_beds'
        db.add_column('facilities_facility', 'three_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.one_beds'
        db.add_column('facilities_facility', 'one_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.two_beds'
        db.add_column('facilities_facility', 'two_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.five_beds'
        db.add_column('facilities_facility', 'five_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.gt_six_beds'
        db.add_column('facilities_facility', 'gt_six_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facility.six_beds'
        db.add_column('facilities_facility', 'six_beds',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
            'day_care': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'palliative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physical_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'physical'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'postal_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'postal'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'psychiatric': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'respite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'beds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['facilities']