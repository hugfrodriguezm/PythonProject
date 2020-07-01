import sqlite3
#Class to connect with DataBase

class sqlite:
    
    def __init__(self):
        self.__DataBase="CitiesDataBase"
    
    #Functions

    #Function to create a table if is not created yet
    
    def IFCreateTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.__DataBase)
            cursor = sqliteConnection.cursor()
            Result=cursor.execute("""CREATE TABLE IF NOT EXISTS TimeProcessingTable (
	                                TimeID INTEGER PRIMARY KEY AUTOINCREMENT,
   	                                SumTime TEXT,
	                                MeanTime TEXT,
	                                MinTime TEXT,
	                                MaxTime TEXT	  	
                                    );""")
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to create table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
    
    # Function to insert a instance in the Table

    def InsertFromTable(self,SumTime,MeanTime,MinTime,MaxTime):
        try:
            sqliteConnection = sqlite3.connect(self.__DataBase)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO TimeProcessingTable
                              (SumTime,MeanTime,MinTime,MaxTime)
                              VALUES (?, ?, ?, ?);"""

            data_tuple = (SumTime,MeanTime,MinTime,MaxTime)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")