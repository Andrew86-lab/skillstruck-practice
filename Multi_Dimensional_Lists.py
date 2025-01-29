# rows = 5
# cols = 3
# list = [
    
# ]

# for i in range(rows):
#     var1 = [
        
#     ]
#     for j in range(cols):
#         var1.append(5)
#     list.append(var1)

# print(list)

# fruits = ["apple", "grape", "peach", "cinnamon", "vanilla"]

# rows = [items.strip() for items in input("Inout a list of fruits").split()]

# list = [[(i + " " + j) for j in fruits] for i in rows]

# print(list)

cols = ["apple", "grape", "peach", "cinnamo", "vanilla"]
rows = [items.strip() for items in input("Inout a list of fruits").split()]
list = []
for i in rows:
    col = []
    for j in cols:
        col.append(i)
    list.append(col)
print(list)