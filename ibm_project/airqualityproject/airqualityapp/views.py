from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np
import json
import urllib.request
# Create your views here.
def home(request):
    return render(request,"home.html")

def Air(request):
    return render(request,"Air.html")

def Airout(request):
    rf_random = joblib.load('AQI.sav')
    lis = []

    lis.append(request.POST.get('pm25'))
    lis.append(request.POST.get('pm10'))
    lis.append(request.POST.get('no'))
    lis.append(request.POST.get('no2'))
    lis.append(request.POST.get('nox'))
    lis.append(request.POST.get('nh3'))
    lis.append(request.POST.get('co'))
    lis.append(request.POST.get('so2'))
    lis.append(request.POST.get('tol'))

    #v = np.array(lis, dtype=int)
    #val = [int(i) for i in v]
    answer = rf_random.predict([lis])[0]
    #answer = np.array(answer,dtype=int)

    if answer <=50:
        ans = "good"
    elif answer>50 and answer <=100:
        ans = "moderate"
    elif answer>100 and answer <=150:
        ans = "satisfactory"
    elif answer>150 and answer <=200:
        ans = "poor"
    elif answer>200 and answer <=300:
        ans = "very poor"
    elif answer>300 and answer <=400:
        ans = "severe"
    else:
        ans = "Hazardous"

    return render(request,"Air.html",{'aqiq':ans,'aqi':answer})

def weather(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a0a23c127804518f75e75713d0ddb52c').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),
            
            "temp": str(list_of_data['main']['temp'])+ ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request,"weather.html", data)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
