
#pip install mysql-connector-python
import mysql.connector
'''
#Crea la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
'''

#Conecta a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS `customers` (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()#Confirma las inserciones

print(mycursor.rowcount, "was inserted.") #Cuenta cuántas inserciones se realizaron


mycursor.execute("SELECT * FROM customers")

#Recupera los resultados de la última consulta
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


sql = "SELECT name FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

print("\n Las personas cuya dirección es Yellow Garden 2 son: ")
for x in myresult:
  print(x)