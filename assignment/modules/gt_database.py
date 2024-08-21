import mysql.connector
from modules.db import DB_Info

class GT_Database:
    def Connect(self):
        self.connection = mysql.connector.connect(user=DB_Info.db_user, password=DB_Info.db_password, host=DB_Info.db_host, database=DB_Info.db_database)
        self.cursor = self.connection.cursor()

    def Disconnect(self):
        self.cursor.close()