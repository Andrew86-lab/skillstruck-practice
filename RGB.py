RGB = [int(n) for n in input("Give me numbers for RGB 0-255: ").split()]

result = [

]

for element in RGB:
    result.append(hex(element)[2:])

print("#" + "".join(result))