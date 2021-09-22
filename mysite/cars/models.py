from django.db import models


class Car(models.Model):
	subheading=models.CharField(max_length=255,verbose_name='subheading')
	model_for_car=models.CharField(max_length=255,verbose_name='Model for car')
	image=models.ImageField(upload_to="images/", verbose_name='image')
	mileage = models.CharField(max_length=255,verbose_name='Mileage')
	transmission=models.CharField(max_length=255,verbose_name='Transmission')
	fuel=models.CharField(max_length=255,verbose_name='Fuel')
	seats=models.CharField(max_length=255,verbose_name='Seats')
	luggage=models.CharField(max_length=255,verbose_name='Luggage')
	airconditions=models.BooleanField(verbose_name='airconditions')
	child_seat=models.BooleanField(verbose_name='child seat')
	GPS=models.BooleanField(verbose_name='GPS')
	music=models.BooleanField(verbose_name='music')
	seat_belt=models.BooleanField(verbose_name='seat belt')
	sleeping_bed=models.BooleanField(verbose_name='sleeping bed')
	water=models.BooleanField(verbose_name='water')
	bluetooth=models.BooleanField(verbose_name='bluetooth')
	onboard_computer=models.BooleanField(verbose_name='onboard computer')
	audio_input=models.BooleanField(verbose_name='audio input')
	long_term_tripl=models.BooleanField(verbose_name='long term tripl')
	car_kit=models.BooleanField(verbose_name='car kit')
	remote_central_locking=models.BooleanField(verbose_name='remote central locking')
	climate_control=models.BooleanField(verbose_name='climate control')
	description=models.TextField(verbose_name='description',null=True)
	cost_hour=models.CharField(max_length=255,verbose_name='cost_hour')
	cost_day=models.CharField(max_length=255,verbose_name='cost_day')
	cost_mounth=models.CharField(max_length=255,verbose_name='cost_mounth')
	
	def __str__(self):

		return self.model_for_car

	def get_absolute_url(self):

		return reverse('post',kwargs={'post_id':self.pk})

class Happy_clients(models.Model):
	name=models.CharField(max_length=100,verbose_name='name')
	email = models.EmailField(unique=True)
	profession=models.CharField(max_length=100,verbose_name='profession')
	date=models.DateTimeField(verbose_name='date',auto_now=False, auto_now_add=False)
	body=models.CharField(max_length=255,verbose_name='massage')	

	def __str__(self):

		return self.name