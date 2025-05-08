word = str(input("Please type in a word: "))
char = str(input("Please type in a character: "))

index = word.find(char)
length_word = len(word)
upper_limit = index+3
try:
    if char in word and length_word > upper_limit:
        print(f"{word[index:index+3]}")

    elif index < 0:
        quit


except IndexError:
    quit