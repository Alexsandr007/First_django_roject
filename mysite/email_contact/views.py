from django.shortcuts import render,redirect
from email_contact.tasks import send_message
# Create your views here.
def contact_page(request):
	return render(request,'post/contact.html')



def send(request):
	print(request.POST['cart_model'])
	if request.method == 'POST':
		objects = request.POST
		send_message.delay(objects['email'],objects['message'],objects['subject'],objects['name'],objects['cart_model'])
	return redirect('contact:contact')