#limit = 10
limit = int(input("Limit: "))
number = 1
result = 1

while limit > result:
    number += 1
    result += number
    
print(result)