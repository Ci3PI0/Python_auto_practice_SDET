#  Insert, Update, Delete, Select

insert_query = 'insert into students value(13,"Kimiko",50)'
update_query = 'update students set Num = 13, marks = 50 where Name = "Saken" '
delete_query = 'delete from students where marks = 50'

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', port='3306', user='root', password='root', database='students')
    cursor = connection.cursor()  # Create Cursor
    #  Insert Data to DB
    cursor.execute(insert_query)  # Execute SQL Command through cursor
    #  Update Data in DB
    # cursor.execute(update_query)  # Execute SQL Command through cursor
    #  Delete specific data from DB
    cursor.execute(delete_query)  # Execute SQL Command through cursor
    connection.commit()  # Commit SQL Command
    connection.close()
    print('Finished')
except mysql.connector.Error as e:
    print(f"Connection failed: {e}")
