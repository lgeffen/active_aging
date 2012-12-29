# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ManagingOrganisation'
        db.create_table('facilities_managingorganisation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['ManagingOrganisation'])

        # Adding model 'City'
        db.create_table('facilities_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['City'])

        # Adding model 'Province'
        db.create_table('facilities_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['Province'])

        # Adding model 'Address'
        db.create_table('facilities_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.City'])),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Province'])),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('gps', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('embedded_map', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('facilities', ['Address'])

        # Adding model 'Person'
        db.create_table('facilities_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Address'], null=True, blank=True)),
        ))
        db.send_create_signal('facilities', ['Person'])

        # Adding model 'InstitutionType'
        db.create_table('facilities_institutiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('facilities', ['InstitutionType'])

        # Adding model 'Facility'
        db.create_table('facilities_facility', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('managing_organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.ManagingOrganisation'], null=True, blank=True)),
            ('physical_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='physical', null=True, to=orm['facilities.Address'])),
            ('postal_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='postal', null=True, to=orm['facilities.Address'])),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Person'], null=True, blank=True)),
            ('institution_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.InstitutionType'], null=True, blank=True)),
            ('affiliated', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dementia', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('frailcare', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('assisted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('independent', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('psychiatric', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('respite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('day_care', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('palliative', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('one_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('two_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('three_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('four_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('five_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('six_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gt_six_beds', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('facilities', ['Facility'])


    def backwards(self, orm):
        # Deleting model 'ManagingOrganisation'
        db.delete_table('facilities_managingorganisation')

        # Deleting model 'City'
        db.delete_table('facilities_city')

        # Deleting model 'Province'
        db.delete_table('facilities_province')

        # Deleting model 'Address'
        db.delete_table('facilities_address')

        # Deleting model 'Person'
        db.delete_table('facilities_person')

        # Deleting model 'InstitutionType'
        db.delete_table('facilities_institutiontype')

        # Deleting model 'Facility'
        db.delete_table('facilities_facility')


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
            'five_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'four_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'frailcare': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gt_six_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'independent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institution_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.InstitutionType']", 'null': 'True', 'blank': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'managing_organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.ManagingOrganisation']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'one_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'palliative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physical_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'physical'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'postal_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'postal'", 'null': 'True', 'to': "orm['facilities.Address']"}),
            'psychiatric': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'respite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'six_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'three_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two_beds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        }
    }

    complete_apps = ['facilities']