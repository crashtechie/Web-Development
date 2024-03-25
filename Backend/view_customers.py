import mariadb
import sys

def print_customers(cust):
    customer = []
    cust.execute("SELECT * FROM customer_view")
    for (customer_id,first_name, last_name, email, phone_number, birth_date, date_entered, notes) in cust:
        customer.append(f"{customer_id} | {first_name} | {last_name} | <{email}> | <{phone_number}> | {birth_date} | {date_entered} | {notes}")
    print("\n".join(contacts))

try: 
    conn = mariadb.connect(
        user='root',
        password='password1',
        host='127.0.0.1',
        port=3306,
        database='game_store_customer_db'
    )
    cust = conn.cursor()
    print_customers(cust)
    conn.close()
except mariadb.Error as err:
    print(f"An error has occurred whilst connecting to MariaDB: {err}")
    sys.exit(1)
