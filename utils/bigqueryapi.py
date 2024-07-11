# -*- coding: utf-8 -*-
import json
import numpy as np
import pandas as pd

from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from pytz import timezone, utc
from dateutil import tz

class BigQueryAPI:

    project: str
    service_account: str
    max_row: int = 20000

    def __init__(self, service_account='/root/credentials/samsung-poc.json'):
        self.project = None
        self.prop = None
        self._service_account = service_account
        self._client = bigquery.Client.from_service_account_json( self._service_account)

    def query(self, query):
        print(query)

        job_config = bigquery.QueryJobConfig()
        job_config.use_legacy_sql = False
        query_job = self._client.query(query, job_config=job_config)
        print(query_job)

        return query_job.to_dataframe()

    def update(self, query, params):
        print(query)
        records = params['record']
        print(records)

        query_params = [
            bigquery.ScalarQueryParameter("patno", "STRING", params['patno']),
            bigquery.ScalarQueryParameter("regtime", "DATETIME", params['regtime']),
            #{'itemCode': '8,2', 'itemName': 'Border', 'parentCode': '2,18', 'itemType': 'Border', 'itemValue': '0', 'itemPos': '8,2', 'itemMerge': '45,4', 'itemLevel': '2', 'itemCheck': None, 'itemColor': None}
            bigquery.ArrayQueryParameter("record", 
                "STRUCT<itemCode STRING, itemName STRING, parentCode STRING, itemType STRING, itemValue STRING, itemPos STRING, itemMerge STRING, itemLevel INTEGER, itemCheck INTEGER, itemColor STRING>", 
                records
            )
        ]

        job_config = bigquery.QueryJobConfig()
        job_config.query_parameters = query_params
        job_config.use_legacy_sql = False
        query_job = self._client.query(query, job_config=job_config)
        print(query_job)

    def insert(self, table_id, rows):
        insert_rows = []
        for index, row in enumerate(rows):
            # print(row)
            if row: insert_rows.append(row)
            if len(insert_rows) >= self.max_row:
                errors = self._client.insert_rows(table_id, insert_rows)
                print('Write rows', len(insert_rows), errors)
                insert_rows = []

        if len(insert_rows) > 0:
            errors = self._client.insert_rows(table_id, insert_rows)
            print('Write rows', len(insert_rows), errors)

    def insert_rows_json(self, table_id, rows_to_insert):
        errors = self._client.insert_rows_json(table_id, rows_to_insert)

        if errors == []:
            print('Inserted json data')
        else:
            print(f'Error: {errors}')

    def load_json_schema(self, file_name):
        with open(file_name) as f:
            cols = json.load(f)
            return cols

        return None

    def load_schema(self, file_name):

        def make_schema(cols):
            description = None

            print(cols, type(cols))
            if isinstance(cols, dict):
                schemafield = None

                try:
                    mode = cols['mode']
                    description = cols['description']
                    sub_cols = cols['fields']
                    schemas = make_schema(sub_cols)
                    schemafield = bigquery.SchemaField(cols['name'], cols['type'], mode, description, schemas)
                except KeyError as e:
                    print('KeyError', e)
                    if 'fields' in str(e):
                        schemafield = bigquery.SchemaField(cols['name'], cols['type'], cols['mode'], description)
                    elif 'description' in str(e):
                        try:
                            sub_cols = col['fields']
                            schemas = make_schema(sub_cols)
                            schemafield = bigquery.SchemaField(cols['name'], cols['type'], cols['mode'], None, schemas)
                        except KeyError as e:
                            schemafield = bigquery.SchemaField(cols['name'], cols['type'], cols['mode'])
                    elif 'mode' in str(e):
                        print("mode is not found")

                return schemafield

            schemafields = []
            for col in cols:
                try:
                    mode = col['mode']
                    description = col['description']
                    sub_cols = col['fields']
                    schemas = make_schema(sub_cols)
                    schemafields.append(
                        bigquery.SchemaField(col['name'], col['type'], mode, description, schemas))
                except KeyError as e:
                    #print('KeyError', e)
                    if 'fields' in str(e):
                        schemafield = bigquery.SchemaField(col['name'], col['type'], col['mode'], description)
                        #print('bigquery.SchemaField', schemafield)
                        schemafields.append(schemafield)
                    elif 'description' in str(e):
                        try:
                            sub_cols = col['fields']
                            schemas = make_schema(sub_cols)
                            schemafield = bigquery.SchemaField(col['name'], col['type'], col['mode'], None, schemas)
                            #print('bigquery.SchemaField', schemafield)
                            schemafields.append(schemafield)
                        except KeyError as e:
                            schemafield = bigquery.SchemaField(col['name'], col['type'], col['mode'])
                            #print('bigquery.SchemaField', schemafield)
                            schemafields.append(schemafield)
                    elif 'mode' in str(e):
                        print("mode is not found")
                #print('schemafields', schemafields)
            return schemafields

        with open(file_name) as f:
            cols = json.load(f)
            #print(type(cols))
            bigquerySchema = make_schema(cols)
            return bigquerySchema

        return None

if __name__ == '__main__':
    api = BigQueryAPI()
    api.load_config()
    user_events = api.run_user_events()
    print(user_events.project, user_events.dataset_id, user_events.table_id)
