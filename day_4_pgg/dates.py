"""
Daty

https://realpython.com/python-datetime/
https://realpython.com/python-packages/#dateutil-for-working-with-dates-and-times

Bedziemy korzystali z:
- pakiet datetime - wbudowany w pythona, nie trzeba go instalowac
- dateutil - trzeba go doinstalowac https://pypi.org/project/python-dateutil/
"""

import datetime

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

from dateutil import tz

print(tz.gettz('America/St_Johns'))

