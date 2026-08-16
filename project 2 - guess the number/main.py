import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a!=n):
    guesses += 1
    a = int(input("Guesss the number : "))
    if(a>n):
        print("Lower number please")

    else: 
        print("Higher number please")    


print(f"You have gussed the number {n} correctly in {guesses} attempt")

