"""
SQLAlchemy - ORM (Object-Relational Mapping)
- https://www.sqlalchemy.org/
- https://realpython.com/search?q=sqlalchemy 
- https://realpython.com/python-sqlite-sqlalchemy/
- mozemy stworzyc w pythonie klasy, ktore beda reprezentowaly tabele z bazy danych
- odchodze od pisania standardowych zapytan na rzecz pracy z obiektami
- instalacja: pip install sqlalchemy
- KOD W PYTHONIE <-> (SQLALCHEMY <-> SQL) <-> BAZA DANYCH
"""

from sqlalchemy import create_engine, or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()
engine = create_engine('sqlite:///day_5_pgg/chinook.db')
Base.prepare(engine, reflect=True)
session = Session(engine)

Employees = Base.classes.employees
Invoices = Base.classes.invoices

employees = session.query(Employees).all()
for employee in employees:
    print(type(employee), employee.FirstName, employee.LastName)


# invoices = session.query(Invoices).filter(Invoices.Total > 15)
# select * from invoices where BillingCity = 'Berlin'
invoices = session.query(Invoices).filter(or_(Invoices.BillingCity == 'Berlin', Invoices.Total > 15)) 
for invoice in invoices:
    print(invoice.InvoiceId, invoice.Total, invoice.BillingCity)

