group = {
    "box1": 5,
    "box2": 2,
    "box3": 10,
    "box4": 3,
    "box5": int(input("Give the number: "))
}

total = 0

for key in group:
    total += 25*group.get(key)

print(total)