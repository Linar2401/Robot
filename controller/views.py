from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
        packages = {}
        for pos in Position.objects.all():
            times[pos.id] = pos.get_time_diff()
            packages[pos.id] = pos.get_package()
        context['times'] = times
        context['packages'] = packages
        context['status'] = RobotStatus.objects.latest("time")
        return context


class StatusView(viewsets.ModelViewSet):
    queryset = RobotStatus.objects.latest("time")
    serializer_class = StatusSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(RobotStatus.objects.latest("time"), many=False)
        return Response(serializer.data)


class PackageView(TemplateView):
    template_name = "package_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['package'] = get_object_or_404(Package, position=self.kwargs.get('pos_id'))
        return context


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PackageViewJSON(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageByPosView(viewsets.ModelViewSet):
    serializer_class = PackageSerializer

    # def list(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(
    #         Package.objects.filter(position=self.kwargs.get('pos_id')))
    #     return Response(serializer.data)

    def get_queryset(self):
        queryset = Package.objects.filter(position_id=self.kwargs["pos_id"])
        return queryset

