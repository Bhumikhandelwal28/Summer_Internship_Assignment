import sqlite3
import hashlib

# --- S: Single Responsibility Principle ---
class DBManager:
    def __init__(self, db_name="user_system.db"):
        self.db_name = db_name
        self.create_user_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_user_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    is_logged_in INTEGER DEFAULT 0
                )
            ''')
            conn.commit()


# Separated Utility Class
class PasswordHasher:
    @staticmethod
    def hash(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


#User-specific Operations
class UserService:
    def __init__(self, db_manager: DBManager, hasher: PasswordHasher):
        self.db = db_manager
        self.hasher = hasher

    def register(self, username, password, confirm_password):
        if password != confirm_password:
            return "Passwords do not match."

        hashed = self.hasher.hash(password)

        try:
            with self.db.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
                conn.commit()
                return "User registered successfully."
        except sqlite3.IntegrityError:
            return "Username already exists."

    def login(self, username, password):
        hashed = self.hasher.hash(password)

        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if not result:
                return "User not found."
            elif result[0] != hashed:
                return "Incorrect password."
            elif result[1] == 1:
                return "User already logged in."
            else:
                cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
                conn.commit()
                return "Login successful."

    def logout(self, username):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if not result:
                return "User not found."
            elif result[0] == 0:
                return "User is not logged in."
            else:
                cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
                conn.commit()
                return "Logout successful."

    def change_password(self, username, current_password, new_password, confirm_new_password):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if not result:
                return "User not found."
            elif self.hasher.hash(current_password) != result[0]:
                return "Incorrect current password."
            elif result[1] == 0:
                return "User must be logged in to change password."
            elif new_password != confirm_new_password:
                return "New passwords do not match."
            else:
                new_hashed = self.hasher.hash(new_password)
                cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed, username))
                conn.commit()
                return "Password changed successfully."


#Interface Segregation/Dependency Injection via Composition ---
class UserInterface:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Register")
            print("2. Login")
            print("3. Logout")
            print("4. Change Password")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                u = input("Username: ")
                p = input("Password: ")
                c = input("Confirm Password: ")
                print(self.user_service.register(u, p, c))

            elif choice == '2':
                u = input("Username: ")
                p = input("Password: ")
                print(self.user_service.login(u, p))

            elif choice == '3':
                u = input("Username: ")
                print(self.user_service.logout(u))

            elif choice == '4':
                u = input("Username: ")
                cp = input("Current Password: ")
                np = input("New Password: ")
                cnp = input("Confirm New Password: ")
                print(self.user_service.change_password(u, cp, np, cnp))

            elif choice == '5':
                print("Exiting system.")
                break

            else:
                print("Invalid choice.")


#Main Function
if __name__ == "__main__":
    db = DBManager()
    hasher = PasswordHasher()
    service = UserService(db, hasher)
    ui = UserInterface(service)
    ui.menu()
