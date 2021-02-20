import yaml
import psycopg2
import psycopg2.extras
import os.path
import json
from datetime import date


def date_normalizer(values):
    for value in values:
        for k, v in value.items():
            if isinstance(v, date):
                value[k] = str(date)
    return values


class SqlConnector:

    def __init__(self):
        self.conf_file = '/../configurations.yaml'
        with open(os.path.dirname(__file__) + self.conf_file, 'r') as f:
            doc = yaml.safe_load(f)
        self.connection = psycopg2.connect(host=doc['sql_connection']['host'],
                                           database=doc['sql_connection']['database'],
                                           user=doc['sql_connection']['user'],
                                           password=doc['sql_connection']['password'])
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def update_data(self, values, table_name, conditions=[]):
        # Creating string to update a value
        query = 'UPDATE ' + table_name
        query += ' SET '
        for k, v in values.items():
            if isinstance(v, str):
                query += str(k) + '=' + '\'' + v + '\','
            else:
                query += str(k) + '=' + str(v) + ','
        query = query[:-1] + ' WHERE ' + ' AND '.join(conditions) if len(conditions) > 0 else ''
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, values, table_name, returning=False, returning_field=None):
        # Creating string to insert values
        query = "INSERT INTO " + table_name + ' ('
        query += ', '.join(values.keys())
        query += ') VALUES ('
        for v in values.values():
            if isinstance(v, str):
                query += '\'' + str(v) + '\'' + ', '
            else:
                query += str(v) + ', '
        query = query[:-2] + ')'
        if returning:
            query += ' RETURNING ' + returning_field
            self.cursor.execute(query)
            returning_value = self.cursor.fetchone()[returning_field]
            self.connection.commit()
            return returning_value
        self.cursor.execute(query)
        self.connection.commit()

    def get_data(self, columns, table_name, conditions=[]):
        query = 'SELECT '
        query += ', '.join(columns)
        query += ' FROM ' + table_name
        where = ' WHERE ' + ' AND '.join(conditions) if len(conditions) > 0 else ''
        query += where
        self.cursor.execute(query)
        ans = json.dumps(date_normalizer(self.cursor.fetchall()))
        return json.loads(ans)

    def get_query(self, query):
        self.cursor.execute(query)
        ans = json.dumps(date_normalizer(self.cursor.fetchall()))
        return json.loads(ans)

    def insert_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def update_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
