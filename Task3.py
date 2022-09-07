import random

user_word = input("Please, enter a word: ")
x = 0
while x < 5:
    answer = "".join(random.choices(user_word, k = len(user_word) ))
    print(answer)
    x += 1



