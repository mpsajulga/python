from math import sqrt

number_ask = int(input("Please type in a number: "))

while True:
    if number_ask == 0:
        print("Exiting...")
        break
    elif number_ask < 0:
        print("Invalid number")
    else:
        print(sqrt(number_ask))
    number_ask = int(input("Please type in a number: "))