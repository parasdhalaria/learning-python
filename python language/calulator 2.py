import random
secret_number = random.randint(1, 20)
guess = int(input("Enter your guess: "))
if  guess == secret_number:
    print("congratulation you have guss correct number ")
else:
     print(f"soory.the secret number is {secret_number}")
           
 
   
            