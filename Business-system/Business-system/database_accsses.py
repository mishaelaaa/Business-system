import pyodbc
###lib for connect python code and accsses database 

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Mihaela\PROJECTS\Kasi Tempra Pak\QR_Code_generator\Business-system\database\test_1.accdb;')
### parth with source 
cursor = conn.cursor()
cursor.execute('select * from Table1')
### choose the table 

for row in cursor.fetchall():
    print (row)
