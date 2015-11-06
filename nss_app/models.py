from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Volunteer(models.Model):
	#volunteer_id = models.CharField(max_length=120,blank=True, null=True)
	name = models.CharField(max_length=20,blank=False) #required. By default its False
	address = models.CharField(max_length=100,blank=True)
	joining_date = models.DateField(blank=True)
	contact = models.CharField(max_length=20,blank=False)
	#contact = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=False) # validators should be a list.... #required
	email = models.EmailField(blank=False, verbose_name='e-mail') #required
	#working_hrs = models.IntegerField(null=True,blank=True)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name) + slugify(self.contact)
		super(Volunteer, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		unique_together = (('name','contact'),)

class Village(models.Model):
	name = models.CharField(max_length=20,blank=False) #required
	adoption_date = models.DateField(blank=True)
	family_count = models.IntegerField(blank=True)
	block = models.CharField(max_length=30,blank=False) #required
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name) + slugify(self.block)
	    super(Village, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		unique_together = (('name','block'),)

class Camp(models.Model):
	village = models.ForeignKey(Village)
	camp_type = models.CharField(max_length=20, blank=False) #required
	date = models.DateField(blank=False) #required
	strt_time = models.TimeField(blank=True)
	end_time = models.TimeField(blank=True)
	organising_cost = models.IntegerField(blank=True)
	details = models.TextField(max_length=200,blank=True)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.camp_type) + '-' + slugify(self.date)
	    super(Camp, self).save(*args, **kwargs)

	def __str__(self):
		return u'%s' % (self.camp_type)
	class Meta:
		ordering = ['camp_type']
		unique_together = (('camp_type','date'),)

class Family(models.Model):
	village = models.ForeignKey(Village)
	head_name = models.CharField(max_length=20, blank=False) #required
	#father_name = models.CharField(max_length=20, blank=False) #required
	address = models.CharField(max_length=100, blank=False) #required
	income = models.IntegerField(blank=True)
	members_count = models.IntegerField(blank=False) #required
	prob_list = models.TextField(max_length=200,blank=True)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.head_name) + slugify(self.members_count)
	    super(Family, self).save(*args, **kwargs)

	def __str__(self):
		return self.address
	class Meta:
		ordering = ['head_name']
		unique_together = (('head_name','members_count'),)

class Fund(models.Model):
	source = models.CharField(max_length=30,blank=False) #required
	receiving_date = models.DateField(blank=False) #required
	amount = models.IntegerField(blank=False) #required
	net_bal = models.IntegerField(blank=False, default=0) #required, initialise it to zero(0)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.source) + slugify(self.amount)
	    super(Fund, self).save(*args, **kwargs)

	def __str__(self):
		return self.source
	class Meta:
		ordering = ['source']
		unique_together = (('source','receiving_date'),)

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	#picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username

