"""
Modul logging i logowanie dzialan w naszym programie.
https://docs.python.org/3/howto/logging.html
https://realpython.com/python-logging/
Standardowa konfiguracja modulu logging wyswietla komunikaty od poziomu warning.
Jak zmienic format wiadomosci, ktore logujemy: https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
Co mozemy umiescic w formacie dla logowanej wiadomosci: https://docs.python.org/3/library/logging.html#logrecord-attributes

"""

import logging

logging.basicConfig(level=logging.DEBUG, filename='log.txt', format='%(asctime)s|%(levelname)s|%(message)s')

logging.debug('log na debug')
logging.info('log na info')
logging.warning('log na warning')
logging.error('log na error')
logging.critical('log na critical')
