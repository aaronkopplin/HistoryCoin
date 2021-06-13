from Commands import commands

while True:
    command = input("> ")

    if command not in commands:
        print("command not recognized")
        continue


