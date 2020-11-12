#! /usr/bin/env python3

#Command-line arguments are parameters that are passed to a program when it's started

import sys
import os

print(sys.argv)

#The exit status is the value returned by a program to the shell
my_number = input("Please Enter a number: \n")
print(my_number)
eval(my_number)
print(my_number)
#Echo $? shows us the result of a program. 
#When a Python program ends, it returns an zero if everything is ok. Another value if not

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else: 
    print("Error, the file {} alredy exists!".format(filename))
    sys.exit(1)
