import sqlite3


class Database:
    def __init__(self, database_name):
        self.db = sqlite3.connect(database_name)

    def authenticate(self, username, password):
        # Check if user exists
        self.db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return self.db.fetchone() is not None

    def register(self, username, password):
        # Check if user exists
        self.db.execute("SELECT * FROM users WHERE username = ?", (username,))
        if self.db.fetchone() is not None:
            return False

        # Insert user into database
        self.db.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        self.db.commit()
        return True

    def close(self):
        self.db.close()
