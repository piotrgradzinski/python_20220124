"""
Obsluga plikow w pythonie
- otwieramy plik - oddaje nam uchwyt do pliku
    - jezeli nie ma pliku, nie mozna go znalezc to dostajemy FileNotFoundError
    - przy otwarciu pliku, moze podac tryb w jakim go otwieramy, standardowo to tryb 'r', czyli do odczytu
    - https://docs.python.org/3/library/functions.html#open
    - https://stackoverflow.com/a/16212401/779084 
    - r - czytanie (domyślny), FileNotFoundError jak nie ma pliku, wskaźnik na początku
    - w - pisanie, nadpisuje istniejący plik, tworzy nowy plik jak nie ma
    - a - dodawanie, wskaźnik na końcu pliku, tworzy nowy plik jak nie ma
    - r+ - czytanie/pisanie, wskaźnik na początku, FileNotFoundError jak nie ma pliku, nie usuwa calej zawartosci pliku
    - w+ - czytanie/pisanie, czysci zawartosc istniejacego pliku juz przy jego otwarciu, tworzy nowy plik jak nie ma
    - a+ - czytanie/dodawanie, wskaźnik na końcu pliku, tworzy nowy plik jak nie ma
    - rb, rb+, wb, wb+, ab, ab+ - analogicznie, ale w trybie binarnym

- wykonujemy operacje (zapis, odczyt)
- zamykamy plik - moze byc tak, ze jak nie zamkniecie pliku, to pozniej inny program nie bedzie w stanie z niego skorzystac
"""


file_handle = open('day_4_pgg/test.txt')
content = file_handle.read()
print(content)
file_handle.close()

print('-' * 60)

file_handle = open('day_4_pgg/test.txt', 'w+')  # tryb do zapisu
file_handle.write('Ala ma kota\nKot ma kompilator')
file_handle.close()

print('-' * 60)

"""
zeby nie trzeba bylo pamietac o zamykaniu pliku mozemy wykorzystac compound statement
takie samo rozwiazanie mozemy zastowac nie tylko do plikwo, ale takze do innych zasobow
np. requesty do API, zasoby sieciowe, itp.
"""

with open('day_4_pgg/test.txt', 'r+', encoding='utf-8') as file_handle:
    content = file_handle.read()
    print(content)
    print(file_handle.closed)  # False
    print(file_handle.encoding)  # UTF-8
    print(file_handle.mode)  # r+
    print(file_handle.name)  # day_4_pgg/test.txt
    print(file_handle.writable())  # True
    print(file_handle.readable())  # True

print(file_handle.closed)  # True

print('Jestem poza with')

print('-' * 60)

with open('day_4_pgg/test.txt', 'r+', encoding='utf-8') as file_handle:
    # jak mozemy odczytywac dane z pliku
    content = file_handle.read()  # trzeba uwazac na wczytywanie duzych plikow
    print(content)

    print('---')

    file_handle.seek(0)  # 1 - czytamy od drugiego znaku z pliku
    content = file_handle.read()  # trzeba uwazac na wczytywanie duzych plikow
    print(content)

    print('---')

    file_handle.seek(0)
    content = file_handle.read(10)
    print(content)
    content = file_handle.read(10)
    print(content)

    print('---')

    file_handle.seek(0)
    content = file_handle.read(10)
    print(content)

    print('---')

    file_handle.seek(0)
    content = file_handle.readline()  # "Ala ma kota\n" - znak \n jest rowniez dolaczany
    print(content)
    content = file_handle.readline()
    print(content)

    print('---')

    file_handle.seek(0)
    content = file_handle.readline().rstrip('\n')  # usuniecie znaku nowej linii z konca wczytanej linii
    print(content)
    content = file_handle.readline()
    print(content)

print('---')

# obrabianie duzych plikow
with open('day_4_pgg/test.txt', 'r+', encoding='utf-8') as file_handle:
    for line in file_handle:
        print(line)


print('---')

with open('day_4_pgg/test.txt', 'r+', encoding='utf-8') as file_handle:
    list_of_lines = list(file_handle)
    print(list_of_lines)

