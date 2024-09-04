my_list = [int(n) for n in input("Give me a list of numbers: ").split()]
total = 1

for elements in my_list:
    total = total * elements

print(total)