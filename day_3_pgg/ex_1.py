"""
Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu.
Zaimplementuj metodę wypisującą informacje o produkcie na konsolę oraz 
zwracająca opis w formie stringa.

Przykład użycia:
> product = Product(1, 'Woda', 10.99)
> product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN
> product_info = product.get_info()
> print(product_info)
Produkt "Woda", id: 1, cena: 10.99 PLN

Scenariusz:
1. Tworzymy klasę
2. Dodajemy __init__ (konstruktor)
3. Dodajemy atrybuty
4. Dodajemy metodę print_info(), get_info()
5. extra: dodać type hinting i dokumentcje metod
"""

class Product:
    def __init__(self, id: int, name: str, price: float) -> None:
        """
        New Product instance.
        :param id:
        :param name:
        :param price:
        """
        self.id = id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        """
        Returns basic information about the Product
        """
        return f'Product "{self.name}", id: {self.id}, price: {self.price} PLN'

    def __str__(self) -> str:
        return self.get_info()

    def print_info(self) ->  None:
        """
        Prints to the console information about the Product, based on .get_info().
        """
        print(self.get_info())


product = Product(1, 'Woda', 10.99)
product.print_info()
product_info = product.get_info()
print(product_info)

product2 = Product(2, 'Pomidory', 3.99)
print(product2)
