with open("spider.txt") as file:
    for line in file:
        print(line)

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

#\n new line, \t tab