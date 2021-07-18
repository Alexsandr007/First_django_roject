from django.shortcuts import render, redirect
from cars.models import *
from blog.models import *
from django.core.paginator import Paginator





def home_page(request):
	object_list = Car.objects.all()
	paginator = Paginator(object_list, 4)
	page_number = request.GET.get('page')
	page_obj=paginator.get_page(page_number)
	object_list_clients = Happy_clients.objects.all()
	# cat_blogs=Blog.objects.order_by()[3:]
	cat_blogs=Post.published.order_by('-pk')[:3]
	context={
	'cat_blogs':cat_blogs,
	'page_obj':page_obj,
	'object_list':object_list,
	'object_list_clients':object_list_clients
	}
	return render(request,'post/index.html',context)

def about_page(request):
	object_list_clients = Happy_clients.objects.all()
	context={
	'object_list_clients':object_list_clients
	}
	return render(request,'post/about.html',context)

def services_page(request):
	return render(request,'post/services.html')

def pricing_page(request):
	object_list = Car.objects.all()
	paginator = Paginator(object_list, 6) # По 3 статьи на каждой странице.
	page_number = request.GET.get('page')
	page_obj=paginator.get_page(page_number)
	return render(request,'post/pricing.html',{'page_obj': page_obj,
    'object_list': object_list,})


def contact_page_post(request,post_id):
	posts=Car.objects.get(pk=post_id)
	return render(request,'post/contact_post.html',{'posts':posts})