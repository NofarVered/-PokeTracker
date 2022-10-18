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
                host=auth.host[0],
                user=auth.user[0],
                password=auth.password[0],
                db=auth.db[0],
                charset=auth.charset[0],
                cursorclass=mysql.cursors.DictCursor
            )
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def execute_insert_query(self, sql_query: string, params: List):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, params)
                self.connection.commit()
        except Exception as e:
            print("Exeception occured:{}".format(e))
