circle = int(input("Give me a radius of a circle: "))

def area(num):
    total = num * num * 3.14159
    print(total.__round__(1))

area(circle)