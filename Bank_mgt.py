import mysql.connector
import csv

# Function to read credentials from a CSV file
def read_credentials_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            return list(csv.DictReader(csvfile))
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Function to authenticate users
def login(username, password, credentials_list):
    return any(row['Username'].lower() == username.lower() and row['Password'].lower() == password.lower() for row in credentials_list)

# Function to establish connection to the MySQL database
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            user='username',
            password='pass',
            database='Bank_mgt'
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Function to view all records in the Customer_details table
def view_customer_records(mycursor):
    try:
        mycursor.execute("SELECT * FROM Customer_details")
        records = mycursor.fetchall()
        for record in records:
            print(record)
    except mysql.connector.Error as e:
        print(f"Error viewing customer records: {e}")

# Function to add a new record to the Customer_details table
def add_customer_record(mycursor, mydb):
    try:
        customer_id = input("Enter customer ID: ")
        customer_name = input("Enter customer name: ")
        mobile_no = input("Enter mobile number: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        account_id = input("Enter account ID: ")

        sql = "INSERT INTO Customer_details (customer_id, customer_name, mobile_no, dob, account_id) VALUES (%s, %s, %s, %s, %s)"
        val = (customer_id, customer_name, mobile_no, dob, account_id)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding customer record: {e}")

# Function to update a record in the Customer_details table
def update_customer_record(mycursor, mydb):
    try:
        customer_id = input("Enter customer ID to update: ")
        mobile_no = input("Enter new mobile number: ")

        sql = "UPDATE Customer_details SET mobile_no = %s WHERE customer_id = %s"
        val = (mobile_no, customer_id)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating customer record: {e}")

# Function to delete a record from the Customer_details table
def delete_customer_record(mycursor, mydb):
    try:
        customer_id = input("Enter customer ID to delete: ")

        sql = "DELETE FROM Customer_details WHERE customer_id = %s"
        val = (customer_id,)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting customer record: {e}")

# Function to view all records in the Account_details table
def view_account_records(mycursor):
    try:
        mycursor.execute("SELECT * FROM Account_details")
        records = mycursor.fetchall()
        for record in records:
            print(record)
    except mysql.connector.Error as e:
        print(f"Error viewing account records: {e}")

# Function to add a new record to the Account_details table
def add_account_record(mycursor, mydb):
    try:
        account_id = input("Enter account ID: ")
        account_type = input("Enter account type (Savings/Deposit): ")
        branch_id = input("Enter branch ID: ")
        account_balance = input("Enter account balance: ")

        sql = "INSERT INTO Account_details (account_id, account_type, branch_id, account_balance) VALUES (%s, %s, %s, %s)"
        val = (account_id, account_type, branch_id, account_balance)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding account record: {e}")

# Function to update a record in the Account_details table
def update_account_record(mycursor, mydb):
    try:
        account_id = input("Enter account ID to update: ")
        account_balance = input("Enter new account balance: ")

        sql = "UPDATE Account_details SET account_balance = %s WHERE account_id = %s"
        val = (account_balance, account_id)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating account record: {e}")

# Function to delete a record from the Account_details table
def delete_account_record(mycursor, mydb):
    try:
        account_id = input("Enter account ID to delete: ")

        sql = "DELETE FROM Account_details WHERE account_id = %s"
        val = (account_id,)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting account record: {e}")

# Function to view all records in the Employee_details table
def view_employee_records(mycursor):
    try:
        mycursor.execute("SELECT * FROM Employee_details")
        records = mycursor.fetchall()
        for record in records:
            print(record)
    except mysql.connector.Error as e:
        print(f"Error viewing employee records: {e}")

# Function to add a new record to the Employee_details table
def add_employee_record(mycursor, mydb):
    try:
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        department = input("Enter employee department: ")

        sql = "INSERT INTO Employee_details (employee_id, name, position, department) VALUES (%s, %s, %s, %s)"
        val = (employee_id, name, position, department)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding employee record: {e}")

# Function to update a record in the Employee_details table
def update_employee_record(mycursor, mydb):
    try:
        employee_id = input("Enter employee ID to update: ")
        position = input("Enter new position: ")
        department = input("Enter new department: ")

        sql = "UPDATE Employee_details SET position = %s, department = %s WHERE employee_id = %s"
        val = (position, department, employee_id)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating employee record: {e}")

# Function to delete a record from the Employee_details table
def delete_employee_record(mycursor, mydb):
    try:
        employee_id = input("Enter employee ID to delete: ")

        sql = "DELETE FROM Employee_details WHERE employee_id = %s"
        val = (employee_id,)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Record deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting employee record: {e}")

# Main menu function
def main_menu(mycursor, mydb):
    while True:
        print("\nMain Menu:")
        print("1. Customer Details")
        print("2. Account Details")
        print("3. Employee Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu(mycursor, mydb)
        elif choice == '2':
            account_menu(mycursor, mydb)
        elif choice == '3':
            employee_menu(mycursor, mydb)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Customer menu function
def customer_menu(mycursor, mydb):
    while True:
        print("\nCustomer Menu:")
        print("1. View Customer Records")
        print("2. Add Customer Record")
        print("3. Update Customer Record")
        print("4. Delete Customer Record")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_customer_records(mycursor)
        elif choice == '2':
            add_customer_record(mycursor, mydb)
        elif choice == '3':
            update_customer_record(mycursor, mydb)
        elif choice == '4':
            delete_customer_record(mycursor, mydb)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Account menu function
def account_menu(mycursor, mydb):
    while True:
        print("\nAccount Menu:")
        print("1. View Account Records")
        print("2. Add Account Record")
        print("3. Update Account Record")
        print("4. Delete Account Record")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_account_records(mycursor)
        elif choice == '2':
            add_account_record(mycursor, mydb)
        elif choice == '3':
            update_account_record(mycursor, mydb)
        elif choice == '4':
            delete_account_record(mycursor, mydb)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Employee menu function
def employee_menu(mycursor, mydb):
    while True:
        print("\nEmployee Menu:")
        print("1. View Employee Records")
        print("2. Add Employee Record")
        print("3. Update Employee Record")
        print("4. Delete Employee Record")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_employee_records(mycursor)
        elif choice == '2':
            add_employee_record(mycursor, mydb)
        elif choice == '3':
            update_employee_record(mycursor, mydb)
        elif choice == '4':
            delete_employee_record(mycursor, mydb)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    csv_file_path = r'C:\Users\Dekstop\Login.csv' # Replace csv file
    credentials_list = read_credentials_from_csv(csv_file_path)

    if credentials_list is not None:
        while True:
            username, password = input("Enter username: "), input("Enter password: ")

            if login(username, password, credentials_list):
                print("Login successful!")
                mydb = connect_to_database()
                if mydb:
                    mycursor = mydb.cursor()
                    main_menu(mycursor, mydb)
                    mycursor.close()
                    mydb.close()
                break
            else:
                print("Invalid username or password. Try again.")

if __name__ == "__main__":
    main()
