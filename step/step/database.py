import sqlite3
import datetime
import os



class Database:
    def __init__(self, path=""):
        db_file = path + "/data.db"
        print(os.path.abspath(db_file))
        if not os.path.exists(db_file):
            with open(db_file, "w") as f:
                f.write("")

        self.conn = sqlite3.connect(db_file)  
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS data  
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                        name TEXT,  
                        world TEXT,
                        x INTEGER, 
                        y INTEGER,
                        z INTEGER,
                        time REAL,
                        state INTEGER,
                        msg TEXT,
                        type TEXT)''') 

    def add(self, name, world, x, y, z,type, msg=""):
        x = int(x)
        y = int(y) 
        z = int(z)
           
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        state = 1
           
        self.cur.execute("INSERT INTO data(name, world, x, y, z, time, state, type, msg ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )",  
                     (name, world, x, y, z, current_time, state, type ,msg))
        self.conn.commit()
           
        return self.cur.lastrowid
    
    def search(self, world, x, y, z, states=1, range=300): 
        query = "SELECT * FROM data WHERE world = ? AND x BETWEEN ? AND ? AND y BETWEEN ? AND ? AND z BETWEEN ? AND ? AND state = ? GROUP BY id"
        params = (world, x-range, x+range, y-range, y+range, z-range, z+range, states)
        self.cur.execute(query, params)  
           
        rows = self.cur.fetchall()
        data = []    
        for row in rows:
            data.append({'id':row[0], 'name':row[1], 'x':row[3], 'y':row[4], 'z':row[5], 'states':row[7], 'time':row[6], 'msg': row[8],'type':row[9]})
        return data

    def search_type(self, type):
        self.cur.execute("SELECT * FROM data WHERE type=?", (type,))
       
        rows = self.cur.fetchall()
        data = []   
        for row in rows:
             data.append({'id':row[0], 'name':row[1], 'x':row[3], 'y':row[4], 'z':row[5], 'states':row[7], 'time':row[6], 'msg': row[8],'type':row[9]})
        return data
    
    def list_loc(self):
        self.cur.execute("SELECT * FROM data WHERE type=?", (-1,))
        
        rows = self.cur.fetchall()
        data = []
        for row in rows:
             data.append({'id':row[0], 'name':row[1], 'x':row[3], 'y':row[4], 'z':row[5], 'states':row[7], 'time':row[6], 'msg': row[8],'type':row[9]})
        return data

    def delete(self, id):
        query = "DELETE FROM data WHERE id =?"
        params = (id,)  
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur.rowcount > 0
    
    def change_state(self, id, state):
        query = "UPDATE data SET state = ? WHERE id = ?"
        params = (state, id)  
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur.rowcount > 0
    
    def exit(self):
        self.conn.close()