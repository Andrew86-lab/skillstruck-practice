num1 = int(input("Give me a number: "))
num2 = int(input("Give me a number: "))

def smallest(first, second):
    if first < second:
        print(first)
    elif first > second:
        print(second)

smallest(num1, num2)