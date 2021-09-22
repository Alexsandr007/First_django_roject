from mysite.celery import app
from .service import send
from email_contact.views import *

@app.task
def send_message(user_email,text,subject,name, cart_model):
	model_car='Model of car: '+ cart_model
	name='name: '+name
	time='time: '+subject
	if cart_model=='buibvbgfi':
		massage=name+'\n'+time+'\n'+text
	else:
		massage=model_car+'\n'+name+'\n'+time+'\n'+text
	send(user_email,massage) 