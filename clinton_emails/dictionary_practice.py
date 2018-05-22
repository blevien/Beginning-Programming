phonebook = []

for x in range(3):

    person = {}
    name = input("What's your name: ")
    age = input("What's your age: ")
    dob = input("What's your date of birth: ")
    phone = input("What's your phone number: ")

    phonebook.append({"name": name, "age": age, "dob": dob, "phone": phone})



print(phonebook)
