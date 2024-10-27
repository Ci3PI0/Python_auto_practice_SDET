#   Select

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', port='3306', user='root', password='root', database='students')
    cursor = connection.cursor()  # Create Cursor

    cursor.execute('select * from students')  # Execute SQL Command through cursor
    for row in cursor :
        print(row[0], row[1], row[2])

    connection.close()
    print('Finished')
except mysql.connector.Error as e:
    print(f"Connection failed: {e}")

# print(names)