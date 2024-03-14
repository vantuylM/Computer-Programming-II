
def circumference(pi, Radius):
  circ = (2 * pi)*(Radius)
  return circ
def Area(pi, Radius):
  area = (pi) * (Radius * Radius)
  return area



def main():
  Radius = float(input("Enter Radius: "))
  pi = 3.141
  circ = circumference(pi, Radius)
  area = Area(pi, Radius)
  area = round(area)
  circ = round(circ)
  
  print("Circumference: ", str(circ))
  print("Area: ", str(area))
  pass


if __name__ == "__main__":
  main()

