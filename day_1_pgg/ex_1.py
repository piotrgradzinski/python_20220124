"""
Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej 
przez użytkownika liczby kilometrów, ceny paliwa oraz spalania. 
Zapytaj użytkownika także o nazwy miejscowości.

Przykładowe komunikaty programu:
Miasto A: Warszawa
Miasto B: Gdańsk
Dystans Warszawa-Gdańsk: 420
Cena paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105 PLN
"""

city_a = input("Miasto A: ")
city_b = input("Miasto B: ")
distance = float(input("Dystans " + city_a + " " + city_b + ": "))
fuel_price = float(input("Cena paliwa: "))
fuel_consumption = float(input("Spalanie na 100 km: "))

cost = distance * fuel_consumption / 100.0 * fuel_price


"""
str + str -> OK
str + float -> TypeError, blad
"""
# print('Koszt przejazdu ' + city_a + '-' + city_b + ' to ' + cost + ' PLN')
print('Koszt przejazdu ' + city_a + '-' + city_b + ' to ' + str(cost) + ' PLN')

# budowanie napisow przy pomocy f-string
"""
Zalety f-string:
- nie musimy konwertowac typow
- mozemy w {} podawac wyrazenia do wyliczenia
- mozemy uzywac format-specifier https://docs.python.org/3/library/string.html#format-specification-mini-language
"""
print(f"Koszt przejazdu {city_a}-{city_b} to {cost} PLN")
print(f"Koszt przejazdu {city_a}-{city_b} to {round(cost, 2)} PLN")
print(f"Koszt przejazdu {city_a}-{city_b} to {cost:_^10.2f} PLN")

# .format()
print("Koszt przejazdu {0}-{1} to {2} PLN".format(city_a, city_b, cost))
