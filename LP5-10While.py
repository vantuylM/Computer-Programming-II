num1 = int(input("Enter non negitive number: "))
num2 = int(input("Enter non negitive number: "))


while (num2 > 0):
  temp = num1 % num2
  num1 = num2
  num2 = temp

print(f"GCD is {num1}")