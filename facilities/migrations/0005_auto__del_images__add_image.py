# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Images'
        db.delete_table('facilities_images')

        # Adding model 'Image'
        db.create_table('facilities_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('photographer', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('facilities', ['Image'])


    def backwards(self, orm):
        # Adding model 'Images'
        db.create_table('facilities_images', (
            ('date_taken', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('photographer', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('facilities', ['Images'])

        # Deleting model 'Image'
        db.delete_table('facilities_image')


    models = {
        'facilities.activity': {
            'Meta': {'ordering': "['name']", 'object_name': 'Activity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
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
        'facilities.document': {
            'Meta': {'ordering': "['facility', 'document_category', 'date_published', 'period_begin', 'period_end']", 'object_name': 'Document'},
            'date_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.DocumentCategory']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_begin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'facilities.documentcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'DocumentCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.facility': {
            'Meta': {'ordering': "['name']", 'object_name': 'Facility'},
            'additional_features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'affiliated': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'assisted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'audiology': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beautician': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'care_plans': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Person']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'day_care': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'dementia': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'frailcare': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gym': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hairdresser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'independent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institution_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.InstitutionType']", 'null': 'True', 'blank': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'library': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'management_commitee': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'managing_organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.ManagingOrganisation']", 'null': 'True', 'blank': 'True'}),
            'mosque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nearest_chc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nearest_pharmacy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nearest_private_hospital': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nearest_secondary_hospital': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nearest_tertiary_hospital': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nursing_care': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupational_therapy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'optometry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'palliative': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'pharmacy_on_site': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physical_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'physical'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'physiotherapy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'podiatrist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postal_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'postal'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'psychiatric': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'resident_committee': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'respite': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'security': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'social_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speech_therapy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'synagogue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'temple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trustees': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'visiting_hours': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'volunteer_program': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'waiting_list': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'facilities.facilityactivity': {
            'Meta': {'ordering': "['facility', 'activity']", 'object_name': 'FacilityActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Activity']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'facilities.facilityprice': {
            'Meta': {'ordering': "['facility', 'from_amount', 'to_amount']", 'object_name': 'FacilityPrice'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'from_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.PriceCategory']"}),
            'prices_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'to_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'facilities.healthcarer': {
            'Meta': {'ordering': "['carer_type', 'frequency']", 'object_name': 'HealthCarer'},
            'carer_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.HealthCarerType']"}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        'facilities.healthcarertype': {
            'Meta': {'ordering': "['name']", 'object_name': 'HealthCarerType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.image': {
            'Meta': {'ordering': "['facility', 'date_taken']", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photographer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
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
        'facilities.numberhealthcarers': {
            'Meta': {'ordering': "['facility', 'health_carer', 'number']", 'object_name': 'NumberHealthCarers'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'health_carer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.HealthCarer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'facilities.numberofrooms': {
            'Meta': {'ordering': "['facility', 'room_type', 'number']", 'object_name': 'NumberOfRooms'},
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
        'facilities.pricecategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'PriceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.province': {
            'Meta': {'ordering': "['name']", 'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'facilities.room': {
            'Meta': {'ordering': "['beds', 'name']", 'object_name': 'Room'},
            'basin': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bathroom': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'bathroom_has_bath': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bathroom_has_shower': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'beds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'overnight': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['facilities']