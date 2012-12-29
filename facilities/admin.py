from facilities.models import Facility, ManagingOrganisation, City,\
    Province, Address, Person, InstitutionType, NumberOfRooms,\
    Room, HealthCarer, HealthCarerType, NumberHealthCarers, Activity,\
    FacilityActivity, Image, DocumentCategory, Document
from django.contrib import admin

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'beds', 'bathroom', 
            'bathroom_has_shower', 'bathroom_has_bath', 'basin', 
            'overnight',]}),
    ]

class NumberOfRoomsInline(admin.TabularInline):
    model = NumberOfRooms
    ordering = ["room_type",]
    extra = 1

class NumberOfHealthCarersInline(admin.TabularInline):
    model = NumberHealthCarers
    extra = 1

class FacilityActivityInline(admin.TabularInline):
    model = FacilityActivity
    extra = 1
    
class DocumentInline(admin.StackedInline):
    model = Document
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class FacilityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'managing_organisation', 
            'institution_type','affiliated',]}),
        ('Contact information', {
            'classes': ('grp-collapse grp-open',),
            'fields': ['physical_address',
            'postal_address', 'landline', 'cell', 'fax', 'email',
            'website', 'contact',]}),
        ('Countable services', {
            'classes': ('grp-collapse grp-open',),
            'fields': ['dementia', 'frailcare', 
            'assisted', 'independent', 'psychiatric', 'respite', 
            'day_care', 'palliative',]}),
        ('Yes-No services', {
            'classes': ('grp-collapse grp-open',),
            'fields' : (
                ('nursing_care', 'occupational_therapy', 
                'physiotherapy','social_work',), 
                ('podiatrist','beautician', 'hairdresser',), 
                ('speech_therapy','audiology', 'optometry', ),
                ('gym', 'pharmacy_on_site',), 'care_plans',),}),
        ('Religion', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ['church', 'synagogue', 'mosque', 'temple',]}),
        ('Nearby', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ['nearest_secondary_hospital',
                'nearest_tertiary_hospital', 
                'nearest_private_hospital', 'nearest_pharmacy', ]}),
        ('Descriptive fields', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ['security', 'volunteer_program',
                'resident_committee', 'management_commitee','trustees',
                'visiting_hours', 'additional_features', 'notes',]}),
    ]
    list_display = ('id', 'name', 'physical_address',
        'date_modified', 'date_added')
    list_display_links = ('id', 'name',)
    list_filter = ('institution_type',)
    search_fields = ('id', 'name', 'physical_address__street',
        'physical_address__city__name',)
    raw_id_fields = ("physical_address", "postal_address",)
    autocomplete_lookup_fields = {
        'fk': ['physical_address', 'postal_address',],
    }
    save_on_top = True
    inlines = [
        NumberOfRoomsInline, NumberOfHealthCarersInline,
        FacilityActivityInline, ImageInline, DocumentInline
    ]


admin.site.register(Facility, FacilityAdmin)
admin.site.register(ManagingOrganisation)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(InstitutionType)
admin.site.register(Room, RoomAdmin)
admin.site.register(NumberOfRooms)
admin.site.register(HealthCarer) 
admin.site.register(HealthCarerType)
admin.site.register(NumberHealthCarers)
admin.site.register(FacilityActivity)
admin.site.register(Activity)
admin.site.register(Document)
admin.site.register(DocumentCategory)
admin.site.register(Image)
