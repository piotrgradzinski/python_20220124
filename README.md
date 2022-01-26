# Python 20220124

# Rozdzial

Ala *ma* **kota** a kot ma [kompilator](https://www.alx.pl).

- `lista` 1
- lista 2
- lista 3

## Podrozdzial

```python
class Student(Person):
    def __init__(self, person_first_name, person_last_name, date_of_birth: str, field: str, index_number: str) -> None:
        super().__init__(person_first_name, person_last_name, date_of_birth)
        self.field = field
        self.index_number = index_number

    # przykrywam (ang. override) metode __str__ z rodzica, wersja dla Studenta
    def __str__(self) -> str:
        return f'Student ({self.first_name} {self.last_name}), {self.field}, index {self.index_number}'

```

### Podpodrozdzial