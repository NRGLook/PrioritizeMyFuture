import sqlite3
from passlib.hash import pbkdf2_sha256

import var.Constants


class RegistrationPolicy:
    @staticmethod
    def registration(self, username, _password):

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')

        def verify_password(password, hashed):
            return pbkdf2_sha256.verify(password, hashed)

        c.execute('SELECT password FROM users WHERE username=?', (username,))
        result = c.fetchone()

        if result:
            # loop checking for correct password
            if verify_password(_password, result[0]):
                print('Authorization is success!')
                with open(f"{username}.json", "a") as tasks_file:
                    pass
                # user = RegisteredUser(username)
            else:
                print('Incorrect password! Try again!')
                exit()
        else:
            hashed_password = pbkdf2_sha256.hash(_password)
            c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed_password))
            with open(f"{username}.json", "a") as tasks_file:
                pass
            print('Registration is success!')
            # user = RegisteredUser(username)

        conn.commit()
        conn.close()
