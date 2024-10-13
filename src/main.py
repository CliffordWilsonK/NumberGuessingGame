import random

number = random.randint(2, 99)
while True:
  try:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess > number:
      print('Too high!')
    elif guess < number:
      print("Too low!")
    elif guess == number:
      print("Congratulations 🎉! You guessed the number")
      break
  except ValueError:
     print("Please enter a valid number.")
   
  
  

  
  
  

  