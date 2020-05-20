# very basic and draft -
# Detect points above or below a plane in order to see if they are obstructions
#
# 5/18/2020 (basic stuff here to see what works.)
# Troy Hicks
# 5/19/2020 I am handing this off to Jason Grimes at GINA from UAF to sort out an actual script.

# here is the nasic conceptual workflow:
# ***************************************
# First sort how to define a plane from 3 points
# then how to compute a distance from a point to that plane
# then be able to open and read a .las file, and output a .las file of
# points that are above the plane. (if the distance is positive it is above.)
#
#
# borrowed some code and edited to work:


# Python program to find equation of a plane  
# passing through given 3 points. 
  
# code copied from: https://www.geeksforgeeks.org/program-to-find-equation-of-a-plane-passing-through-3-points/
# edited to work with python3
  
# Function to find equation of plane (aX + bY + cZ + d = 0)
# returns a, b, c, d
def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3):  
      
    a1 = x2 - x1 
    b1 = y2 - y1 
    c1 = z2 - z1 
    a2 = x3 - x1 
    b2 = y3 - y1 
    c2 = z3 - z1 
    a = b1 * c2 - b2 * c1 
    b = a2 * c1 - a1 * c2 
    c = a1 * b2 - b1 * a2 
    d = (- a * x1 - b * y1 - c * z1) 
    print ("equation of plane is ", a, "x +", b, "y +", c, "z +", d, "= 0.")
    return a, b, c, d
# equation of plane is  26 x + 7 y + 9 z + 3 = 0 when using sample data [-1, 2, 1][0,-3, 2][1,1,-4]
  
# ****** here is where I would enter the 3 points of the plane ******
# 3 points in [x, y, z] order
point1 = [0, 0, 0]
point2 = [10,20, 1]
point3 = [-10,20,1]
# point1 = [-1, 2, 1]
# point2 = [0,-3, 2]
# point3 = [1,1,-4]

x1 = point1[0]
y1 = point1[1]
z1 = point1[2]
x2 = point2[0]
y2 = point2[1]
z2 = point2[2]
x3 = point3[0]
y3 = point3[1]
z3 = point3[2]
plane = equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3)
# save results of plane for later use
a = plane[0]
b = plane[1]
c = plane[2]
d = plane[3]


# -------------------------------------------------
#
# https://www.geeksforgeeks.org/distance-between-a-point-and-a-plane-in-3-d/?ref=lbp
 
# Python program to find the Perpendicular(shortest) 
# distance between a point and a Plane in 3 D. 
  
import math 
  
# Function to find distance 
def shortest_distance(x1, y1, z1, a, b, c, d):  
      
    #d = abs((a * x1 + b * y1 + c * z1 + d))   
    d = ((a * x1 + b * y1 + c * z1 + d))
    e = (math.sqrt(a * a + b * b + c * c))
    distance = d / e
    print("Perpendicular distance is", distance)
    if distance > 0:
        print("point is above the plane")
    if distance < 0:
        print("point is below the plane")
    if distance == 0:
        print("point is on the plane")
      
  
# ***** test a point that is in [x, y, z] mode
test_point = [0,-20, -2]
x1 = test_point[0]
y1 = test_point[1]
z1 = test_point[2]

  
# Function call 
shortest_distance(x1, y1, z1, a, b, c, d)


# Works very well this far. Maybe it should be using numpy arrays instead and dusing numpy methods for the math.
# which only matters if it is faster.
#
# next step is deal with actual lidar file.
# this is not in the hands of the amazing Jason Grimes.
# 5/19/2020
