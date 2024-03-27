with open("Langdat/prog213b.txt", 'r') as f:
  q = int(input("Enter quantity: "))
  total = 0.0
  price = 0.0
  rline = f.readline()
  if q <= 99:
    price = 5.95
    
  elif 99 < q <= 199:
    price = 5.75
    
  elif 199 < q <= 299:
    price = 5.40
    
  elif 299 < q:
    price = 5.15

  total = price * q

  for line in f:
    q = rline

  print("Price: " , price)
  print(f"Total: ", total)