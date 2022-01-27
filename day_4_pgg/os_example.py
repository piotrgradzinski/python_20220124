"""
Module OS

https://www.analyticsvidhya.com/blog/2021/05/30-useful-methods-from-python-os-module/
"""

import os
from pprint import pprint

# uruchamianie jakielkowiek komendy na poziomie konsoli
# print(os.system('ls'))  # na Windowsie dir

try:
    os.mkdir('day_4_pgg/os_example')  # rzuci FileExistsError jezeli katalog istnieje
    os.rmdir('day_4_pgg/os_example')
except FileExistsError:
    pass

try:
    os.makedirs('day_4_pgg/os_example/tmp1/tmp2')
except FileExistsError:
    pass

print(os.getcwd())  # bezwgledna sciezka do aktualnego katalogu

print('---')

pprint(list(os.walk('day_4_pgg')))

print('---')

base_path = os.getcwd()
folder = 'day_4_pgg/os_example/tmp1/../tmp1'
file_name = 'tmp2/20220127_1602_test.txt'

full_path = os.path.join(base_path, folder, file_name)
print(full_path)  # /Users/gradzinski/python_20220124/day_4_pgg/os_example/tmp1/../tmp1/tmp2/test.txt
print(os.path.normpath(full_path))  # /Users/gradzinski/python_20220124/day_4_pgg/os_example/tmp1/tmp2/test.txt
print(os.path.exists(full_path))  # True
print(os.path.isdir(full_path))  # False
print(os.path.isfile(full_path))  # True

# jak wyciagnac rozszerzenie pliku? Czyli dla full_path chodzi nam o .txt
print(os.path.splitext(full_path))  # ('/Users/gradzinski/python_20220124/day_4_pgg/os_example/tmp1/../tmp1/tmp2/test', '.txt')
print(os.path.splitext(full_path)[1][1:])  # txt

# z pelnej sciezki moge wyciagnac tylko nazwe pliku
print(os.path.basename(full_path))  # 20220127_1602_test.txt

print(os.path.split(full_path))

print(os.sep)

file_name = os.path.basename(full_path)
print(file_name)
parts = file_name.split('_')  # to jest metoda wbudowana w str
print(parts)

"""
glob

https://docs.python.org/3/library/glob.html
"""

import glob

files = glob.glob('./**/*.py', recursive=True)

pprint(files)

print('---')

for file in files:
    print(file)
