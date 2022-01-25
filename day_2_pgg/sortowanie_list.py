"""
Sortowanie listy
https://docs.python.org/3/howto/sorting.html
"""

my_list = [-10, 2, 1, 0, 50, -100]

print(my_list)

my_list.sort()  # modyfikuje oryginalna liste, nie tworzy nowej
my_list.sort(reverse=True)

print(my_list)

print('-' * 60)

my_list2 = [-10, 2, 1, 0, 50, -100]
print(my_list2)
my_list3 = sorted(my_list2)
print(my_list2)
print(my_list3)
