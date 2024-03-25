import mariadb
import sys

def main():
    cust_id = input('\n Please enter customer ID number: ')
    try: 
        conn = mariadb.connect(
            user='root',
            password='password1',
            host='127.0.0.1',
            port=3306,
            database='game_store_customer_db'
        )
        cust = conn.cursor()
        menu(cust)
        conn.close()
    except mariadb.Error as err:
        print(f"An error has occurred whilst connecting to MariaDB: {err}")
        sys.exit(1)


def menu(cust):
    cust_id = input('\n Please enter customer ID number: ')
    while option != 6:
        option = input('\nUser Update Menu\n1. First Name\n2. Last Name\n3. Email\n4. Phone Number\n5. Birth Date\n6. Exit\nSelect Option: ')
    if(option == 1):
        update_first_name(cust,cust_id)
    
def update_first_name(cust,cust_id):
    new_first_name = input('\n Please enter new phon number: ')
    update_cust = f"UPDATE customer_view SET first_name='{new_first_name}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()
    vaildate_update(cust_id)
    
def update_first_name(cust,cust_id):
    new_phone = input('\n Please enter new phon number: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_phone}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()
    
def update_first_name(cust,cust_id):
    new_phone = input('\n Please enter new phon number: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_phone}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()

def update_email(cust,cust_id):
    new_email = input('\n Please enter new email: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_email}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()
    
def update_phone(cust,cust_id):
    new_phone = input('\n Please enter new phon number: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_phone}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()
    
def update_email(cust,cust_id):
    new_email = input('\n Please enter new email: ')
    update_cust = f"UPDATE customer_view SET phone_number='{new_email}' WHERE customer_id={cust_id}"
    cust.execute(update_cust)
    cust.commit()
    
def validate_update(cust):
    


if __name__ == "__main__":
    main()
