from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests


# Create your views here.
def send_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None

def update_data(data):
    films = data['films']
    vehicles = data['vehicles']
    starships = data['starships']

    new_films = list()
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])

    new_vehicles = list()
    for vehicle in vehicles:
        vehicle = send_req(vehicle)
        new_vehicles.append(vehicle['name'])

    new_starships = list()
    for starship in starships:
        starship = send_req(starship)
        new_starships.append(starship['name'])

    data['films'] = new_films
    data['vehicles'] = new_vehicles
    data['starships'] = new_starships

    return data

def get_luke_info(request):
    data = send_req('https://swapi.dev/api/people/1/')

    if data:
        updated_data = update_data(data)

        return render(request, 'peple/person.html', updated_data)
    return HttpResponse('не удалось')

def update_data_for_starhip(data):
    films = data['films']
    pilots = data['pilots']

    new_films = list()
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])

    new_pilots = list()
    for pilot in pilots:
        pilot_data = send_req(pilot)
        new_pilots.append((pilot_data['name'], pilot_data['gender']))


    data['films'] = new_films
    data['pilots'] = new_pilots

    return data

def get_X_wing(request):
    data = send_req('https://swapi.dev/api/starships/12/')
    if data:
        updated_data = update_data_for_starhip(data)

        return render(request, 'peple/starship_1.html', updated_data)
    return HttpResponse('не удалось')

def get_Imperial_shuttle(request):
    data = send_req('https://swapi.dev/api/starships/22/')
    if data:
        updated_data = update_data_for_starhip(data)

        return render(request, 'peple/starship_2.html', updated_data)
    return HttpResponse('не удалось')

def get_Slave_1(request):
    data = send_req('https://swapi.dev/api/starships/21/')
    if data:
        updated_data = update_data_for_starhip(data)

        return render(request, 'peple/starship_2.html', updated_data)
    return HttpResponse('не удалось')