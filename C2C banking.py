import mysql.connector

# Establish connection
connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')

# Close connection
connection.close()


# function that will connect the create account function to mysql. it takes in two parameters. 

def create_account(username, password):
    connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')
    cursor = connection.cursor()
    query = "INSERT INTO accounts (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    connection.commit()
    cursor.close()
    connection.close()

def validate_login(username, password):
    connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')
    cursor = connection.cursor()
    query = "SELECT balance FROM accounts WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def withdraw(username, amount):
    connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')
    cursor = connection.cursor()
    query = "UPDATE accounts SET balance = balance - %s WHERE username = %s"
    cursor.execute(query, (amount, username))
    connection.commit()
    cursor.close()
    connection.close()

def deposit(username, amount):
    connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')
    cursor = connection.cursor()
    query = "UPDATE accounts SET balance = balance + %s WHERE username = %s"
    cursor.execute(query, (amount, username))
    connection.commit()
    cursor.close()
    connection.close()

def delete_account(username):
    connection = mysql.connector.connect(user='root', database='c2c', password='Da11@s123')
    cursor = connection.cursor()
    query = "DELETE FROM accounts WHERE username = %s"
    cursor.execute(query, (username,))
    connection.commit()
    cursor.close()
    connection.close()

def login_BE():
    global login_attempts
    username = input("Username: ")
    password = input("Password: ")
    result = validate_login(username, password)
    if result:
        balance = result[0]  # Extract balance from the result
        print("Login successful!")
        print(f"Your current balance is: ${balance}")
        while True:  # Allow user to perform multiple operations until they choose to exit
            print(" ")
            print("1: Deposit")
            print("2: Withdraw")
            print("3: Balance")
            print("4: Close Account")
            print("5: Logout")

            choice = input("Enter choice: ")
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                deposit(username, amount)
                print("Deposit successful!")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(username, amount)
                print("Withdrawal successful!")
            elif choice == "3":
                print(f"Your current balance is: ${balance}")
            elif choice == "4":
                confirm = input("Are you sure you want to close your account? (yes/no): ")
                if confirm.lower() == "yes":
                    delete_account(username)
                    print("Account closed successfully!")
                    break  # Exit the loop after closing account
            elif choice == "5":
                print("Logout successful!")
                break  # Exit the loop and return to main menu
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    else:
        print("Username or password incorrect.")
        quit()

def create_account_BE():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    create_account(username, password)
    print("Account created successfully!")

def bank_list():
    print("Welcome to ___ Banks")
    print(" ")
    print("1. Login")
    print("2. Create account")

def select_choice():
    user_cInput = input("Enter: ")
    if user_cInput == "1":
        login_BE()
    elif user_cInput == "2":
        create_account_BE()

def main():
    bank_list()
    print(" ")
    select_choice()

if __name__ == "__main__":
    login_attempts = 0
    main()