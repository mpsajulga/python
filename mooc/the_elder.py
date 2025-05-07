print("Person 1:")
person_1_name = str(input("Name: "))
person_1_age = int(input("Age: "))
print("Person 2:")
person_2_name = str(input("Name: "))
person_2_age = int(input("Age: "))

def elder_1():
    print(f"The elder is {person_1_name}")

def elder_2():
    print(f"The elder is {person_2_name}")
def equal():
    print(f"{person_1_name} and {person_2_name} are the same age")

if person_1_age > person_2_age:
    elder_1()
elif person_1_age < person_2_age:
    elder_2()
else:
    equal()
