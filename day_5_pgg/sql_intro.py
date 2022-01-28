"""
SQL na przykladzie SQLite
Baza testowa: https://www.sqlitetutorial.net/sqlite-sample-database/
jej schemat: https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf
Diagramy ERD:
- https://pl.wikipedia.org/wiki/Diagram_zwi%C4%85zk%C3%B3w_encji
- https://www.guru99.com/er-diagram-tutorial-dbms.html

Narzedzie do robienia diagramow (wszelakich): https://app.diagrams.net/
Wtyczka SQLite do Visual Studio Code: 
- SQLite (ta z piorkiem)
- https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite
- po instalacji: ctrl+shift+p ->  SQLite: Open database
"""
from pprint import pprint
import sqlite3

# jezeli sqlite3.connect nie znajdzie tego pliku, to pod ta sciezka sprobuje go utworzyc
con = sqlite3.connect('day_5_pgg/chinook.db')
print(type(con))

"""
Jak wydajemy zapytania do bazy? 
1. Uzyskanie kursora (ang. cursor)
2. Wykonuje zapytanie
3. W kursorze pojawiaja sie dane, ktore moge odczytac
"""

# select
cur = con.cursor()
# cur.execute('select * from customers where Country = \'Brazil\'')
cur.execute('''
select * 
from customers 
where Country = 'Brazil'
''')
# execute(zapytanie_sql, tupla_z_parametrami)
# cur.execute('select * from customers where Country = ?', ('Brazil',))

customers = cur.fetchall()
pprint(customers)
print(type(customers))
print(type(customers[0]))

for customer in customers:
    print(customer[1], customer[2])

# insert 
cur = con.cursor()
sql = 'insert into employees  (FirstName, LastName, Title) values (?, ?, ?)'
sql_data = ('Piotr', 'GG', 'Trainer')
cur.execute(sql, sql_data)
employee_id = cur.lastrowid
"""
Dla operacji, ktore modyfikuja dane w bazie, musimy uruchomic metode commit na polaczeniu.
"""
con.commit()
print(employee_id)

# update
cur = con.cursor()
sql = 'update employees set LastName=? where EmployeeId=?'
sql_data = ('Grabski-Gradzinski', employee_id)
cur.execute(sql, sql_data)
con.commit()

# delete
cur = con.cursor()
sql = 'delete from employees where EmployeeId=?'
sql_data = (employee_id,)
cur.execute(sql, sql_data)
con.commit()

con.close()

con = sqlite3.connect('day_5_pgg/chinook.db')
con.row_factory = sqlite3.Row

cur = con.cursor()
employees = cur.execute('select * from employees')

for employee in employees:
    # print(dict(employee))
    print(employee['FirstName'], employee['LastName'])

