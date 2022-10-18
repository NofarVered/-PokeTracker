from msilib.schema import Error
from signal import raise_signal
import string
from time import process_time_ns
from typing import List
from .my_sql_auth import my_sql_auth
import pymysql as mysql


class my_sql_proxy:
    def __init__(self, auth: my_sql_auth):
        try:
            self.connection = mysql.connect(
                host=auth.host,
                user=auth.user,
                password=auth.password,
                db=auth.db,
                charset=auth.charset,
                cursorclass=auth.cursorclass)
        except Error as e:
            raise e

    def execute_query(self, sql_query: string, params: List):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params)
                self.connection.close()
        except Error as e:
            raise e
