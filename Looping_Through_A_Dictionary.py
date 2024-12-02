Amanda = int(input("How many will she bring: "))
Jane = int(input("How many will she bring: "))

group = {
    "Fred" : 12,
    "Jackson" : 15,
    "Sophie" : 20,
    "Amanda" : Amanda,
    "Jane" : Jane
}

total = 0

for x in group.values():
    total += x

print(total)