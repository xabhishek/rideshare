__author__ = 'gjacoby'

from user import User
from event import Event
from driver import Driver

class Passenger(User):
    requested_driver = None
    requested_event = None

    def __init__(self):
        pass

    def __init__(self, dict):
        requested_driver = dict["driver"]
        requested_event = dict["event"]

    def request_event(self, driver, event):
        requested_driver = driver
        requested_event = event