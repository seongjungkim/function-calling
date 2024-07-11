# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import psycopg2.extensions
import decimal

class PostgresqlAPI:

    def __init__(self, host, port, user, password, dbname):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__dbname = dbname

        self.__conn = psycopg2.connect(host=self.__host,
            dbname=self.__dbname,
            user=self.__user,
            password=self.__password,
            port=self.__port)

    def close(self):
      self.__conn.close()

    def query_one(self, query):
        cursor = self.__conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()
        print(row)
        return row

    def query_all(self, query, params=None):
        cursor = self.__conn.cursor()
        if not params:
          cursor.execute(query)
        else:
          cursor.execute(query, params)

        row = cursor.fetchall()
        #print(row)
        return row

    def execute(self, query, data):
        cursor = self.__conn.cursor()

        cursor.execute(query, data)

        self.__conn.commit()
        
        row = None
        try:
            row = cursor.fetchone()
        except psycopg2.ProgrammingError as e:
            print(e)
        
        cursor.close()
        return row

    def execute_batch(self, query, data):
        cursor = self.__conn.cursor()

        try:
            extras.execute_batch(cursor, query, data)
            self.__conn.commit()
        except Exception as e:
            self.__conn.rollback()
        
        cursor.close()

    def update(self, query, params=None):
        cursor = self.__conn.cursor()
        if not params:
          cursor.execute(query)
        else:
          cursor.execute(query, params)

        self.__conn.commit()
        cursor.close()

    def updates(self, queries, params=[]):
        cursor = self.__conn.cursor()
        cursor.execute(queries, params)
        
        self.__conn.commit()
        cursor.close()
