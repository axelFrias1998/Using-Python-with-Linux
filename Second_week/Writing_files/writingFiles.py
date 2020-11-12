with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

#If you open a file for writing and the file alredy exists, the old contents
#will be deleted as soon as the file is opened
#https://docs.python.org/3/library/functions.html#open