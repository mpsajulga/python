while True:
    string = str(input("Please type in a string: "))
    len_string = len(string)
    dash = "-"
    multiplied = len_string * dash

    if len_string != 0:    
        print(string)
        print(multiplied)
    
    else:
        break

