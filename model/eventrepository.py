__author__ = 'gjacoby'

import psycopg2
import psycopg2.extras
import geojson
from event import Event
from address import Address
from repository import Repository
from addressrepository import AddressRepository

class EventRepository(Repository):

    __insert_sql = """insert into event (eventname, addressid, startdate, enddate, description) VALUES (%s, %s, %s, %s, %s)"""
    __select_by_id_sql = "select *, ST_AsGeoJSON(a.location) as location_json from event e join address a on e.addressid = a.addressid where eventid = %s"

    __select_by_name_sql = "select *, ST_AsGeoJSON(a.location) as location_json from event e join address a on e.addressid = a.addressid where eventname = %s"
    __select_with_people_and_location_sql = """select * from event e
                                            join address a
                                                on a.address_id = e.address_id
                                            join eventdriver ed
                                                on ed.event_id = e.event_id
                                            join user ud
                                                on ed.driver_id = ud.user_id
                                            join event_passenger ep
                                                on e.event_id = ep.event_id
                                            join user up
                                                on ep.passenger_id = up.user_id
                                            where e.event_id = %s"""

    __update_sql = """update event
                    set name = %s ,
                    addressid = %s ,
                    startdate = %s ,
                    enddate = %s ,
                    description = %s
                    where event_id = %s"""

    __delete_sql = """delete from event where event_id = %s"""

    __address_repo = None


    def __init__(self, host, port, database, user, password):
        Repository.__init__(self, host, port, database, user, password)
        self.__address_repo = AddressRepository(host, port, database, user, password)
    def save(self, event):
        if event.event_id is None:
            self.create(event)
        else:
            self.update(event)

    def create(self, event):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__insert_sql, [event.event_name, event.address.addressid, event.start_date, event.end_date, event.description])
                #TODO: persist address, drivers and passengers
                #TODO: wrap in transaction
                if not event.address.address_id is None:
                    self.__address_repo.create(event.address)
                if not event.drivers is None or event.drivers.len() > 0:
                    #persist driver associations
                    pass


    def update(self, event):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__update_sql, [event.name, event.address.addressid, event.start_date, event.end_date, event.description])
                 #TODO: persist address, drivers and passengers
                #TODO: wrap in transaction
                if not event.address.address_id is None:
                    self.__address_repo.update(event.address)
                if not event.drivers is None or event.drivers.len() > 0:
                    #persist driver associations
                    pass
                if not event.passengers is None or event.passengers.len() > 0:
                    #persist passenger associations
                    pass

    def get_by_id(self, event_id):
            conn = None
            cur = None
            event = None
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute(self.__select_by_id_sql, [event_id])
                    records = cur.fetchone()
                    if records is not None and records["eventid"] is not None:
                        event = Event(records)
                        if records.get("addressid") is not None:
                                address = Address(records)
                                event.address = address
            return event

    def get_by_name(self, event_name):
        conn = None
        cur = None
        event = None

        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__select_by_name_sql, [event_name])
                records = cur.fetchone()
                if records is not None and records["eventid"] is not None:
                    event = Event(records)
                    if records.get("addressid") is not None:
                            address = Address(records)
                            event.address = address
        return event

    def delete(self, event_id):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__delete_sql, [event_id])









