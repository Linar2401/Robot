import datetime

from django.db import models


class Position(models.Model):
    OPEN = 'OP'
    LOAD = "L"
    OCCUPIED = 'OC'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (LOAD, 'on load'),
        (OCCUPIED, 'occupied'),
    )
    name = models.CharField(max_length=50, default='Position')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=OPEN)
    time_info_updated = models.DateTimeField(default=datetime.datetime.now())


class Package(models.Model):
    OPEN = 'O'
    TRANSIT = "T"
    IN_STOCK = 'IS'
    ON_ISSUE = 'OS'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (TRANSIT, 'In transit'),
        (IN_STOCK, 'In stock'),
        (ON_ISSUE, 'On issue'),
    )

    name = models.CharField(max_length=50, default='Package')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=OPEN)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    time_arrived = models.DateTimeField(default=datetime.datetime.now())
    time_of_departure = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    additional_info = models.TextField(blank=True)


class RobotStatus(models.Model):
    AWAIT_PACKAGE = 'A'
    MOVING = "M"
    IN_STOCK = 'IS'
    ON_BASE = "OB"
    STATUS_CHOICES = (
        (AWAIT_PACKAGE, 'Await package'),
        (MOVING, 'Moving'),
        (IN_STOCK, 'In stock'),
        (ON_BASE, 'On base')
    )

    time = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=AWAIT_PACKAGE)

    def __str__(self):
        return str(self.status)
