#! /usr/bin/env python3

#I/O Streams are the basic mechanism for 
# performing input and output operations in your programs

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)