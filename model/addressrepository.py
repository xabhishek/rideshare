__author__ = 'geofjacoby'

import psycopg2
from repository import Repository
from address import Address

class AddressRepository(Repository):

    __insert_sql = """insert into address(streetname, city, state, country, zipcode, location)
                        VALUES('%s', '%s', '%s', '%s', '%s', ST_GeomFromText('POINT('%d','%d')')    """

    __update_sql = """update address
                    set streetname = '%s',
                    city = '%s',
                    state = '%s',
                    country = '%s',
                    zipcode = '%s',
                    location = ST_GeomFromText('POINT('%d','%d')')
                    where addressid = %d"""

    __select_sql = """select *, ST_AsGeoJSON(location) as location_json where addressid = %s"""

    __host = None
    __port = None
    __database = None
    __username = None
    __password = None

    def __init__(self, host, port, database, user, password):
        Repository.__init__(self, host, port, database, user, password)

    def create(self, address):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__insert_sql, [address.street_name, address.city, address.state, address.country,
                                                     address.zipcode, address.longitude, address.latitude])

    def update(self, address):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__update_sql, [address.street_name, address.city, address.state, address.country,
                                                     address.zipcode, address.longitude, address.latitude, address.address_id])

    def get_by_id(self, address_id):
        address = None
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(self.__select_sql.format(address_id))
                records = cur.fetchone()
                address = Address(records)
        return address