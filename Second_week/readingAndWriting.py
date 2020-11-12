guests = open("guests.txt", "w")
initial_guests = ["Axel", "Jordana", "Mariana", "Bryan"]

for i in initial_guests:
    guests.write(i + "\n")
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

new_guests = ["Ulises", "Claudia", "Mike"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out = ["Ulises", "Bryan", "Axel"]
temp_list = []

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ["Jordana", "Claudia"]
checked_in = []

with open("guests.txt") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in.".format(check))
        else:
            print("{} is not checked in.".format(check))