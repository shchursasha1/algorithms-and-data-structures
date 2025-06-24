with open("input.txt") as file:
    n = file.readline()
    counter = 0

    for line in file.readlines():
        line = [int(i) for i in line.split()]
        
        if line.count(1) == 1:
            counter += line.count(1)

print(counter)