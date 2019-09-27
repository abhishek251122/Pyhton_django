from django.http import HttpResponse
from django.shortcuts import render
import requests


def conver(input_value,home_value):
    print(input_value)
    home_EUR = (1 / float(list(input_value.values())[0])) * home_value
    EUR_Tgt = round(float(list(input_value.values())[1]) * home_EUR,2)

    return EUR_Tgt

def home(request):
    url = "http://data.fixer.io/api/latest?access_key=7af141a2533086ee4c870f193464d7a0"
    r = requests.get(url).json()

    home_currency = list(r['rates'])

    return render(request, 'home.html',{'home_currency': home_currency})

def main(request):
    home_txt = request.GET['Home_Currency']
    tgt_txt = request.GET['Target_Currency']
    home_value = float(request.GET['fname'])
    url = "http://data.fixer.io/api/latest?access_key=ef22b7bae94e03147c0ab8c84b6365f5&symbols={0},{1}".format(home_txt,tgt_txt)
    rw = requests.get(url).json()

    input_p = dict(rw['rates'])

    tgt_value = conver(input_p,home_value)

    return render(request, 'home.html',{'output_value': tgt_value})