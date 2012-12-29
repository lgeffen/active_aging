# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Images'
        db.create_table('facilities_images', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('photographer', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('facilities', ['Images'])

        # Adding model 'FacilityPrice'
        db.create_table('facilities_facilityprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('price_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.PriceCategory'])),
            ('from_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('to_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('prices_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('facilities', ['FacilityPrice'])

        # Adding model 'HealthCarer'
        db.create_table('facilities_healthcarer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carer_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.HealthCarerType'])),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
        ))
        db.send_create_signal('facilities', ['HealthCarer'])

        # Adding model 'Document'
        db.create_table('facilities_document', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('document_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.DocumentCategory'])),
            ('file_name', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('period_begin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('period_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('facilities', ['Document'])

        # Adding model 'HealthCarerType'
        db.create_table('facilities_healthcarertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['HealthCarerType'])

        # Adding model 'Activity'
        db.create_table('facilities_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['Activity'])

        # Adding model 'FacilityActivity'
        db.create_table('facilities_facilityactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Activity'])),
        ))
        db.send_create_signal('facilities', ['FacilityActivity'])

        # Adding model 'PriceCategory'
        db.create_table('facilities_pricecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['PriceCategory'])

        # Adding model 'DocumentCategory'
        db.create_table('facilities_documentcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('facilities', ['DocumentCategory'])

        # Adding model 'NumberHealthCarers'
        db.create_table('facilities_numberhealthcarers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('health_carer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.HealthCarer'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('facilities', ['NumberHealthCarers'])

        # Adding field 'Facility.registration_number'
        db.add_column('facilities_facility', 'registration_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Facility.waiting_list'
        db.add_column('facilities_facility', 'waiting_list',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Facility.podiatrist'
        db.add_column('facilities_facility', 'podiatrist',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.beautician'
        db.add_column('facilities_facility', 'beautician',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.hairdresser'
        db.add_column('facilities_facility', 'hairdresser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.occupational_therapy'
        db.add_column('facilities_facility', 'occupational_therapy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.physiotherapy'
        db.add_column('facilities_facility', 'physiotherapy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.social_work'
        db.add_column('facilities_facility', 'social_work',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.library'
        db.add_column('facilities_facility', 'library',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.church'
        db.add_column('facilities_facility', 'church',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.synagogue'
        db.add_column('facilities_facility', 'synagogue',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.mosque'
        db.add_column('facilities_facility', 'mosque',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.temple'
        db.add_column('facilities_facility', 'temple',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.gym'
        db.add_column('facilities_facility', 'gym',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.speech_therapy'
        db.add_column('facilities_facility', 'speech_therapy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.nursing_care'
        db.add_column('facilities_facility', 'nursing_care',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.audiology'
        db.add_column('facilities_facility', 'audiology',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.optometry'
        db.add_column('facilities_facility', 'optometry',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.nearest_chc'
        db.add_column('facilities_facility', 'nearest_chc',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Facility.nearest_secondary_hospital'
        db.add_column('facilities_facility', 'nearest_secondary_hospital',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Facility.nearest_tertiary_hospital'
        db.add_column('facilities_facility', 'nearest_tertiary_hospital',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Facility.nearest_private_hospital'
        db.add_column('facilities_facility', 'nearest_private_hospital',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Facility.pharmacy_on_site'
        db.add_column('facilities_facility', 'pharmacy_on_site',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.nearest_pharmacy'
        db.add_column('facilities_facility', 'nearest_pharmacy',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Facility.care_plans'
        db.add_column('facilities_facility', 'care_plans',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Facility.security'
        db.add_column('facilities_facility', 'security',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.visiting_hours'
        db.add_column('facilities_facility', 'visiting_hours',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.volunteer_program'
        db.add_column('facilities_facility', 'volunteer_program',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.additional_features'
        db.add_column('facilities_facility', 'additional_features',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.notes'
        db.add_column('facilities_facility', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.resident_committee'
        db.add_column('facilities_facility', 'resident_committee',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.management_commitee'
        db.add_column('facilities_facility', 'management_commitee',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Facility.trustees'
        db.add_column('facilities_facility', 'trustees',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Room.overnight'
        db.add_column('facilities_room', 'overnight',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Images'
        db.delete_table('facilities_images')

        # Deleting model 'FacilityPrice'
        db.delete_table('facilities_facilityprice')

        # Deleting model 'HealthCarer'
        db.delete_table('facilities_healthcarer')

        # Deleting model 'Document'
        db.delete_table('facilities_document')

        # Deleting model 'HealthCarerType'
        db.delete_table('facilities_healthcarertype')

        # Deleting model 'Activity'
        db.delete_table('facilities_activity')

        # Deleting model 'FacilityActivity'
        db.delete_table('facilities_facilityactivity')

        # Deleting model 'PriceCategory'
        db.delete_table('facilities_pricecategory')

        # Deleting model 'DocumentCategory'
        db.delete_table('facilities_documentcategory')

        # Deleting model 'NumberHealthCarers'
        db.delete_table('facilities_numberhealthcarers')

        # Deleting field 'Facility.registration_number'
        db.delete_column('facilities_facility', 'registration_number')

        # Deleting field 'Facility.waiting_list'
        db.delete_column('facilities_facility', 'waiting_list')

        # Deleting field 'Facility.podiatrist'
        db.delete_column('facilities_facility', 'podiatrist')

        # Deleting field 'Facility.beautician'
        db.delete_column('facilities_facility', 'beautician')

        # Deleting field 'Facility.hairdresser'
        db.delete_column('facilities_facility', 'hairdresser')

        # Deleting field 'Facility.occupational_therapy'
        db.delete_column('facilities_facility', 'occupational_therapy')

        # Deleting field 'Facility.physiotherapy'
        db.delete_column('facilities_facility', 'physiotherapy')

        # Deleting field 'Facility.social_work'
        db.delete_column('facilities_facility', 'social_work')

        # Deleting field 'Facility.library'
        db.delete_column('facilities_facility', 'library')

        # Deleting field 'Facility.church'
        db.delete_column('facilities_facility', 'church')

        # Deleting field 'Facility.synagogue'
        db.delete_column('facilities_facility', 'synagogue')

        # Deleting field 'Facility.mosque'
        db.delete_column('facilities_facility', 'mosque')

        # Deleting field 'Facility.temple'
        db.delete_column('facilities_facility', 'temple')

        # Deleting field 'Facility.gym'
        db.delete_column('facilities_facility', 'gym')

        # Deleting field 'Facility.speech_therapy'
        db.delete_column('facilities_facility', 'speech_therapy')

        # Deleting field 'Facility.nursing_care'
        db.delete_column('facilities_facility', 'nursing_care')

        # Deleting field 'Facility.audiology'
        db.delete_column('facilities_facility', 'audiology')

        # Deleting field 'Facility.optometry'
        db.delete_column('facilities_facility', 'optometry')

        # Deleting field 'Facility.nearest_chc'
        db.delete_column('facilities_facility', 'nearest_chc')

        # Deleting field 'Facility.nearest_secondary_hospital'
        db.delete_column('facilities_facility', 'nearest_secondary_hospital')

        # Deleting field 'Facility.nearest_tertiary_hospital'
        db.delete_column('facilities_facility', 'nearest_tertiary_hospital')

        # Deleting field 'Facility.nearest_private_hospital'
        db.delete_column('facilities_facility', 'nearest_private_hospital')

        # Deleting field 'Facility.pharmacy_on_site'
        db.delete_column('facilities_facility', 'pharmacy_on_site')

        # Deleting field 'Facility.nearest_pharmacy'
        db.delete_column('facilities_facility', 'nearest_pharmacy')

        # Deleting field 'Facility.care_plans'
        db.delete_column('facilities_facility', 'care_plans')

        # Deleting field 'Facility.security'
        db.delete_column('facilities_facility', 'security')

        # Deleting field 'Facility.visiting_hours'
        db.delete_column('facilities_facility', 'visiting_hours')

        # Deleting field 'Facility.volunteer_program'
        db.delete_column('facilities_facility', 'volunteer_program')

        # Deleting field 'Facility.additional_features'
        db.delete_column('facilities_facility', 'additional_features')

        # Deleting field 'Facility.notes'
        db.delete_column('facilities_facility', 'notes')

        # Deleting field 'Facility.resident_committee'
        db.delete_column('facilities_facility', 'resident_committee')

        # Deleting field 'Facility.management_commitee'
        db.delete_column('facilities_facility', 'management_commitee')

        # Deleting field 'Facility.trustees'
        db.delete_column('facilities_facility', 'trustees')

        # Deleting field 'Room.overnight'
        db.delete_column('facilities_room', 'overnight')


    models = {
        'facilities.activity': {
            'Meta': {'object_name': 'Activity'},
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
            'Meta': {'object_name': 'HealthCarer'},
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
        'facilities.images': {
            'Meta': {'ordering': "['facility', 'date_taken']", 'object_name': 'Images'},
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
            'Meta': {'ordering': "['name', 'beds']", 'object_name': 'Room'},
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