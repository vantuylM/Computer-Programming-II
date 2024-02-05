eggs = int(input("Enter # of eggs"))
Dozens = eggs // 12
price = 0.0

if 0 < Dozens < 4:
  price = 0.50
elif 4 < Dozens < 6:
  price = 0.45
elif 6 < Dozens < 11:
  price = 0.40
elif Dozens > 11:
  price = 0.35

print("Cost is $" + str(price))