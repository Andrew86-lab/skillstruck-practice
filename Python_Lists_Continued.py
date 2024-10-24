my_list = [int(n) for n in input("Give me a list of numbers: ").split()]

counter = 0

for x in range(0, len(my_list) -1):
    if my_list[x] > my_list[x -1] and my_list[x] > my_list[x +1]:
        counter += 1

print(counter)