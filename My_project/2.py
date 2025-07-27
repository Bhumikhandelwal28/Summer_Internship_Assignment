import sqlite3
import hashlib

class UserSystem:
    def __init__(self, db_name="user_system.db"):   #constructor
        self.db_name = db_name
        self.create_user_table()

    def create_user_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                is_logged_in INT DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register_user(self):
        username = input("Enter the username:\n")
        password = input("Enter the password:\n")
        confirm_password = input("Enter the confirm password:\n")

        if password != confirm_password:
            print("Passwords do not match.")
            return

        hashed_password = system.hash_password(password)

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists.")
        finally:
            conn.close()

    def login_user(self):
        username = input("Enter the username:\n")
        password = input("Enter the password:\n")
        hashed_password = self.hash_password(password)

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if not result:
            print("User not found.")
        elif result[0] != hashed_password:
            print("Incorrect password.")
        elif result[1] == 1:
            print("User already logged in.")
        else:
            cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
            conn.commit()
            print("Login successful.")
        conn.close()

    def logout_user(self):
        username = input("Enter the username:\n")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if not result:
            print("User not found.")
        elif result[0] == 0:
            print("User is not logged in.")
        else:
            cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
            conn.commit()
            print("Logout successful.")
        conn.close()

    def change_password(self):
        username = input("Enter the username:\n")
        current_password = input("Enter current password:\n")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if not result:
            print("User not found.")
        elif self.hash_password(current_password) != result[0]:
            print("Incorrect current password.")
        elif result[1] == 0:
            print("User must be logged in to change password.")
        else:
            new_password = input("Enter new password:\n")
            confirm_password = input("Confirm new password:\n")
            if new_password != confirm_password:
                print("Passwords do not match.")
            else:
                new_hashed = self.hash_password(new_password)
                cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed, username))
                conn.commit()
                print("Password changed successfully.")
        conn.close()

    def menu(self):
        while True:
            print("\n---MENU---")
            print("1. Register")
            print("2. Login")
            print("3. Logout")
            print("4. Change Password")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                self.logout_user()
            elif choice == '4':
                self.change_password()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    system = UserSystem()   #object creation
    system.menu()
