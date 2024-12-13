file = open("speech.txt", "r")

count = file.read()

print(len(count.split()))

file.close()