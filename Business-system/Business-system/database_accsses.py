import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Mihaela\PROJECTS\Kasi Tempra Pak\QR_Code_generator\Business-system\database\test_1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Table1')
   
for row in cursor.fetchall():
    print (row)
