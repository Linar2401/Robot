from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from time import sleep

from django.http import HttpResponse

# Create your views here.
import asyncio


def controller(request):
    return render(request, 'main.html')





# helpers
async def http_call_async():
    for num in range(1, 60):
        await asyncio.sleep(1)
        print(num)



# views
async def index(request):
    return HttpResponse("Hello, async Django!")


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
