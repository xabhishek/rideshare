__author__ = 'gjacoby'


class Event:
    event_id = None
    address = None
    event_name = None
    start_date = None
    end_date = None
    description = None
    drivers = []
    passengers = []

    def __init__(self):
        pass

    def __init__(self, dict):
        self.event_id = dict["eventid"]
        self.event_name = dict.get("eventname")
        self.address = dict.get("address")
        self.start_date = dict.get("startdate")
        self.end_date = dict.get("enddate")
        self.description = dict.get("description")
        self.drivers = dict.get("drivers")
        self.passengers = dict.get("passengers")


