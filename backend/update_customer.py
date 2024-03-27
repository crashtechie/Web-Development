import mariadb
import sys

def main():
    menu()
    

def connect_to_update(update_cust):
    try: 
        conn = mariadb.connect(
            user='root',
            password='password1',
            host='127.0.0.1',
            port=3306,
            database='game_store_customer_db'
        )
        cust = conn.cursor()
        cust.execute(update_cust)
        conn.commit()
        conn.close()
    except mariadb.Error as err:
        print(f"An error has occurred whilst connecting to MariaDB: {err}")
        sys.exit(1)
        
def menu():
    cust_id = input('\n Please enter customer ID number: ')
    option = 0
    while option != 6:
        option = int(input('\nUser Update Menu\n1. First Name\n2. Last Name\n3. Email\n4. Phone Number\n5. Birth Date\n6. Exit\nSelect Option: '))
        if(option == 1):
            update_first_name(cust_id)
        elif (option == 2):
            update_last_name(cust_id)
        elif (option == 3):
            update_email(cust_id)
        elif (option == 4):
            update_phone(cust_id)
        elif (option == 5):
            update_birth_date(cust_id)
        elif (option == 6):
            print('\nExiting...')
            option = 6
        else:
            print('\nInvalid Option. Please try again.')
    
def update_first_name(cust_id):
    new_first_name = input('\n Please enter new first name: ')
    update_cust = f"UPDATE customer_view SET first_name='{new_first_name}' WHERE customer_id={cust_id}"
    connect_to_update(update_cust)
        
def update_last_name(cust_id):
    new_last_name = input('\n Please enter new last name: ')
    update_cust = f"UPDATE customer_view SET last_name='{new_last_name}' WHERE customer_id={cust_id}"
    connect_to_update(update_cust)
    
def update_email(cust,cust_id):
    new_email = input('\n Please enter new email: ')
    update_cust = f"UPDATE customer_view SET email='{new_email}' WHERE customer_id={cust_id}"
    connect_to_update(update_cust)

def update_phone(cust,cust_id):
    new_phone = input('\n Please enter new phon number: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_phone}' WHERE customer_id={cust_id}"
    connect_to_update(update_cust)
    
def update_birth_date(cust,cust_id):
    new_dob = input('\n Please enter new birth date (yyyy-mm-dd): ')
    update_cust = f"UPDATE customer_view SET birth_date='{new_dob}' WHERE customer_id={cust_id}"
    connect_to_update(update_cust)
    
if __name__ == "__main__":
    main()
