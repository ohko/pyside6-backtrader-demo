import sqlite3
import os


class DB():
    def __init__(self):
        super(DB, self).__init__()

        self.db = sqlite3.connect('db.db')
        if os.path.exists('db.db') == False:
            c = self.db.cursor()
            c.execute('''
            CREATE TABLE strategy(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100),
                content TEXT
            );
            ''')
            c.execute("INSERT INTO strategy VALUES(NULL,'test','print(123)')")
            self.db.commit()

    def list(self) -> list[dict]:
        c = self.db.cursor()
        rows = c.execute("SELECT * FROM strategy")
        rtn = []
        for row in rows:
            rtn.append({"id": row[0], "name": row[1], "content": row[2]})
        return rtn

    def save(self, id: int, name: str, content: str):
        c = self.db.cursor()
        if id:
            c.execute("UPDATE strategy SET name=?, content=? WHERE id=?",
                      (name, content, id,))
        else:
            c.execute("INSERT INTO strategy VALUES(NULL,?,?)",
                      (name, content,))
        self.db.commit()

    def remove(self, id):
        c = self.db.cursor()
        c.execute("DELETE FROM strategy WHERE id=?", (id,))
        self.db.commit()

    def close(self):
        self.db.close()
