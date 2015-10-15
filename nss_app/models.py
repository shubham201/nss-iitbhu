from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Volunteer(models.Model):
	#volunteer_id = models.CharField(max_length=120,blank=True, null=True)
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	joining_date = models.DateField()
	contact = models.IntegerField()
	email = models.EmailField(blank=True, verbose_name='e-mail')
	working_hrs = models.IntegerField(null=True)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Volunteer, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Village(models.Model):
	name = models.CharField(max_length=20)
	adoption_date = models.DateField()
	family_count = models.IntegerField()
	block = models.CharField(max_length=30)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Village, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Camp(models.Model):
	village = models.ForeignKey(Village)
	camp_type = models.CharField(max_length=20, null=True)
	date = models.DateField()
	strt_time = models.TimeField()
	end_time = models.TimeField()
	organising_cost = models.IntegerField()
	details = models.TextField(max_length=200)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.camp_type)
	    super(Camp, self).save(*args, **kwargs)

	def __str__(self):
		return u'%s' % (self.camp_type)
	class Meta:
		ordering = ['camp_type']

class Family(models.Model):
	village = models.ForeignKey(Village)
	head_name = models.CharField(max_length=20, null=True)
	address = models.CharField(max_length=100)
	income = models.IntegerField()
	members_count = models.IntegerField()
	prob_list = models.TextField(max_length=200)
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.head_name)
	    super(Family, self).save(*args, **kwargs)

	def __str__(self):
		return self.address
	class Meta:
		ordering = ['head_name']

class Fund(models.Model):
	source = models.CharField(max_length=30)
	receiving_date = models.DateField()
	amount = models.IntegerField()
	net_bal = models.IntegerField()
	slug = models.SlugField(default='',unique=True)

	def save(self, *args, **kwargs):
	    self.slug = slugify(self.source)
	    super(Fund, self).save(*args, **kwargs)

	def __str__(self):
		return self.source
	class Meta:
		ordering = ['source']

