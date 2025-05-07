first_word = str(input("Please type in the 1st word: "))
second_word = str(input("Please type in the 2nd word: "))

def second_word_last():
    print(f"{second_word} comes alphabetically last.")
def first_word_last():
    print(f"{first_word} comes alphabetically last.")
def equals():
    print("You gave the same word twice.")

if first_word<second_word:
    second_word_last()
elif first_word>second_word:
    first_word_last()
else:
    equals()
