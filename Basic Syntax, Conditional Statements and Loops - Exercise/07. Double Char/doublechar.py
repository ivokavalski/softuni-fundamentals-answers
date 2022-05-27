while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    output = ""

    for i in command:
        output += i*2
    
    print(output)

