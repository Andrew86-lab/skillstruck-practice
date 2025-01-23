num = [int(n) for n in input("Give me the numbers for RGB 0-255: ").split()]

result = []

for element in num:
    result.append(hex(element)[2:].zfill(2))

print("#" + "".join(result))