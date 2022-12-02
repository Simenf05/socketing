
import mysql.connector
from typing import Any

class Database:
    """Creates object that connects and executes SQL to the MYSQL database."""
    
    def __init__(self, host: str, user: str, password: str, database: str, dbName: str="mydb") -> None:
        """Makes the connection and the cursor.

        Args:
            host (str): Host to connect to.
            user (str): The user to connect with.
            password (str): Password for the user.
            database (str): The database to connect to.
            dbName (str, optional): Optional name for the database connection. Defaults to mydb.
        """
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.dbName = dbName
        
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        self.cursor = self.db.cursor()
        
        
    def executeSQL(self, sql: str) -> None:
        """Executes SQL code to the database.
        
        Note: this does not commit changes to the database.

        Args:
            sql (str): The code that will be executed.
        """
        self.cursor.execute(sql) 
        
    def insertToDB(self, INTO: str, values: tuple) -> None:
        """Inserts values to the database.

        Args:
            INTO (str): SQL code that specifies where to insert.
            values (tuple): Tuples containing the values to insert.
        """
        
        sql = f"INSERT INTO {INTO} VALUES {values}"
        self.executeSQL(sql)
        self.db.commit()
    
    
    def deleteFromDB(self, FROM: str, WHERE: str) -> None:
        """Deletes elements from the database.

        Args:
            FROM (str): SQL code that specifies the database to delete from.
            WHERE (str): SQL code that specifies what to delete.
        """
        
        sql = f"DELETE FROM {FROM} WHERE {WHERE}"
        self.executeSQL(sql)
        self.db.commit()
    
        
    def getFromDB(self, FROM: str, selection: str, WHERE: str | None = None) -> list:        
        """Gets information from the database.

        Args:
            FROM (str): SQL code that specifies where to get from.
            selection (str): SQL code that specifies what to get.
            WHERE (str | None, optional): Optional SQL for the WHERE conditon. Defaults to None.

        Returns:
            list: List of the matching data.
        """
        
        sql = f"SELECT {selection} FROM {FROM}"
        if WHERE:
            sql += f" WHERE {WHERE}"
        self.executeSQL(sql)
        return self.cursor.fetchall()
        
    
    
        
"""

game_info = Database("localhost", "server", "123123", "game_info")

into = "player (player_name, player_password)"
values = tuple(["arvid", "1223"])

game_info.insertToDB(into, values)

noe = game_info.getFromDB("player", "*")

print(type(noe))
"""