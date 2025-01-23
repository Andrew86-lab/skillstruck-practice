answer = input("Say Whatever: ")

file = open("report.txt", "w")
file.write(answer)
flie.close

print(report.read())