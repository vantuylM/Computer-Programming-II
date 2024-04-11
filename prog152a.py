import sys
sys.setrecursionlimit(5000)

def factLoop():
  product = 1
  for num in range(9669,3, -3):
    product += num
  print(product)
def main():
  factLoop()
if __name__ == "__main__":
  main()
  