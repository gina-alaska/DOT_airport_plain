#! /usr/bin/env python3
#
# Compare LIDAR point data to a plane and write out all points above the plane surface.
# GINA - 05/19/2020
#
# For this script to work you need the following python modules loaded via pip
# pylas
# lazrs
#
# This script supports both .las and .laz (if lazrs is installed) file formats. Las file formats 1.2, 1.3, and 1.4
# are supported.
#

# Import modules
import pylas                      # pylas module for reading and writing las files
import csv                        # csv module to read csv files
import numpy as np                # numpy for math operations
import argparse                   # argparse to get command line parameters/options
import os                         # os check to see if files exist
import math                       # math for sqrt function

# Import functions
import las_plane_func as laspf    # import script functions

# Parse command line
parser = argparse.ArgumentParser()
parser.add_argument("las_file", help="LAS file to load (.las/.laz)")      # las file to load
parser.add_argument("plane_file", help="CSV file with plane data")        # csv file with plane point data
parser.add_argument("threshold", help="Threshold over the plane")         # csv file with plane point data
args = parser.parse_args()                                                # parse

threshold = args.threshold                                                # get threshold from command line

# Load plane csv file if it exists
if not os.path.exists(args.plane_file):
  print("The CSV file " + args.plane_file + " can not be found!")
  exit(1)

csvfile = open(args.plane_file)
csv_data = csv.DictReader(csvfile)                                        # CSV reader object

# Load las/laz file if it exists
if not os.path.exists(args.las_file):
  print("The LAS file " + args.las_file + " can not be found!")
  exit(1)

las_data = pylas.read(args.las_file)

# Access las file header
las_header = las_data.header

# Output las file information
print()
print("LAS file: " + args.las_file)
print("Creation date: " + str(las_header.date))
print("Software used: " + str(las_header.generating_software))
print("Number of points: " + str(las_header.point_count))
print("Min Values: " + str(las_header.mins))
print("Max Values: " + str(las_header.maxs))
print()

# Get some stats
max_z = las_header.z_max

# Assign LAS data to numpy arrays
las_x = np.array(las_data.x)
las_y = np.array(las_data.y)
las_z = np.array(las_data.z)

# Process LAS data
for row in csv_data:                                         # Process each plane in the plane file
  # Get all of the plane data from CSV file
  name = row['Name']
  point1 = laspf.convert_xyz(row['Point1'])                  # Get the first defined point of the plane
  point2 = laspf.convert_xyz(row['Point2'])                  # Get the second defined point of the plane
  point3 = laspf.convert_xyz(row['Point3'])                  # Get the third defined point of the plane

  if point1[2]>max_z and point2[2]>max_z and point3[2]>max_z:
    print("The highest point in the file is lower than all of the plane points!")

  # Calculate plane equation
  equation = laspf.equation_plane(point1, point2, point3)
  e = (math.sqrt(equation[0] * equation[0] + equation[1] * equation[1] + equation[2] * equation[2]))

  print("\nProcessing " + name + " ...", end="", flush=True)

  d = (equation[0] * las_x + equation[1] * las_y + equation[2] * las_z + equation[3])
  distances = d / e

  if equation[0]<0 and equation[1]<0 and equation[2]<0:
    dist_ind = np.where(distances < 0)
  else:
    dist_ind = np.where(distances > 0)

  for x in range(10):
    print(distances[dist_ind[0][x]])

  # Check for no high points
  if not dist_ind:
    print("There are no points above the plane " + name)
    continue

  # Gather data for output las file
  out_x = las_x[dist_ind[0]]
  out_y = las_y[dist_ind[0]]
  out_z = las_z[dist_ind[0]]

  las_out = pylas.create()
  las_out.x = out_x
  las_out.y = out_y
  las_out.z = out_z
  
  # Write .las file
  las_out.write(name + ".las")
  print("done")

# Close CSV file
csvfile.close()
