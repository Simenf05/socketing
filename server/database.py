
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
        self.cursor.execute("SELECT * FROM colr")
        self.colors = self.cursor.fetchall()
        
        
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
    
    def new_coords(self, x: int, y: int, map: str):
        self.cursor.execute("SELECT * FROM coords")
        coords_table = self.cursor.fetchall()
        
        for col in coords_table:
            row = (col[1], col[2], col[3])
            
            if row == (x, y, map):
                coords_id = col[0]
                break
        else:
            sql = "INSERT INTO coords (x, y, map) VALUES (%s, %s, %s)"
            val = (x, y, map)
            
            self.cursor.execute(sql, val)
            self.db.commit()
            
            coords_id = self.cursor.lastrowid
        return coords_id
    
    def create_user(self, name: str, password: str, x: int, y: int, map: str, color: str):
        
        player = self.get_user_by_name_and_pass(name, password)
        
        if not player:
            
            
            
            for item in self.colors:
                if item[1].split(".")[0] in [color, color.capitalize()]:
                    color_id = item[0]
                    break
            else:
                color_id = 1
            
            print(color)
            print(color_id)
            
            coords_id = self.new_coords(x, y, map)
            
            sql = "INSERT INTO player (player_name, player_password, coords_coords_id, colr_colr_id) VALUES (%s, %s, %s, %s)"
            val = (name, password, coords_id, color_id)
            
            self.cursor.execute(sql, val)
            
            self.db.commit()
            
            player = self.get_user_by_name_and_pass(name, password)
            return player
        else:
            return player
        
    def save_user(self, id: int, x: int, y: int, map: str):
        
        coords_id = self.new_coords(x, y, map)
        
        sql = "UPDATE player SET coords_coords_id=%s WHERE idPlayer = %s"
        val = (coords_id, id)
        
        self.cursor.execute(sql, val)
        self.db.commit()
        
    def get_user_by_name_and_pass(self, name, password):
        
        sql = "SELECT * FROM player WHERE player_name=%s AND player_password=%s"
        val = (name, password)
        
        self.cursor.execute(sql, val)
        players = self.cursor.fetchall()        
        
        return players
        
        



"""
game_info = Database("localhost", "server", "123123", "game_info")



game_info.create_user("joon", "jegerkul", 100, 300, "map1", "green")



"""