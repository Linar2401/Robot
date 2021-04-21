from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from time import sleep
from rest_framework import viewsets
from django.http import HttpResponse

# Create your views here.
import asyncio

from rest_framework.response import Response

from controller.models import RobotStatus
from controller.serializers import StatusSerializer


def controller(request):
    return render(request, 'main.html')


class StatusView(viewsets.ModelViewSet):
    queryset = RobotStatus.objects.latest("time")
    serializer_class = StatusSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(RobotStatus.objects.latest("time"), many=False)
        return Response(serializer.data)


