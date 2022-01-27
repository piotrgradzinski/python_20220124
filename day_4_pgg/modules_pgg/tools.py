import datetime
from dateutil.relativedelta import relativedelta
from config import db_config

my_string = "Ala ma kota"
my_list = [10, 20, 30, 40, 50,]


def added(a: int, b: int) -> int:
    return a + b

class Person:
    def __init__(self, person_first_name, person_last_name, date_of_birth: str) -> None:
        self.first_name = person_first_name
        self.last_name = person_last_name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'Person ({self.get_full_name()})'

    @property
    def age(self) -> int:
        return relativedelta(datetime.datetime.now(), self.date_of_birth).years

class Student(Person):
    def __init__(self, person_first_name, person_last_name, date_of_birth: str, field: str, index_number: str) -> None:
        super().__init__(person_first_name, person_last_name, date_of_birth)
        self.field = field
        self.index_number = index_number

    def __str__(self) -> str:
        return f'Student ({self.first_name} {self.last_name}), {self.field}, index {self.index_number}'



print('Ala ma kota  akot ma kompilator.')
