from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.weathermap.org/data/2.5/weather?q='+city+'&appid=87a6e0f6fefa5125cce18519e5a0c79a').read()
        json_data = json.loads(res)
        data= {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['']['lat'])
        }
    else:
        ''
    return render(request, 'index.html', {'city' : city})
