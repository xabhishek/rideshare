__author__ = 'geofjacoby'

import psycopg2

class Repository:


    __host = None
    __port = None
    __database = None
    __username = None
    __password = None

    def __init__(self, host, port, database, user, password):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__username = user
        self.__password = password


    def _get_connection(self):
        dsn = str.format("dbname={0} user={1} password={2} host={3} port={4}", self.__database, self.__username, self.__password, self.__host, self.__port)
        conn = psycopg2.connect(dsn)
        return conn