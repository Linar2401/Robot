from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from time import sleep
from rest_framework import viewsets
from django.views.generic import *
from django.http import HttpResponse

# Create your views here.
import asyncio

from rest_framework.response import Response

from controller.models import *
from controller.serializers import *


class Controller(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = Position.objects.all()
        times = {}
        for pos in Position.objects.all():
            times[pos.id] = pos.get_time_diff()
        context['times'] = times
        return context


class StatusView(viewsets.ModelViewSet):
    queryset = RobotStatus.objects.latest("time")
    serializer_class = StatusSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(RobotStatus.objects.latest("time"), many=False)
        return Response(serializer.data)


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
