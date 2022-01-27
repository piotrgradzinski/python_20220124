"""
Daty

https://realpython.com/python-datetime/
https://realpython.com/python-packages/#dateutil-for-working-with-dates-and-times

Bedziemy korzystali z:
- pakiet datetime - wbudowany w pythona, nie trzeba go instalowac
- dateutil - trzeba go doinstalowac https://pypi.org/project/python-dateutil/
"""

import datetime
from dateutil import tz, parser
from dateutil.relativedelta import relativedelta

# tworzenie
# date
d = datetime.date(year=2022, month=1, day=27)
print(d)

# time
t = datetime.time(hour=11, minute=4, second=30)
print(t)

# datetime
dt = datetime.datetime(year=2022, month=1, day=27, hour=11, minute=4, second=30)
print(dt)

# aktualny datetime
dt = datetime.datetime.now()
print(dt)


"""
Strefy czasowe (time zone)
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
"""

print(tz.gettz('America/St_Johns'))  # Mac/linux: /usr/share/zoneinfo/America/St_Johns

dt = datetime.datetime.now()
print(dt)

dt = datetime.datetime.now(tz.gettz('America/St_Johns'))
print(dt)
print(dt.tzname())

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.weekday())  # Monday == 0 ... Sunday == 6
print(dt.isoweekday())  # Monday == 1 ... Sunday == 7
print(dt.isocalendar().week)

# konwertowanie datetime na stringa
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# string format time
print(dt.strftime('%d.%m.%Y %H:%I:%S'))
print(dt.isoformat())  # 2022-01-27T06:51:17.022635-03:30

dt = datetime.datetime.now(tz=datetime.timezone.utc)
print(dt)
print(dt.tzname())  # UTC

dt = datetime.datetime.utcnow()  # lepiej uzywac datetime.datetime.now(tz=datetime.timezone.utc), https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow
print(dt)
print(dt.tzname())  # None


dt = datetime.datetime.now(tz=tz.tzlocal())
print(dt)
print(dt.tzname())  # CET

"""
Wczytywanie dat
timestamp - int, liczba sekund, jaka upynela od EPOCH do teraz
EPOCH - w linuxach, to 1970-01-01 00:00:00, https://en.wikipedia.org/wiki/Epoch_(computing)
epochconverter - https://www.epochconverter.com/
kiedy operujemy na timestamp, to musimy wiedzec w jakiej strefie czasowej zostaly zapisane
"""

# wczytywanie z timestampa
dt = datetime.datetime.fromtimestamp(1615890862)  
print(dt)  # 2021-03-16 11:34:22

dt = datetime.datetime.fromtimestamp(1615890862, tz=datetime.timezone.utc)
print(dt)  # 2021-03-16 10:34:22+00:00

# wczytywanie z ISO
dt = datetime.datetime.fromisoformat("2022-01-27T06:51:17.022635-03:30")  # od 3.7
print(dt)

"""
offset-naive datetime - bez strefy czasowej
offset-aware datetime - ze strefa czasowa
"""
dt1 = datetime.datetime.now()
dt2 = datetime.datetime.now(tz.gettz('America/St_Johns'))

# dt3 = dt1 - dt2  # TypeError: can't subtract offset-naive and offset-aware datetimes

# wczytywanie ze napisu
# strptime - string parse time
dt = datetime.datetime.strptime("27.01.2022 11:46:00", "%d.%m.%Y %H:%M:%S")
print(dt)

# dateutil i parser
dt = parser.parse("27.01.2022 11:46:00")
print(dt)

dt = parser.parse("2022-01-27T06:51:17.022635-03:30")
print(dt)
dt2 = dt.astimezone(tz.gettz('Europe/Warsaw'))
print(dt2)


"""
Operacje na datach
"""

dt1 = datetime.datetime.now()
dt2 = parser.parse("2020-06-16T15:18:33")
print(dt1)
print(dt2)

dt3 = dt1 - dt2
print(type(dt3))  # datetime.timedelta
print(dt3)
print(dt3.days)
print(dt3.seconds)
print(dt3.microseconds)

dt3 = dt1 + datetime.timedelta(days=3)
print(dt3)

# delta miedzy dwiema datami
dt_delta = relativedelta(dt1, dt2)
print(dt_delta)
print(dt_delta.years)
print(dt_delta.months)
print(dt_delta.days)
print(dt_delta.hours)
print(dt_delta.minutes)
print(dt_delta.seconds)

# do daty mozemy dodawac / odejmowac delte
