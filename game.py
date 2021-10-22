import random

name = input("Enter your name : ")
print(f"Hello {name} \nWelcome to Guessing Game !!! \nGuess the names of the fruits : ")
words = ["apple","lemon","banana","pineapple","strawberry","cherry","watermelon","grapes","oranges","mango"]
index = random.randint(0,len(words))
word = words[index]
indexes = random.sample(range(0,len(word)),3)
guesses = ""
for i in indexes:
    guesses += word[i]
chance = 10
play = "Yes"

def playagain():
    play = input("Do you want to play again Yes/No : ")
    if play == "Yes":
        global chance, word, guesses
        chance = 10
        index = random.randint(0, len(words))
        word = words[index]
        indexes = random.sample(range(0, len(word)), 3)
        guesses = "" 
        for i in indexes:
            guesses += word[i]
   

while play == "Yes":
    while chance > 0:
        won = True
        for ch in word:
            if ch in guesses:
                print(ch, end=" ")
            else:
                print("_", end=" ")
                won = False
        if won:
            print(f"\nCongratulations {name} !!!\nYou scored {chance * 10} ")
            playagain()
            break
        guess = input("\nGuess your Character :  ")
        guesses += guess

        if guess not in word:
            chance -= 1
            print(f"\nYour guess is wrong !!!\nYou have {chance} left ")

        if chance == 0:
            print("\nYou Lose !!! ")
            playagain()
            break

print("\nThank You for playing !!!")