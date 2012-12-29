from django.db import models
from django.utils.translation import ugettext as _

BATHROOM_CHOICES = (
    (u'ES', _(u'en suite')),
    (u'EX', _(u'exclusive to room')),
    (u'CO', _(u'communal')),
)

SECTOR_CHOICES = (
    (u'PR', _(u'private')),
    (u'ST', _(u'state')),
    (u'NO', _(u'none')),
)

FREQUENCY_CHOICES = (
    (u'DW', _(u'every week day')),
    (u'DE', _(u'everyday')),
    (u'OW', _(u'once weekly')),
    (u'OR', _(u'on request')),
    (u'NO', _(u'none')),
)

OVERNIGHT_CHOICES = (
    (u'AL', _(u'always')),
    (u'FR', _(u'to assist with frailcare')),
)

class ManagingOrganisation(models.Model):
    name = models.CharField(_("name"), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("managing organisation")
        verbose_name_plural = _("managing organisations")
        ordering = ["name",]

class City(models.Model):
    name = models.CharField(_("name"), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("town or city")
        verbose_name_plural = _("towns and cities")
        ordering = ["name",]
    
class Province(models.Model):
    name = models.CharField(_("name"), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("managing organisation")
        verbose_name_plural = _("managing organisations")

    class Meta:
        verbose_name = _("province or state")
        verbose_name_plural = _("provinces and states")
        ordering = ["name",]
        
class Address(models.Model):
    street = models.CharField(_("street or post box"), 
        max_length=200)
    city = models.ForeignKey(City, verbose_name=_("city or town"))
    province = models.ForeignKey(Province, 
        verbose_name=_("province or state"))
    postal_code = models.CharField(_("postal code"), max_length=20, 
        blank=True)
    gps = models.CharField(_("gps co-ordinates"), max_length=50, 
        blank=True)
    embedded_map = models.CharField("embedded map", max_length=200,
        help_text=_("HTML for embedded map from, for example, "
                "Google Maps."), blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "street__icontains",)

    def __unicode__(self):
        return u' '.join([self.street, unicode(self.city), \
            unicode(self.province), self.postal_code, self.gps])

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ["street",]

class Person(models.Model):
    first = models.CharField(_("first name"), max_length=200)
    middle = models.CharField(_("middle names"), max_length=200, 
        blank=True)
    last = models.CharField(_("last name"), max_length=200)
    landline = models.CharField(_("telephone number"), max_length=20,
        blank=True)
    cell = models.CharField(_("mobile phone number"), max_length=20,
        blank=True)
    email = models.EmailField(_("email"), blank=True)
    address = models.ForeignKey(Address, verbose_name=_("address"), 
        blank=True, null=True)

    def __unicode__(self):
        return u' '.join([self.first, self.middle, 
            self.last, self.email])

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("people")
        ordering = ["last", "first",]

class InstitutionType(models.Model):
    name = models.CharField(_("name"), max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("institution type")
        verbose_name_plural = _("institution types")
        ordering = ["name"]

class Room(models.Model):
    beds = models.IntegerField(_("number of beds"), blank=True, 
        null=True)
    bathroom = models.CharField(_("type of bathroom"), max_length=3,
        choices=BATHROOM_CHOICES, blank=True)    
    bathroom_has_shower = models.NullBooleanField(
        _("bathroom has shower"), blank=True, null=True)
    bathroom_has_bath = models.NullBooleanField(_("bathroom has bath"),
        blank=True, null=True)
    basin = models.NullBooleanField(_("room has private basin"),
        blank=True, null=True)
    name = models.CharField(_("name"), max_length=200, blank=True)
    overnight = models.CharField(_("overnight visitors"), max_length=3,
        choices=OVERNIGHT_CHOICES, blank=True)

    def __unicode__(self):
        return ' '.join([self.name, unicode(self.beds), _("bed(s),"),
            _("bathroom "), self.get_bathroom_display()])

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
        ordering = ["beds", "name",]


class HealthCarerType(models.Model):
    name = models.CharField(_("type of health carer"), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("health carer type")
        verbose_name_plural = _("health carer types")
        ordering = ["name", ]


class HealthCarer(models.Model):
    carer_type = models.ForeignKey(HealthCarerType, 
        verbose_name=_("carer type"))
    frequency = models.CharField(choices=FREQUENCY_CHOICES, 
        max_length=3)
    sector = models.CharField(choices=SECTOR_CHOICES, 
        max_length=3, blank=True)
        
    def __unicode__(self):
        return ' '.join([unicode(self.carer_type), 
            self.get_frequency_display(), self.get_sector_display()])

    class Meta:
        verbose_name = _("health carer")
        verbose_name_plural = _("health carers")
        ordering = ["carer_type", "frequency",]


class Activity(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")
        ordering = ["name",]


class Facility(models.Model):
    name = models.CharField(_("name"), max_length=200)
    managing_organisation = models.ForeignKey(ManagingOrganisation,
        blank=True, null=True)
    physical_address = models.ForeignKey(Address, 
        related_name="physical", verbose_name=_("physical address"),
        blank=True, null=True)
    postal_address = models.ForeignKey(Address,
        related_name="postal", verbose_name=_("postal address"), 
        blank=True, null=True)
    landline = models.CharField(_("telephone number"), max_length=20,
        blank=True)
    cell = models.CharField(_("mobile phone number"), max_length=20,
        blank=True)
    fax = models.CharField(_("fax number"), max_length=20, blank=True)
    email = models.EmailField(_("email"), blank=True)
    website = models.URLField(verify_exists=False, blank=True,
        verbose_name=_("website"))
    contact = models.ForeignKey(Person, 
        verbose_name=_("contact person"), blank=True, null=True)
    institution_type = models.ForeignKey(InstitutionType, 
        verbose_name="institution type", blank=True, null=True)
    registration_number = models.CharField(_("registration number"), 
        max_length=50, blank=True)
    affiliated = models.CharField(_("affiliated organisation"), 
        max_length=200, blank=True)
    waiting_list = models.IntegerField(
        _("average time on waiting list in days"), 
            blank=True, null=True)        
    dementia = models.IntegerField(_("dementia"), default=0)
    frailcare = models.IntegerField(_("frailcare"), default=0)
    assisted = models.IntegerField(_("assisted living"), default=0)
    independent = models.IntegerField(_("independent living"), 
        default=0)
    psychiatric = models.IntegerField(_("psychiatric care"), default=0) 
    respite = models.IntegerField(_("respite care"), default=False)
    day_care = models.IntegerField(_("day care"), default=False)
    palliative = models.IntegerField(_("palliative"), default=False)
    podiatrist = models.BooleanField(_("podiatrist"), default=False)
    beautician = models.BooleanField(_("beautician"), default=False)
    hairdresser = models.BooleanField(_("hairdresser"), default=False)
    occupational_therapy = models.BooleanField(
        _("occupational therapist"), default=False)
    physiotherapy = models.BooleanField(
        _("physiotherapy"), default=False)
    social_work = models.BooleanField(
        _("social work"), default=False)
    library = models.BooleanField(_("library"), default=False)
    church = models.BooleanField(_("church"), default=False)
    synagogue = models.BooleanField(_("synagogue"), default=False)
    mosque = models.BooleanField(_("mosque"), default=False)
    temple = models.BooleanField(_("temple"), default=False)
    gym = models.BooleanField(_("gym"), default=False)
    speech_therapy = models.BooleanField(
        _("speech therapy"), default=False)
    nursing_care = models.BooleanField(
        _("nursing care"), default=False)
    audiology = models.BooleanField(_("audiology"), default=False)
    optometry = models.BooleanField(_("optometry"), default=False)
    nearest_chc = models.CharField(_("nearest community health centre"), 
        max_length=200, blank=True)
    nearest_secondary_hospital = models.CharField(
        _("nearest secondary hospital"), max_length=200, blank=True)
    nearest_tertiary_hospital = models.CharField(
        _("nearest tertiary hospital"), max_length=200, blank=True)
    nearest_private_hospital = models.CharField(
        _("nearest private hospital"), max_length=200, blank=True)
    pharmacy_on_site = models.BooleanField(_("pharmacy on site"), 
        default=False)
    nearest_pharmacy = models.CharField(_("nearest pharmacy"),
        max_length=200, blank=True)
    care_plans = models.BooleanField(_("individual care plans offered"),
        default=False)
    security = models.TextField(_("description of security"), 
        blank=True)
    visiting_hours = models.TextField(_("visiting hours"), blank=True)
    volunteer_program = models.TextField(
        _("description of volunteer programs"), blank=True)
    additional_features = models.TextField(_("additional features"), 
        blank=True)    
    notes = models.TextField(_("notes"), blank=True)
    resident_committee = models.TextField(_("resident committee"), 
        blank=True)
    management_commitee = models.TextField(_("management committee"), 
        blank=True)
    trustees = models.TextField(_("trustees"), blank=True)    
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)    

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("facility")
        verbose_name_plural = _("facilities")
        ordering = ["name"]

class FacilityActivity(models.Model):
    facility = models.ForeignKey(Facility, verbose_name=_("facility"))
    activity = models.ForeignKey(Activity, 
        verbose_name=_('activity'))

    def __unicode__(self):
        return ' '.join([unicode(self.facility), 
            unicode(self.activity)])

    class Meta:
        verbose_name = _("facility activity")
        verbose_name_plural = _("facility activities")
        ordering = ["facility", "activity",]


class NumberOfRooms(models.Model):
    facility = models.ForeignKey(Facility, verbose_name=_("facility"))
    room_type = models.ForeignKey(Room, verbose_name=_("room type"))
    number = models.IntegerField(_("number of this room"))

    def __unicode__(self):
        return ' '.join([unicode(self.facility), 
            unicode(self.room_type), unicode(self.number)])

    class Meta:
        verbose_name = _("number of rooms")
        verbose_name_plural = _("numbers of rooms")
        ordering = ["facility", "room_type", "number",]


class NumberHealthCarers(models.Model):
    facility = models.ForeignKey(Facility, verbose_name=_("facility"))
    health_carer = models.ForeignKey(HealthCarer, 
        verbose_name=_("health carer"))
    number = models.IntegerField(_("number of this health carer"))

    def __unicode__(self):
        return ' '.join([unicode(self.facility), 
            unicode(self.health_carer), unicode(self.number)])

    class Meta:
        verbose_name = _("number health carers")
        verbose_name_plural = _("numbers of health carers")
        ordering = ["facility", "health_carer", "number",]


class PriceCategory(models.Model):
    name = models.CharField(_("name"), max_length=200)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("price category")
        verbose_name_plural = _("price categories")
        ordering = ["name",]
    
    
class FacilityPrice(models.Model):
    facility = models.ForeignKey(Facility, verbose_name=_("facility"))
    price_category = models.ForeignKey(PriceCategory, 
        verbose_name=_("cost category"))
    from_amount = models.DecimalField(_("from amount"), max_digits=8, 
        decimal_places=2)
    to_amount = models.DecimalField(_("to amount"), max_digits=8, 
        decimal_places=2)
    prices_updated = models.DateField(
        _("date that prices were last updated"), auto_now=True)

    def __unicode__(self):
        return ' '.join([unicode(self.facility), 
            unicode(self.price_category), unicode(self.from_amount),
            unicode(self.to_amount)])

    class Meta:
        verbose_name = _("facility price")
        verbose_name_plural = _("facility prices")
        ordering = ["facility","from_amount", "to_amount",]


class Image(models.Model):
    facility = models.ForeignKey(Facility, verbose_name = _("facility"))
    photo = models.ImageField(upload_to='uploads/images/')
    caption = models.CharField(_("caption"), max_length=200, blank=True)
    date_taken = models.DateField(_("date taken"), blank=True, null=True)
    photographer = models.CharField(_("photographer"), max_length=200, 
        blank=True)

    def __unicode__(self):
        return ' '.join([unicode(self.facility), self.caption])

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")
        ordering = ["facility","date_taken",]


class DocumentCategory(models.Model):
    name = models.CharField(_("name"), max_length=200)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("document category")
        verbose_name_plural = _("document categories")
        ordering = ["name",]

class Document(models.Model):
    facility = models.ForeignKey(Facility, verbose_name = _("facility"))
    document_category = models.ForeignKey(DocumentCategory, 
        verbose_name = _("document category"))
    file_name = models.FileField(_("file"), 
        upload_to='uploads/documents/', blank=True, null=True,
        help_text=_("Either upload the file or provide a URL to it."))
    url = models.URLField(_("URL"), blank=True, verify_exists=False)
    date_published = models.DateField(_("date published"), blank=True,
        null=True)
    period_begin = models.DateField(_("start date of period covered"),
        blank=True, null=True)
    period_end = models.DateField(_("end date of period covered"),
        blank=True, null=True)

    def __unicode__(self):
        return u' '.join([unicode(self.facility), 
            unicode(self.document_category), unicode(self.date_published)])

    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")
        ordering = ["facility", "document_category","date_published",
            "period_begin", "period_end", ]
