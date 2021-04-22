import datetime

from django.db import models


class Position(models.Model):
    OPEN = 'OP'
    LOAD = "L"
    OCCUPIED = 'OC'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (LOAD, 'On load'),
        (OCCUPIED, 'Occupied'),
    )
    P1 = 'P1'
    P2 = "P2"
    P3 = 'P3'
    P4 = 'P4'
    P5 = 'P5'
    POSITION_CHOICES = (
        (P1, 'Position #1'),
        (P2, 'Position #2'),
        (P3, 'Position #3'),
        (P4, 'Position #4'),
        (P5, 'Position #5'),
    )
    position_number = models.CharField(max_length=4, choices=POSITION_CHOICES, default=P1, unique=True)
    name = models.CharField(max_length=50, default='Position')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=OPEN)
    time_info_updated = models.DateTimeField(default=datetime.datetime.now())

    def get_time_diff(self):
        naive = self.time_info_updated.replace(tzinfo=None)
        current = datetime.datetime.now()
        current.replace(tzinfo=None)
        dif = current - naive
        # return str(dif.seconds)
        if dif.days > 0:
            return "More than 24 hours ago"
        elif int(dif.seconds/3600) > 2:
            return "A few hours ago"
        elif int(dif.seconds/3600) > 0:
            return "More than hour ago"
        elif dif.seconds > 60:
            return str(int(dif.seconds/60)) + " minutes ago"
        else:
            return "Less than a minute ago"

    def __str__(self):
        return self.position_number


class Package(models.Model):
    OPEN = 'O'
    TRANSIT = "T"
    IN_STOCK = 'IS'
    ON_ISSUE = 'OS'
    GONE = "G"
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (TRANSIT, 'In transit'),
        (IN_STOCK, 'In stock'),
        (ON_ISSUE, 'On issue'),
        (GONE, 'Is gone'),
    )

    name = models.CharField(max_length=50, default='Package')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=OPEN)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    time_arrived = models.DateTimeField(default=datetime.datetime.now())
    time_of_departure = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    additional_info = models.TextField(blank=True, max_length=1000)

    def __str__(self):
        return self.name


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
