#limit = 10
limit = int(input("Limit: "))
number = 1
result = 1
print_out = "The consecutive sum: 1"
while limit > result:
    
    number += 1
    
    result += number
    print_out += f" + {number}"
    
print(print_out, " = ", result)
