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

class Element:
    def __init__(self, content) -> None:
        self.content = content

    def __str__(self) -> str:
        return f'{self.content}'

class HeaderElement(Element):
    def __str__(self) -> str:
        rendered_content = super().__str__()
        # return f'{rendered_content}\n{"=" * len(rendered_content)}'
        return rendered_content + '\n' + ('=' * len(rendered_content))

class LinkElement(Element):
    def __init__(self, content, url) -> None:
        super().__init__(content)
        self._url = url

    def __str__(self) -> str:
        return f'[{super().__str__()}]({self._url})'

class Document:
    def __init__(self) -> None:
        self._elements = []

    def add_element(self, element: Element) -> None:
        if not isinstance(element, Element):
            raise TypeError('You can only add Element objects.')

        self._elements.append(element)

    def render(self) -> None:
        rendered_elements = [str(element) for element in self._elements]
        result = '\n'.join(rendered_elements)  # join to metoda z str
        print(result)

document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'http://abc.com'))
document.add_element(Element('Simple'))
document.render()
