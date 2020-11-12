#!/usr/bin/env python3

import os

#In Linux and MacOS, the portions of a file are split using a forward slash (/)
#On Windows, they're splt using a backslash (\)
dir = "First_week"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
print(os.getcwd())

if os.path.exists("Test_dir"):
    os.rmdir("Test_dir")
os.mkdir("Test_dir")
os.chdir("Test_dir")
print(os.getcwd())
