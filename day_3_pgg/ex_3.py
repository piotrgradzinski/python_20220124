"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka. 
Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
Zaimplementuj metodę obliczającą ile produktów znajduje się w koszyku.
Zaimplementuj właściwość wskazującą czy koszyk jest pusty.
Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję. 

Do trzymania produktów w koszyku wykorzystac slownik.

https://yuml.me/3519f876.png

Przykład użycia:
> basket = Basket()
> product = Product(1, 'Woda', 10.00)
> basket.add_product(product, 5)
> basket.count_total_price()
50.0
> basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
> basket.count_products()
1
> basket.is_empty
False
"""

from day_3_pgg.ex_1 import Product

class Basket:
    def __init__(self) -> None:
        self._items = dict()

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if not isinstance(product, Product):
            raise TypeError('You can add only products.')

        if quantity <= 0:
            raise ValueError('Quantity has to be greater than 0.')

        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    def count_total_price(self) -> float:
        total_price = 0.0

        for product, quantity in self._items.items():
            total_price += product.price * quantity

        return total_price

    def generate_report(self) -> None:
        print('Products in basket:')
        for product, quantity in self._items.items():
            print(f'{product} x {quantity}')
        print(f'Total due: {self.count_total_price():.2f} PLN')

    def count_products(self) -> int:
        return len(self._items)

    @property
    def is_empty(self) -> bool:
        if len(self._items) == 0:
            return True
        else:
            return False


basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
print(basket.count_total_price())
basket.generate_report()
print(basket.count_products())
print(basket.is_empty)
