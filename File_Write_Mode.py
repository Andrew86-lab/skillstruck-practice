file = open("porcupine.txt.txt", "w")
file.write("In short, I love to code!")
file.close()

file = open("porcupine.txt.txt", "r")
print(file.read())