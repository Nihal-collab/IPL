from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
def get_ipl(request):
    data=Ipl.objects.all()
    print(data)
    return Response('data')

@api_view(["POST"])
def post_ipl(request):
    Ipl.objects.create(team=request.data["team"],captain=request.data["captain"],cups=request.data["cups"])
    return Response("POST")

@api_view(["PUT"])
def put_ipl(request,id):
    data=Ipl.objects.get(id=id)
    data.team=request.data["team"]
    data.captain=request.data["captain"]
    data.cups=request.data["cups"]
    data.save()
    return Response("PUT")

@api_view(["DELETE"])
def delete_ipl(request,id):
    data=Ipl.objects.get(id=id)
    data.delete()
    return Response("DELETE")

@api_view(["GET"])
def get_student(request):
    data=list(Student.objects.values())
    return Response(data)

@api_view(["GET"])
def get_students(request,id):
    data=Student.objects.get(id=id)
    va = {
        "name": data.name,
        "age": data.age,
        "branch":data.branch
        # Add other fields manually
    }
    return JsonResponse(va)