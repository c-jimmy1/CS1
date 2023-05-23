import math

pi = math.pi
Area1 = pi*(5**2)
Area2 = pi*pow(32, 2)

out_string = "Area 1 = {0:.2f}".format(Area1)
print(out_string)
print("Area 2 = " + str(round(Area2, 2)))
