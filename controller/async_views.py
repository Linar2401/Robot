import asyncio

from asgiref.sync import sync_to_async
from django.shortcuts import redirect
from controller.models import *
import serial

from controller.qr_reader import qr_recognize

ser = serial.Serial('/dev/ttyACM0', 115200)


async def commandGetPackage(request):
    if request.method == "POST":
        loop = asyncio.get_event_loop()
        data = request.POST.get("packages_select_command")
        loop.create_task(get_package(data))
        return redirect("http://127.0.0.1:8000/")


async def get_package(package):
    package = await sync_to_async(Package.objects.filter(id=package).first, thread_sensitive=True)()
    pos = await sync_to_async(Position.objects.filter(package=package).first, thread_sensitive=True)()
    ser.flush()
    data = 1000 + pos.position_number
    write(data)
    data = read()
    if data == 0:
        status = RobotStatus(status=RobotStatus.MOVING)
        await sync_to_async(status.save, thread_sensitive=True)()
        data = read()
        if data == 1:
            await sync_to_async(RobotStatus.objects.create, thread_sensitive=True)(status=RobotStatus.IN_STOCK)
            pos.status = Position.LOAD
            pos.time_info_updated = datetime.datetime.now()
            await sync_to_async(pos.save, thread_sensitive=True)()
            data = read()
            if data == 2:
                await sync_to_async(RobotStatus.objects.create, thread_sensitive=True)(status=RobotStatus.IN_STOCK)
                pos.status = Position.OPEN
                pos.time_info_updated = datetime.datetime.now()
                await sync_to_async(pos.save, thread_sensitive=True)()
                package.status = Package.TRANSIT
                await sync_to_async(package.save, thread_sensitive=True)()
                data = read()
                if data == 3:
                    await sync_to_async(RobotStatus.objects.create, thread_sensitive=True)(status=RobotStatus.MOVING)
                    package.status = Package.ON_ISSUE
                    await sync_to_async(package.save, thread_sensitive=True)()
                    if data == 4:
                        await sync_to_async(RobotStatus.objects.create, thread_sensitive=True)(
                            status=RobotStatus.AWAIT_PACKAGE)
                        package.status = Package.GONE
                        await sync_to_async(package.save, thread_sensitive=True)()


async def commandPullPackage(request):
    if request.method == "POST":
        loop = asyncio.get_event_loop()
        data = request.POST.get("packages_select_command")
        loop.create_task(pull_package(data))
        return redirect("http://127.0.0.1:8000/")


async def pull_package(package):
    for i in range(10):
        print(i, package)
        await asyncio.sleep(2)


def read():
    line = ser.readline()
    return int(line)


def write(data):
    output_str = str(data) + "\n"
    ser.write(output_str.encode("utf-8"))
