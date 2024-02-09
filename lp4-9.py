import random
x = random.randint(1, 20)
b = int(input("Enter a number between 1 and 20: "))
if x == b:
  print("Computers number: ", x)
  print("your number: ", b)
  print("you win!")

else:
  print("computers number: ", x)
  print("your number: ", b)
  print("Better luck next time")