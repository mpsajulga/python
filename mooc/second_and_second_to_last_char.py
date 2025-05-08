string = str(input("Please type in a string: "))

positive_index = string[1]
negative_index = string[-2]

if positive_index == negative_index:
    print(f"The second and the second to last characters are {positive_index}")
else:
    print(f"The second and the second to last characters are different")
