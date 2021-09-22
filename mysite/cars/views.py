from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
  object_list = Car.objects.all()
  paginator = Paginator(object_list, 3)
  page_number = request.GET.get('page')
  page_obj=paginator.get_page(page_number)

  return render(request,'post/car.html',{'page_obj': page_obj,'paginator': paginator})

def car_single_page(request,post_id):
  cat_posts=Car.objects.order_by()[:3]
  posts=Car.objects.get(pk=post_id)

  return render(request,'post/car-single.html', {'posts':posts,'cat_posts':cat_posts})