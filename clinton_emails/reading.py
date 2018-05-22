
choice = input("Enter 1 to enter a name, enter 2 to retrieve Names")

if choice == str(1):
    name = input("What's your Name")
    title = input("What's your title")
    years = input("How long have you been here")

    with open("file_with_lines", "a") as f:
        f.write(name)
        f.write(",")
        f.write(title)
        f.write(",")
        f.write(years)
        f.write("\n")

if choice == str(2):
    usertype = input("Who do you want to find (Student, Teacher or Admin)")
    with open("file_with_lines", "r") as f:
        for line in f:
            line = line.split(",")
            if line[1] == usertype:
                print(line[0])
            else:
                print("Not Found")
