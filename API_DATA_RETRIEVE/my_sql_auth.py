from typing import Optional
import pymysql as mysql


DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_PWD = ""


class my_sql_auth:
    def __init__(self, user: str = DEFAULT_USER, pwd: str = DEFAULT_PWD, host: Optional[str] = DEFAULT_HOST):
        self.host = host,
        self.user = user,
        self.password = pwd,
        self.db = "sql_poketracker",
        self.charset = "utf8",
        self.cursorclass = mysql.cursors.DictCursor
