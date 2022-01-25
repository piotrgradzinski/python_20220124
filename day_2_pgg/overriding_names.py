"""
Uwaga na nadawanie nazw zmiennym (czy funkcja) o takich nazwach jak typy wbudowane w pythona. 
"""

dict = {}
dict['asd'] = 123
print(dict)

my_dict2 = dict()  # TypeError
