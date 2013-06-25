from django.db import models
from django.contrib import admin

class Location(models.Model):
	l_name = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.l_name
	pass

class Cuisine(models.Model):
	c_name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.c_name
	pass
class Restaurant(models.Model):
	r_name = models.CharField(max_length = 30)
	r_location =models.ForeignKey(Location)
	r_delivery = models.BooleanField()
	r_pickup = models.BooleanField()
	r_detail = models.CharField(max_length = 500)
	r_image = models.CharField(max_length=200)
	r_rating = models.IntegerField(default=0)
	r_tel = models.CharField(max_length=30)
	r_email = models.CharField(max_length=100)
	r_website = models.CharField(max_length=200)
	r_entry_date = models.DateField()

	def __unicode__(self):
		return self.r_name
	pass
class Menu_Item(models.Model):
	i_name = models.CharField(max_length=30)
	i_price = models.IntegerField(default=0)
	i_cuisine = models.ForeignKey(Cuisine)
	i_restaurant = models.ForeignKey(Restaurant)
	i_detail = models.CharField(max_length=200)
	i_image = models.CharField(max_length=200) 
	def __unicode__(self):
		return self.i_name
	pass





admin.site.register(Location)
admin.site.register(Cuisine)
admin.site.register(Menu_Item)
admin.site.register(Restaurant)
