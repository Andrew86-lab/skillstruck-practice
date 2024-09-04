listed_beans = input("What bean do you like?: ").split()

if "lima" in listed_beans:
    listed_beans.remove("lima")

print(listed_beans)