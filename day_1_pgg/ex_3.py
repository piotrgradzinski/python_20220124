"""
Korzystając z operatora dostępu oraz wycinania wyświetl:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie)
- co trzeci element
- co drugi element licząc od końca
"""
#          0   1   2   3   4   5   6   7   8   9 - indeksy
#          -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 - indeksy ujemne
#          1   2   3   4   5   6   7   8   9   10 - ktory element?
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(numbers[1])
print(numbers[-2])
print(numbers[2:7])
print(numbers[::3])
print(numbers[::-2])
