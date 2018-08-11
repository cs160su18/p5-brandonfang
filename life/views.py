from django.shortcuts import render
from django.core import serializers
from life.models import *

def groups(request):
  if request.method == "POST":
    print(json.loads(request.body))
    return HttpResponse("")
  else:
    all_groups = Group.objects.all()
    response = serialize("json", all_groups)
    return HttpResponse(response, content_type="application/json")
  
def lists(request):
  if request.method == "POST":
    print(json.loads(request.body))
    return HttpResponse("")
  else:
    all_lists = ShopList.objects.all()
    response = serialize("json", all_lists)
    return HttpResponse(response, content_type="application/json")

def index(request):
  all_lists = ShopList.objects.all()
  return render(request, 'life/index.html', {"all_lists": all_lists})

def login(request):
  all_groups = Group.objects.all()
  return render(request, 'life/login.html', {"groups": all_groups})
