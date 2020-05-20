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

# Import functions
import las_plane_func as laspf    # import script functions

# Parse command line
parser = argparse.ArgumentParser()
parser.add_argument("las_file", help="LAS file to load (.las/.laz)")      # las file to load
parser.add_argument("plane_file", help="CSV file with plane data")        # csv file with plane point data
args = parser.parse_args()                                                # parse

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
print()

# Process LAS data
for row in csv_data:                                         # Process each plane in the plane file
  # Get all of the plane data from CSV file
  name = row['Name']
  point1 = laspf.convert_xyz(row['Point1'])                  # Get the first defined point of the plane
  point2 = laspf.convert_xyz(row['Point2'])                  # Get the second defined point of the plane
  point3 = laspf.convert_xyz(row['Point3'])                  # Get the third defined point of the plane
  print(point1, point2, point3)

  # Calculate plane equation
  equation = laspf.equation_plane(point1, point2, point3)

# Close CSV file
csvfile.close()
