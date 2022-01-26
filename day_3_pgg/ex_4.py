"""
Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown. 
Stwórz klasę bazową Element zawierającą podstawową implementację metody render() 
oraz kilka jej klas pochodnych. Stwórz klasę Document umożliwiającą wyrenderowanie dodanych elementów.

UML: https://drive.google.com/file/d/1ZblDnt6xSjpuPfO-1dtnh8K09CwtuLMK/view

Przykład użycia:
> document = Document()
> document.add_element(HeaderElement('Header'))
> document.add_element(LinkElement('ABC', 'http://abc.com'))
> document.add_element(Element('Simple'))
> document.render()
Header
======
[ABC](http://abc.com)
Simple
"""

