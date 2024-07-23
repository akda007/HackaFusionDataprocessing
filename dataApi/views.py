import json
from rest_framework.decorators import api_view
from rest_framework import status
from dataApi.data_processing.dataprocess import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(["POST"])
def generate_chart_instructor(req, id = None):

    chart_data = dataprocess_instructor(req.body, id)

    return Response(chart_data, status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def generate_chart_student(req):

    chart_data = dataprocess_student(req.body)

    return Response(chart_data, status.HTTP_200_OK)