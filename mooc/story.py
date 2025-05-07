words = []
previous_word = 'none'

while True:
    word = input(str("Please type in a word: "))
       
    if word == 'end' or word == previous_word:
        break
    words.append(word)
    previous_word = word  
        
print(*words)