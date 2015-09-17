from django.db import models

# Create your models here.
class Volunteer(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	joining_date = models.DateField()
	contact = models.IntegerField()
	working_hrs = models.IntegerField()
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Village(models.Model):
	name = models.CharField(max_length=20)
	adoption_date = models.DateField()
	family_count = models.IntegerField()
	block = models.CharField(max_length=30)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Camp(models.Model):
	village = models.ForeignKey(Village)
	camp_type = models.CharField(max_length=20)
	date = models.DateField()
	str_time = models.TimeField()
	end_time = models.TimeField()
	organising_cost = models.IntegerField()
	details = models.TextField(max_length=200)
	def __unicode__(self):
		return u'%s' % (self.camp_type)
	class Meta:
		ordering = ['camp_type']

class Family(models.Model):
	village = models.ForeignKey(Village)
	head_name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	income = models.IntegerField()
	members_count = models.IntegerField()
	prob_list = models.TextField(max_length=200)
	def __unicode__(self):
		return self.address
	class Meta:
		ordering = ['head_name']

class Fund(models.Model):
	source = models.CharField(max_length=30)
	receiving_date = models.DateField()
	amount = models.IntegerField()
	net_bal = models.IntegerField()
	def __unicode__(self):
		return self.source
	class Meta:
		ordering = ['source']