import sqlite3 
from random import choice
from time import strftime

DB = None
CONN = None

def get_a_name():
	query = """SELECT * FROM CallView"""
	DB.execute(query)
	customers_to_call = DB.fetchall()
	customer_to_call = choice(customers_to_call)

	return customer_to_call

def display_customer(customer_to_call):
	customer_id = customer_to_call[0]
	first_name = str(customer_to_call[1])
	last_name = str(customer_to_call[2])
	phone_number = str(customer_to_call[3])
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print "Customer ID: ", customer_id
	print "Name: ", first_name, last_name
	print "Phone: ", phone_number
	print "\n"
	called = raw_input("Call made? Y or N (or Q): ")
	cust_id_and_called = [customer_id, called]
	return cust_id_and_called

def update_db(cust_id_and_called):
	customer_id, called = cust_id_and_called
	todays_date = strftime("%m/%d/%y")
	print todays_date
	if called == "Y" or called == "y":
		query = """UPDATE customers SET called = ? WHERE customer_id = ?"""
		DB.execute(query, (todays_date, customer_id))
		CONN.commit()
		print "\nGood work!\n"
		update_db(display_customer(get_a_name()))

	elif called == "Q" or called == "q":
		print "Quittin' time"
	else:
		print "\nCall another!\n"
		update_db(display_customer(get_a_name()))



def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("melons.db")
    DB = CONN.cursor()


def main():
	connect_to_db()
	update_db(display_customer(get_a_name()))
	CONN.close()

if __name__ == "__main__":
    main()
