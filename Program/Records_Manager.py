from PyQt5 import QtSql

class RecordManager:
    def __init__(self):
        self.n_records = 0

    def load_records(self):
        global connr
        connr = QtSql.QSqlDatabase.addDatabase('QSQLITE', "con2")
        connr.setDatabaseName("source/record.db")
        connr.open()
        global cQuery
        cQuery = QtSql.QSqlQuery(connr)
        cQuery.exec(
            """
            CREATE TABLE record(
                w_time TEXT,
                w_distance REAL
            )
            """
        )
        #print("ready to record")

    def load_database(self):
        pass
        # загрузка из базы данных, которая лежит в папке source