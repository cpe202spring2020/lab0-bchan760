def weight_on_planets():
   # write your code here
   weight = float(input("What do you weigh on earth? "))
   mars = "On Mars you would weigh " + str(weight * 0.38) + " pounds.\n"
   jup = "On Jupiter you would weigh " + str(weight * 2.34) + " pounds."
   print("\n" + mars + jup)
   
   
if __name__ == '__main__':
   weight_on_planets()