print("Please type in integer numbers. Type in 0 to finish.")

positive_count = 0
negative_count = 0
numbers = []
  
while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
    numbers.append(number)
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
            
total_sum = sum(numbers)
total_number_count = len(numbers)
total_mean = (total_sum/total_number_count)


print(f"Numbers typed in {(len(numbers))}")
print(f"The sum of the numbers is {total_sum}")
print(f"The mean of the numbers is {total_mean}")
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")
        
        