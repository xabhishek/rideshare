__author__ = 'gjacoby'

from user import User
from event import Event
class Driver(User):
    events = []
    comment = None

    def __init__(self):
        pass

    def __init__(self, dict):
        events = dict["event"]
        comment = dict["comment"]

    def agree_to_drive(self, eventid, new_comment):
        new_event = Event()
        new_event.event_id = eventid
        comment = new_comment
        events.append(new_event)