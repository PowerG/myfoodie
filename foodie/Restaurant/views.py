from django.db.models import Q
from django.shortcuts import render_to_response
from Restaurant.models import *
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context

def search(request):
	query_browse = request.GET.get('b')
	query_in1 = request.GET.get('q')
	query_in = str(query_in1)
	query_input = query_in.strip()
	query_cusine=request.GET.get('c')
	query_location=request.GET.get('l')
	query_delivery = request.GET.get('d')
	query_pickup = request.GET.get('p')

	restaurant = Restaurant.objects.filter().distinct()
	location = Location.objects.filter().distinct()
	cuisine = Cuisine.objects.filter().distinct()
	#results=Restaurant.objects.filter().distinct()
	results=Menu_Item.objects.filter().distinct()

	if query_input:
		
		qset=(Q(i_name__icontains=query_input))
		results= results.filter(qset).distinct()

	if query_cusine:
		qset_one=(Q(i_cuisine__c_name__icontains=query_cusine))
		results= results.filter(qset_one).distinct()

	if query_location:
		qset_two=(Q(i_restaurant__r_location__l_name__icontains=query_location))
		results= results.filter(qset_two).distinct()

	if query_delivery:
		qset_two=(Q(i_restaurant__r_delivery=query_delivery))
		results= results.filter(qset_two).distinct()

	if query_pickup:
		qset_two=(Q(i_restaurant__r_pickup=query_pickup))
		results= results.filter(qset_two).distinct()

	if not (query_input or query_cusine or query_location or query_delivery or query_pickup):
		results=[]


	return render_to_response("search3.html",
	{"results": results,
	"query_browse": query_browse,
	 "query": query_input,
	 
	'restaurant': restaurant,
	'cuisine': cuisine,
	 'location': location})
def index(request):
    
   	query_browse = request.GET.get('b')
	query_in1 = request.GET.get('q')
	query_in = str(query_in1)
	query_input = query_in.strip()
	query_cusine=request.GET.get('c')
	query_location=request.GET.get('l')
	query_delivery = request.GET.get('d')
	query_pickup = request.GET.get('p')

	restaurant = Restaurant.objects.filter().distinct()
	location = Location.objects.filter().distinct()
	cuisine = Cuisine.objects.filter().distinct()
	#results=Restaurant.objects.filter().distinct()
	results=Menu_Item.objects.filter().distinct()

	if query_input:
		
		qset=(Q(i_name__icontains=query_input))
		results= results.filter(qset).distinct()

	if query_cusine:
		qset_one=(Q(i_cuisine__c_name__icontains=query_cusine))
		results= results.filter(qset_one).distinct()

	if query_location:
		qset_two=(Q(i_restaurant__r_location__l_name__icontains=query_location))
		results= results.filter(qset_two).distinct()

	if query_delivery:
		qset_two=(Q(i_restaurant__r_delivery=query_delivery))
		results= results.filter(qset_two).distinct()

	if query_pickup:
		qset_two=(Q(i_restaurant__r_pickup=query_pickup))
		results= results.filter(qset_two).distinct()

	if not (query_input or query_cusine or query_location or query_delivery or query_pickup):
		results=[]


	return render_to_response("index3.html",
	{"results": results,
	"query_browse": query_browse,
	 "query": query_input,
	 
	'restaurant': restaurant,
	'cuisine': cuisine,
	 'location': location})

def item(request):


	return render_to_response("item.html",
	{
	 
	'restaurant': restaurant,
	'cuisine': cuisine,
	 'location': location})
