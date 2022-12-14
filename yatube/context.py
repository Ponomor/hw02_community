from django.shortcuts import render
import datetime as dt
def year(request):
    today = dt.datetime.now().year
    return  {'today': today}