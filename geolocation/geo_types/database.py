import sqlite3


class Database:
    def __init__(self, db_name: str):
        self._db_connection = sqlite3.connect(db_name)
        self._cursor = self._db_connection.cursor()
        self._data_list = list()

    def get_data_list(self, table_name: str):
        for row in self._cursor.execute("""SELECT * FROM {}""".format(table_name)):
            self._data_list.append(row)

        return self._data_list
