from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from app.get_bus_stations import get_bus_stations
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    list_of_stations = get_bus_stations('data-398-2018-08-30.csv')
    paginator = Paginator(list_of_stations, 10)
    current_page = request.GET.get('page', 1)
    next_page_url, previous_page_url = None, None
    posts = paginator.get_page(current_page)
    if posts.has_next():
        next_page = urlencode({'page': posts.next_page_number()})
        next_page_url = '?'.join((reverse('bus_stations'), next_page))
    if posts.has_previous():
        previous_page = urlencode({'page': posts.previous_page_number()})
        previous_page_url = '?'.join((reverse('bus_stations'), previous_page))
    return render_to_response('index.html', context={
        'bus_stations': posts,
        'current_page': current_page,
        'prev_page_url': previous_page_url,
        'next_page_url': next_page_url,
    })
