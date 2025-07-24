import sqlite3
import hashlib


def user_register():
    conn=sqlite3.connect('user_system.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        is_logged_in INT DEFAULT 0)
        '''
    )
    conn.commit()
    conn.close()


def hash_password(password):
    """Hashes the password using SHA-256."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def register_user():
     conn=sqlite3.connect("user_system.db")
     cursor=conn.cursor()
     username=input("Enter the username:\n")
     password=input("Enter the password:\n")
     confirm_password=input("Enter the confirm password\n")
     if password!=confirm_password:
         print("Enter correct confirm password\n")
         return
     hashed_password=hash_password(password)

     try:
         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
         conn.commit()
         print("User registered successfully.")
     except sqlite3.IntegrityError:
         print("Username already exists. Please choose another.")
     finally:
         conn.close()


def login_user():
    user_name=input("Enter the username:")
    password = input("Enter the password:")
    hashed_password = hash_password(password)
    conn = sqlite3.connect("user_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password,is_logged_in FROM users WHERE username = ?", (user_name,))
    result = cursor.fetchone()


    if not result:
        print("User not found.")
        return

    if result[0] != hashed_password:
        print("Incorrect password.")
        return

    if result[1] == 1:
        print("User is already logged in.")
        return

    cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (user_name,))
    conn.commit()
    conn.close()
    print("Login successful!")


def logout():
    user_name=input("Enter the username:")
    conn = sqlite3.connect("user_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (user_name,))
    user = cursor.fetchone()

    if not user:
        print("User is not found")
        return

    if user[0]==0:
        print("User is not logged in.")
        return

    cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (user_name,))
    conn.commit()
    conn.close()
    print("Logout successfully!")

def pass_change():
    user_name=input("Enter the username:")
    current_password=input("enter the current password:")
    hash_pass=hash_password(current_password)
    conn = sqlite3.connect("user_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password,is_logged_in FROM users WHERE username = ?", (user_name,))
    output = cursor.fetchone()
    if not output:
        print("User not found")
        return
    if output[0]!=hash_pass:
        print("Incorrect current password")
        return
    if output[1]==0:
        print("User must logged In to change password")
        return

    new_password = input("Enter the new password:")
    confirm_password =input("Enter the confirm password:")
    if new_password!=confirm_password:
        print("New_password and confirm password are not same.")
        return

    new_hashed=hash_password(new_password)
    cursor.execute("UPDATE users SET password=? WHERE username=?",(new_hashed,user_name))
    conn.commit()
    conn.close()
    print("Password Changed Successfully")

def menu():
    while True:
        print("---MENU DRIVEN INTERFACE---\n")
        print("1.REGISTER\n")
        print("2.LOGIN\n")
        print("3.LOGOUT\n")
        print("4.PASSWORD CHANGE\n")
        print("5.EXIT\n")
        ch=int(input("SELECT THE OPTION FROM (1-5)\n"))

        if ch==1:
            register_user()
        elif ch==2:
            login_user()
        elif ch==3:
            logout()
        elif ch==4:
            pass_change()
        elif ch==5:
            print("Exit")
            break
        else:
            print("Invalid choice.Please try again\n")


if __name__ == "__main__":
    user_register()
    menu()





