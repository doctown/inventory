from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<p>In index view</p>')

def item_details(request, id):
    return HttpResponse('<p>In item_detail view with id {0}'.format(id))