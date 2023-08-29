from django.db import models

# import the date time package as you have used attribute below
from datetime import time

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    """"
    adding a start time and duration attributes to our Meeting class
    We added default time as we created two meetings using the admin interface
    Because we have previously created date before creating the below two new attributes,
    we have to provide default attributes - of 9 o'clock for time and 1hr for duration
    """
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    """
    To add a room for my meeting, add a new attribute called room with a foreign key 
    Foreign key adds a relation between the meeting class to the room class 
    Foreign key is a concept from sql 
    On delete means: shows what happens when a room is removed from the database 
    Cascade means: if room is deleted, all meetings from that room si removed 
    In django, if we use a foreign key, we must specify the on delete behaviour
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

# Add string representation to our class
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

# Create a model class called Room to represent meeting room
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} : room {self.room_number} on floor {self.floor}"
