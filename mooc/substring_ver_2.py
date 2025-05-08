string = str(input("Please type in a string: "))
index = -1
length_of_string = len(string)

while length_of_string > 0:
    print(string[index:])
    length_of_string -= 1
    index -= 1