# Functions for the las_plain.py script
# GINA 05192020
#

# import modules
import math

# Pull out xyz values from CSV file
def convert_xyz(point):
  points = point.split(" ")

  return [float(points[0]), float(points[1]), float(points[2])]

# Function to find equation of plane (aX + bY + cZ + d = 0)
# returns a, b, c, d
def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3):  
  equation = []
      
  a1 = x2 - x1 
  b1 = y2 - y1 
  c1 = z2 - z1 
  a2 = x3 - x1 
  b2 = y3 - y1 
  c2 = z3 - z1 
  equation[0] = b1 * c2 - b2 * c1 
  equation[1] = a2 * c1 - a1 * c2 
  equation[2] = a1 * b2 - b1 * a2 
  equation[3] = (- a * x1 - b * y1 - c * z1) 
  print ("equation of plane is ", equation[0], "x +", equation[1], "y +", equation[2], "z +", equation[3], "= 0.")

  return equation

# Function to find distance 
def shortest_distance(x1, y1, z1, equation):  
      
  #d = abs((a * x1 + b * y1 + c * z1 + d))   
  d = ((equation[0] * x1 + equation[1] * y1 + equation[2] * z1 + equation[3]))
  e = (math.sqrt(equation[0] * equation[0] + equation[1] * equation[1] + equation[2] * equation[2]))
  distance = d / e
  print("Perpendicular distance is", distance)
  if distance > 0:
    print("point is above the plane")
  if distance < 0:
    print("point is below the plane")
  if distance == 0:
    print("point is on the plane")

  return distance
