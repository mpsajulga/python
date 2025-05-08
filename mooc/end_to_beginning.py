string = str(input("Please type in a string: "))
index = 0
limit = len(string)

if len(string) > 0:
    while limit != 0 :
        limit -= 1
        index -= 1
        print(string[index])

else:    
    print("The input string is empty.")