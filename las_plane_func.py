# Functions for the las_plane.py script
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
def equation_plane(point1, point2, point3):  
  equation = []
      
  a1 = point2[0] - point1[0] 
  b1 = point2[1] - point1[1] 
  c1 = point2[2] - point1[2] 
  a2 = point3[0] - point1[0] 
  b2 = point3[1] - point1[1] 
  c2 = point3[2] - point1[2] 
  equation.append(b1 * c2 - b2 * c1)
  equation.append(a2 * c1 - a1 * c2)
  equation.append(a1 * b2 - b1 * a2)
  equation.append((- equation[0] * point1[0] - equation[1] * point1[1] - equation[2] * point1[2]))
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
