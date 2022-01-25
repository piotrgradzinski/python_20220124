"""
Napisz program wyliczający kwotę należną za zakupiony towar
na podstawie podanej przez użytkownika wagi i nazwy produktu.
Do przechowywania informacji o cenie za kilogram
danego produktu użyj słownika.
Wypisz wszystkie dostępne produkty w sklepie.


1. Robimy słownik z produktami, dodajmy:
      ziemniaki 1.2
      pomidory 4.5
      marchew 0.5
2. Wyświetlam słownik
3. Pytam użytkownika o produkt i sprawadzam czy jest w produktach
4. Wczytujemy ile kg uzytkownik chce kupic
5. Liczymy należnosc
"""

products = {
    'ziemniaki': 1.2,
    'pomidory': 4.5,
    'marchew': 0.5,
}

for product, price in products.items():
    print(f'{product} - {price:.2f} PLN / kg')

user_choice = input('Jaki produkt chcesz kupic? ')

weight = float(input(f"Ile kilogramow produktu {user_choice} chcesz kupic? "))

due = weight * products.get(user_choice, 0.0)

print(f'Za {weight:.2f} kg produktu {user_choice} zaplacisz {due:.2f} PLN.')
