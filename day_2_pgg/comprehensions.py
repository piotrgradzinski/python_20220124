"""
Comprehensions
"""

# podejscie bez list comprehension
numbers = []
for number in range(0, 11):
    numbers.append(number * 10)

print(numbers)

# list comprehension
numbers = [number * 10 for number in range(0, 11)]
print(numbers)
print(type(numbers))

print('-' * 60)

# jak uwzglednic warunki
numbers = []
for number in range(0, 11):
    if number >= 5:
        if number % 2 == 0:
            numbers.append(number * 10)
        else:
            numbers.append(number * -1)

print(numbers)

numbers = [number * 10 if number % 2 == 0 else number * -1 for number in range(0, 11) if number >= 5]
print(numbers)


# set comprehensions
letters = {letter for letter in "Ala ma kota"}
print(letters)

# dict comprehensions
my_str = "Ala ma kota"
occurences = {letter: my_str.count(letter) for letter in my_str}
print(occurences)

