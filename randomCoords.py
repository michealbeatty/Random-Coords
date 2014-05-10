#! /usr/bin/env python

"""US Geographic Information

Northernmost - (49.384472, -95.153389)
Southernmost - (24.433333, -81.918333)
Easternmost - (44.815278. -65.949722)
Westernmost - (48.164167. -124.733056)
Geographic Center - (39.833333. -98.583333)
"""
import random
import os
from geopy.geocoders import GoogleV3
#import geocoder

northernmost = 49.
southernmost = 25.
easternmost = -66.
westernmost = -124.
geolocator = GoogleV3()

fullstring = '{0}, {1}, "{2}", \n'


def coordinate_generator(number_of_points, output_file):
    """Takes an int number_of_points and generates an equivalent number of random coordinate points, geocodes them
     then writes them to the given output_file."""
    counter = 0
    while counter < number_of_points:
        #This generates a random coordinate based on the most extreme points in the contiguous United States
        latlng = round(random.uniform(southernmost, northernmost), 6), round(random.uniform(easternmost, westernmost),
                                                                             6)
        try:
            #This reverse geocodes the random coordinate
            address, (lat, lng) = geolocator.reverse(latlng, exactly_one=True)
            # TODO: Allow ability to include Canada
            if 'USA' not in address:  # We only want USA addresses
                continue
            else:
                counter += 1
                output_file.write(fullstring.format(lng, lat, address))
        except TypeError: # This checks for geocoding that returns NoneType
            continue


fname = input("Filename: ")
if os.path.isfile(fname):
    proceed_prompt = input("File exists, proceed(y or n)? ")
    if proceed_prompt.lower() == 'y':
        fout = open(fname, 'a')
        number_of_points = int(input("Number of points to generate: "))
        coordinate_generator(number_of_points, fout)
        fout.close()
    else:
        print('Aborting . . .')
        exit()
else:
    fout = open(fname, 'a')
    number_of_points = int(input("Number of points to generate: "))
    coordinate_generator(number_of_points, fout)
    fout.close()

#TODO Check for existence of random_addresses.csv and warn before appending.
