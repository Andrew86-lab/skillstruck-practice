user_number = int(input("Give me a number: "))

largest_value = user_number

while user_number > 0:
    user_number = int(input("Give me a number: "))
    if user_number > largest_value:
        largest_value = user_number
print(largest_value)