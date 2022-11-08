# from cgitb import reset
# from msilib.schema import Error
# from signal import raise_signal
import string
# from time import process_time_ns
from typing import List
from .my_sql_auth import my_sql_auth
import pymysql as mysql


class my_sql_proxy:  ## TDOD : camel case

    def __init__(self, auth: my_sql_auth):
        try:
            self.connection = mysql.connect(
                host=auth.host[0],
                user=auth.user[0],
                password=auth.password[0],
                db=auth.db[0],
                charset=auth.charset[0],
                cursorclass=mysql.cursors.DictCursor
            )
        except Exception as e:
            print(e)

    def execute_insert_query(self, sql_query: string, params: List):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params)
                self.connection.commit()
        except Exception as e:
            print(e)
            raise e

    def execute_select_all_query(self, sql_query: string, params: List):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            result = [obj for obj in cursor.fetchall()]
            return result

    def execute_select_one_query(self, sql_query: string, params: List = None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    sql_query, params) if params else cursor.execute(sql_query)
                result = cursor.fetchone()
                return result
        except Exception as e:
            return e




AUTH = my_sql_auth()

CONNECTOR = None
if CONNECTOR is None:
    CONNECTOR = my_sql_proxy(AUTH)

