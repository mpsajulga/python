width_of_string = int(input("Width: "))
height_of_string = int(input("Height: "))
multiplied = width_of_string * "#"

while height_of_string > 0:
    print(multiplied)
    height_of_string -= 1