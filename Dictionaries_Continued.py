shopping = {

}

fruits1 = int(input("How many apples do you need: "))
fruits2 = int(input("How many bananas do you need: "))
fruits3 = int(input("How many strawberries do you need: "))

if fruits1 > 5:
    apple = fruits1 - 5
    shopping["apples"] = apple

if fruits2 > 7:
    bananas = fruits2 - 7
    shopping["bananas"] = bananas

if fruits3 > 3:
    strawberries = fruits3 - 3
    shopping["strawberries"] = strawberries

print(shopping)