
import mysql.connector


class Database:
    
    def __init__(self, host: str, user: str, password: str, database: str, dbName: str | None=None) -> None:
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        if dbName:
            self.dbName = dbName
        else: 
            self.dbName = "mydb"
        
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        self.cursor = self.db.cursor()
        
        
    def executeSQL(self, sql: str):
        self.cursor.execute(sql) 
        
    def insertToDB(self, INTO: str, values: tuple): 
        
        sql = f"INSERT INTO {INTO} VALUES {values}"
        self.executeSQL(sql)
        self.db.commit()
    
    
    def deleteFromDB(self, FROM: str | None = None, WHERE: str | None = None):
        
        sql = f"DELETE FROM {FROM} WHERE {WHERE}"
        self.executeSQL(sql)
        self.db.commit()
    
        
    def getFromDB(self, FROM: str, selection: str, WHERE: str | None = None):
        
        sql = f"SELECT {selection} FROM {FROM}"
        if WHERE:
            sql += f" WHERE {WHERE}"
        self.executeSQL(sql)
        return self.cursor.fetchall()
        
    
    
        


game_info = Database("localhost", "server", "123123", "game_info")

into = "player (player_name, player_password)"
values = tuple("arvid", "1223")

game_info.insertToDB(into, values)
