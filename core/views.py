from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
from django.conf import settings
import os
from .models import Edata
from rest_framework.response import Response
from .Serilizaer import DataSerializer


def index(request):
    return HttpResponse("Hello World ! ")


@api_view(('GET',))
def getData(request):
    Book = Edata.objects.all()
    serializer = DataSerializer(Book, many=True)
    return Response(serializer.data)


@api_view(('GET',))

def specificData(request,slug):
    key = slug.split('=')[0]
    print(key)
    if(key == 'end_year'):
        dataa = Edata.objects.filter(end_year=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'intensity'):
        dataa = Edata.objects.filter(intensity=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'sector'):
        dataa = Edata.objects.filter(sector=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'topic'):
        dataa = Edata.objects.filter(topic=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'region'):
        dataa = Edata.objects.filter(region=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'pestle'):
        dataa = Edata.objects.filter(pestle=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif(key == 'source'):
        dataa = Edata.objects.filter(source=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif key == 'country':
        dataa = Edata.objects.filter(country=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)
    elif key == 'insight':
        dataa = Edata.objects.filter(insight=slug.split('=')[1])
        serializer = DataSerializer(dataa,many=True)
        return  Response(serializer.data)

    else:
        return  HttpResponse('this si new world ')