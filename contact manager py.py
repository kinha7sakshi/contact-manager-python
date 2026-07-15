import sqlite3
connection = sqlite3.connect("contacts_v1.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts_v1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone INTEGER)""")
connection.commit()
def add_contact():
	name=input("Enter your name:")
	phone=int(input("Enter your phone:"))
	cursor.execute( "INSERT INTO contacts_v1 (name,phone) VALUES (?,?)",(name,phone))
	connection.commit()
	print("Contact added sucessfully")
def view_contact():
			cursor.execute("SELECT * FROM contacts_v1")
			records = cursor.fetchall()
			if records:
				for record in records:
					print("ID:", record[0])
					print("Name:", record[1])
					print("Phone:", record[2])
					print("--------------------")
			else:
				print("No contacts found.")
def search_contact():
		try:
			contact_id=int(input("Enter ID to search:"))
		except ValueError:
			print("Please enter digits only.")
			return
		cursor.execute("SELECT * FROM contacts_v1 WHERE id = ?" ,(contact_id,))
		records=cursor.fetchall()
		if records:
			for record in records:
				print("ID:", record[0])
				print("Name:", record[1])
				print("Phone:", record[2])
				print("--------------------")
		else:
			print("Contact not found.")
def update_contact():
		try:
			contact_id=int(input("Enter ID:"))
			phone=int(input("Enter new phone:"))
		except ValueError:
			print("Please enter digits only.")
			return
		cursor.execute("UPDATE contacts_v1 SET phone=? WHERE id=?", (phone,contact_id))
		connection.commit()
		if cursor.rowcount == 0:
			print("No contact found with that ID.")
		else:
			print("Contact updated successfully.")
		cursor.execute("SELECT * FROM contacts_v1")
		records=cursor.fetchall()
		for record in records:
			print("ID:", record[0])
			print("Name:", record[1])
			print("Phone:", record[2])
			print("--------------------")
def delete_contact():
		try:
			contact_id=int(input("Enter ID to delete:"))
		except ValueError:
			 print("Please enter digits only.")
			 return
		cursor.execute("DELETE FROM contacts_v1 WHERE id=?",(contact_id,))
		connection.commit()
		if cursor.rowcount == 0:
			 print("No contact found with that ID.")
		else:
			print("Contact deleted successfully.")
		cursor.execute("SELECT * FROM contacts_v1")
		records = cursor.fetchall()
		for record in records:
			print("ID:", record[0])
			print("Name:", record[1])
			print("Phone:", record[2])
			print("--------------------")
while True:
	print("=====Contact Manager v1.0=====")
	print("1.Add Contact")
	print("2.View Contact")
	print("3.Search Contact")
	print("4.Update Contact")
	print("5.Delete Contact")
	print("6.Exit")
	choice= input("Enter your choice(1-6):")
	if choice=="1":
		add_contact()
	elif choice=="2":
		view_contact()
	elif choice=="3":
		search_contact()
	elif choice=="4":
		update_contact()
	elif choice=="5":
		delete_contact()
	elif choice=="6":
		print("Goodbye")
		connection.close()
		break