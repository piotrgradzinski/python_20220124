"""
Przekazywanie argumentow do programu, przy pomocy sys.argv

Kody funkcji exit()
- 0 - program zakonczony powodzeniem, 
- inna wartość oznacza blad
- http://www.bic.mni.mcgill.ca/~dale/helppages/BashGuide/advshell/exitcodes.html
"""

import sys
import json

"""
0  - nazwa naszego programu
1+ - argumenty, ktore przekazujemy do naszego programu
"""
print(sys.argv)

try: 
    with open(sys.argv[1]) as file_handle:
        json_data = json.load(file_handle)
        print(json_data)
except IndexError:
    print('Usage: python argv_intro.py FILE_NAME')
    exit(1)
except FileNotFoundError:
    print(f'File not found.')
    exit(1)
