# opening a file in read mode
file = open("myfile.txt", "r")

# reading the content of the file
file = open("myfile.txt", "r")
content = file.read()
print(content)
file.close() # Always close the file!

# reads a single line from the file
file = open("myfile.txt", "r")
line1 = file.readline()
print(line1)
file.close()

# writing to a file
file = open("newfile.txt", "w")
file.write("This is the first line.\n")
file.write("This is the second line.")
file.close()

# closing a file automatically using the with statement
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)