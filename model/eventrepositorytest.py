from model import eventrepository

__author__ = 'gjacoby'


import unittest
from event import Event
from eventrepository import EventRepository

class EventRepositoryTest(unittest.TestCase):

    event_repository = None
    host = None
    port = None
    database = None
    user_name = None
    password = None

    def setUp(self):
        self.host = "centspark6675.cloudapp.net"
        self.port = "5432"
        self.database = "ridedata"
        self.user_name = "spark"
        
        self.event_repository = EventRepository(self.host, self.port, self.database, self.user_name, self.password)


    def test_connection(self):
        event = self.event_repository.get_by_id(42)

    def test_get_by_id(self):
        event = self.event_repository.get_by_id(1)
        self.assertIsNotNone(event)
        self.assertEqual(1, event.event_id)
        self.assertEqual("Hello world", event.description)
        self.assertEqual(50, event.address.latitude)

    def test_get_by_name(self):
        event = self.event_repository.get_by_name("Foo Name")
        self.assertIsNotNone(event)
        self.assertEqual(1, event.event_id)
        self.assertEqual("Foo Name", event.event_name)
        self.assertEqual("Hello world", event.description)
        self.assertEqual(50, event.address.latitude)

if __name__ == "__main__":
    unittest.main()