"""
Na podstawie tabeli invoices przygotuj raport w Excelu, który
wskaże sumę faktur dla każdego państwa w podziale na lata.

Obliczenia, agregację wykonaj w Pythonie.

Przykład:
Argentina | 2010 | 11.88
Argentina | 2011 | 0.99
Argentina | 2013 | 24.75
"""

from collections import defaultdict
from pprint import pprint
import sqlite3
from dateutil.parser import parse
from openpyxl import Workbook

# polaczenie z baza i odczyt faktur
con = sqlite3.connect('day_5_pgg/chinook.db')
con.row_factory = sqlite3.Row

cur = con.cursor()
invoices = cur.execute('select * from invoices').fetchall()

# przetwarzanie danych
report_data = {}

for invoice in invoices:
    if invoice['BillingCountry'] not in report_data:
        report_data[invoice['BillingCountry']] = defaultdict(float)

    year = parse(invoice['InvoiceDate']).year

    report_data[invoice['BillingCountry']][year] += invoice['Total']

pprint(report_data)

# zapis do excela
wb = Workbook()
ws = wb.active

ws.append(['Country', 'Year', 'Total'])

"""
sorted(report_data.items()) - sortujemy liste tupli (kazda tupla to klucz i wartosc), 
standardowo jak sortujemy tuple, to sortujemy po wartosci pod kluczem 0.
"""

for country, yearly_data in sorted(report_data.items()):
    for year, total in sorted(yearly_data.items()):
        ws.append([country, year, total])

# https://openpyxl.readthedocs.io/en/stable/filters.html
ws.auto_filter.ref = "A:C"
ws.auto_filter.add_filter_column(0, ["Austria"])

wb.save('day_5_pgg/invoices_report.xlsx')
