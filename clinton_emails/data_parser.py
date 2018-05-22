
commands = []

with open("datafile", "r") as f:

    for line in f:
        command = {}
        line = line.split(" ")
        command["number"] = line[0]
        command["program"] = line[2]
        commands.append(command)

for item in commands:
    print(item["number"], item["program"])
