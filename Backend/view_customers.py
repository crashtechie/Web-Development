import mariadb
import sys

user = input('\nEnter Username: ')
password = input('\n Enter Password: ')
print('\n connecting to MariaDB... \n')

def print_customers(cust):
    contacts = []
    cust.execute("SELECT customer_id,first_name,last_name,email,phone,notes,customer_since,active FROM customers")
    for (customer_id,first_name, last_name, email, phone, notes, customer_since, active) in cust:
        contacts.append(f"{customer_id} | {first_name} | {last_name} | <{email}> | <{phone}> | {notes} | {customer_since} | {active}")
    print("\n".join(contacts))

try: 
    conn = mariadb.connect(
        user=user,
        password=password,
        host='127.0.0.1',
        port=3306,
        database='game_store'
    )
    cust = conn.cursor()
    print_customers(cust)
    conn.close()
except mariadb.Error as err:
    print(f"An error has occurred whilst connecting to MariaDB: {err}")
    sys.exit(1)
