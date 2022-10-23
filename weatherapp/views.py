from django.shortcuts import render
# json is used to filter out data thats been sent through the api
import json  
import urllib.request

# Create your views here.
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def index (request):
    if request.method == 'POST':
        city = request.POST['city']
        rest = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(rest)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon'])+''+ str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "description": str(json_data['weather'][0]['description']),
            
        }
    else:
        city = 'Nakuru'
        rest = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3b638fccef8920c0bf1356f12e48be34').read()
        json_data = json.loads(rest)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon'])+''+ str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "description": str(json_data['weather'][0]['description']),
        }
    return render (request, "index.html", {'city': city, 'data':data})