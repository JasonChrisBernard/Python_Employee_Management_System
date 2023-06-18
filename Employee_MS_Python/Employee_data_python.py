import mysql.connector
import random

# Database connection details
host = "localhost"
user = "root"
password = ""
database_name = "Employee_MS"
table = "Employee_t"

# Create a connection object
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)


# Create a cursor object
cursor = mydb.cursor()
    

def main():
    sql_conn()
    val = True
    while(val):   
        print("Employee Management Data")
        print("Choose your option between 1 to 6 ")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Edit Employee")
        print("4. Search Employee")
        print("5. View Employee Details")
        print("6. Exit Program")
        opt = int(input("Enter your option between 1 to 6 \n"))
        
        
        if opt == 1:
            add(cursor)
        elif opt == 2:
             delete(cursor)
        elif opt == 3:
             edit(cursor)
        elif opt == 4:
             search(cursor)
        elif opt == 5:
             view(cursor)
        elif opt == 6:
            val = False
        else:
            print("Please Enter the correct option again")


def sql_conn():
    # Check if the database already exists
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    exists = cursor.fetchone()

    # Create the database if it doesn't exist
    if not exists:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"The database '{database_name}' has been created.")
    else:
        print(f"The database '{database_name}' already exists.")

    # Use the database
    cursor.execute(f"USE {database_name}")

    # Check if the database table already exists
    cursor.execute(f"SHOW TABLES LIKE '{table}'")
    exists = cursor.fetchone()

    # Create the database table if it doesn't exist
    if not exists:
        cursor.execute(f"CREATE TABLE {table}(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary DECIMAL(10,2), address VARCHAR(255), department VARCHAR(255),email VARCHAR(255))")
        print(f"The table '{table}' has been created.")
    else:
        print(f"The table '{table}' already exists.")

    
    
   


def add(cursor):
    while True:
        name = input("Enter the name: ")
        if not name:
            print("Name is required. Please try again.")
            continue

        try:
            salary = float(input("Enter the Salary: "))
        except ValueError:
            print("Invalid salary. Please enter a numeric value.")
            continue

        address = input("Enter the Address: ")
        if not address:
            print("Address is required. Please try again.")
            continue

        department = input("Enter the Department: ")
        if not department:
            print("Department is required. Please try again.")
            continue

        email = input("Enter the Email: ")
        if not email:
            print("Email is required. Please try again.")
            continue

        # If all input values are valid, execute the SQL statement
        sql = f"INSERT INTO {table} (name, salary, address, department, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, salary, address, department, email))
        mydb.commit()

        # Get the auto-incremented ID of the inserted record
        id_num = cursor.lastrowid

        # Print the ID of the inserted record
        print("Record inserted successfully! ID:", id_num)
        break

   

    

def delete(cursor):
    while True:
        id_num = input("Enter the Employee ID: ")
        if not id_num:
            print("Employee ID is required. Please try again.")
            continue

        # Check if the employee ID exists in the table
        cursor.execute(f"SELECT * FROM {table} WHERE id = %s", (id_num,))
        result = cursor.fetchone()
        if not result:
            print("Employee ID not found. Please enter a valid ID.")
            continue

        # Execute the DELETE statement
        sql = f"DELETE FROM {table} WHERE id = %s"
        cursor.execute(sql, (id_num,))
        mydb.commit()

        print(cursor.rowcount, "record(s) deleted")

        break
    
    


def edit(cursor):
    while True:
        id_num = input("Enter the Employee ID: ")

        # Check if the employee ID exists in the table
        cursor.execute(f"SELECT * FROM {table} WHERE id = %s", (id_num,))
        result = cursor.fetchone()
        if not result:
            print("Employee ID not found. Please enter a valid ID.")
            continue

        break

    while True:
        new_name = input("Enter the name: ")
        if not new_name:
            print("Name is required. Please try again.")
            continue

        new_salary = input("Enter the Salary: ")
        if not new_salary:
            print("Salary is required. Please try again.")
            continue
        try:
            new_salary = float(new_salary)
        except ValueError:
            print("Invalid Salary. Please enter a numeric value.")
            continue

        new_address = input("Enter the Address: ")
        if not new_address:
            print("Address is required. Please try again.")
            continue

        new_department = input("Enter the Department: ")
        if not new_department:
            print("Department is required. Please try again.")
            continue

        new_email = input("Enter the Email: ")
        if not new_email:
            print("Email is required. Please try again.")
            continue

        break

    # Execute the UPDATE statement
    sql = f"UPDATE {table} SET name = %s, salary = %s, address = %s, department = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (new_name, new_salary, new_address, new_department, new_email, id_num))
    mydb.commit()

    print(cursor.rowcount, "record(s) updated")

    
    

def search(cursor):
    while True:
        id_num_or_name = input("Enter the Employee ID or name to search: ")

        # Execute the SELECT statement with the search query
        sql = f"SELECT * FROM {table} WHERE id = %s OR name = %s"
        cursor.execute(sql, (id_num_or_name, id_num_or_name))

        # Fetch all matching rows
        result = cursor.fetchall()

        if not result:
            print("Employee ID or name not found. Please enter a valid ID or name.")
            continue

        break

    # Print the total number of rows
    print("Total number of rows in table:", cursor.rowcount)

    # Print each row
    print("\nPrinting each row")
    for row in result:
        print("Id =", row[0])
        print("Name =", row[1])
        print("Salary =", row[2])
        print("Address =", row[3])
        print("Department =", row[4])
        print("Email =", row[5], "\n")
    
    
    
    


def view(cursor):
    cursor.execute(f"SELECT * FROM {table}")
    results = cursor.fetchall()

    if len(results) == 0:
        print("No records found.")
    else:
        print("Employee details:")
        print("+----+--------------+------------+---------------+----------------+-----------------+")
        print("| ID | Name         | Salary     | Address       | Department     | Email           |")
        print("+----+--------------+------------+---------------+----------------+-----------------+")
        for row in results:
            print(f"| {row[0]:<2} | {row[1]:<12} | {row[2]:<10.2f} | {row[3]:<14} | {row[4]:<14} | {row[5]:<16} |")
        print("+----+--------------+------------+---------------+----------------+-----------------+")
    
  

if __name__ == "__main__":
    main()
    
cursor.close()
mydb.close()
