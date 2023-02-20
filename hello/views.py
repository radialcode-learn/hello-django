import re
from django.shortcuts import render
from django.utils.timezone import datetime
from hello.models import LogMessage

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LogMessageSerializer
from rest_framework import status

print("http://127.0.0.1:5000/hello/VSCode")

# Create your views here.


# def home(request):
#     return render(request, "hello/home.html")


@api_view(["GET", "POST"])
def home_list_view(request):
    """
    Get All available logs
    """
    if request.method == "GET":
        logs = LogMessage.objects.all()
        serializer = LogMessageSerializer(logs, many=True)
        return Response(
            {"success": True, "data": serializer.data, "message": "Success."}
        )

    if request.method == "POST":
        data = request.data
        data["log_date"] = datetime.now()
        serializer = LogMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "message": "Log create successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
