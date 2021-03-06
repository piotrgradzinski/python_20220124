"""
Utwórz następującą strukturę pakietów i modułów:
- główny pakiet mathematica
- pakiet wewnętrzny geometry
- moduł figures w pakiecie geometry z funkcjami
    - square_area oraz triangle_area
- pakiet wewnętrzny algebra
- moduł formulas w pakiecie algebra z funkcjami
    - add, substract, multiply, divide

Struktura katalogów i plików:
mathematica/
    algebra/
        formulas.py
    geometry/
        figures.py

W pliku z tym cwiczeniem policz: 
- pole kwadratu o boku 5
- podziel 10 przez 2
"""

# tutaj robimy importy:
# from PAKIET.MODUL import cos
# from mathematica.algebra.formulas import square_area
# import PAKIET.MODUL

from mathematica.geometry.figures import square_area
print(square_area(5))

# import mathematica.algebra.formulas
# print(mathematica.algebra.formulas.divide(10, 2))

import mathematica.algebra.formulas as mathfo
print(mathfo.divide(10, 2))
