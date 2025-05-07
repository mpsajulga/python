key_word = "no"
print("hi")
input_keyword = str(input("Shall we continue? "))

while True:
    if input_keyword == key_word:
        print("okay then")
        break
    print("hi")
    input_keyword = str(input("Shall we continue? "))
