master_pin_code = 4321
attempts = 0

def one_attempt():
    print("Correct! It only took you one single attempt!")
def multiple_attempts():
    print(f"Correct! It took you {attempts} attempts")
def wrong():
    print("Wrong")
    
while True:
    pin_code = int(input("PIN: "))
    attempts += 1
    if pin_code == master_pin_code:
        if attempts == 1:
            one_attempt()
            break
        else:
            multiple_attempts()
            break
    wrong()