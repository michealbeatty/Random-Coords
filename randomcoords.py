#!/usr/bin/env python

"""
Program to generate random coordinates in the contiguous UNited States.


This program will generate a user-specified number of random geographic
coordinates in the contiguous United States, reverse geocode them, then
write them to the specified file.

Example:
    $ python randomcoords.py number_of_points output_file

The following conventions were used to ensure the coordinates were in the
contiguous U.S.

US Geographic Information

Northernmost - (49.384472, -95.153389)
Southernmost - (24.433333, -81.918333)
Easternmost - (44.815278. -65.949722)
Westernmost - (48.164167. -124.733056)
Geographic Center - (39.833333. -98.583333)
"""


import argparse
import os
import random

from pygeocoder import Geocoder, GeocoderError

__version__ = '0.0.3'

NORTHERNMOST = 49.
SOUTHERNMOST = 25.
EASTERNMOST = -66.
WESTERNMOST = -124.

def coordinate_generator(number_of_points):
    """
    Generate a number of random geographical points and then geocode them.

    :param number_of_points: number of points to generate
    :type number_of_points: int
    :return: list of geographic point tuples

    """


    coordinate_list = []
    counter = 0

    while counter < number_of_points:
        lat = round(random.uniform(SOUTHERNMOST, NORTHERNMOST), 6)
        lng = round(random.uniform(EASTERNMOST, WESTERNMOST), 6)
        try:
            gcode = Geocoder.reverse_geocode(lat, lng)
            if "Canada" in gcode[0].data[0]['formatted_address']:
                continue
            else:
                counter += 1
            coordinate_list.append((gcode[0].coordinates, gcode[0].formatted_address))
            # output_file.write(fullstring.format(gcode.x, gcode.y, gcode.address))
        except GeocoderError:
            continue
    print 'Finished generating %d coordinate points' % counter
    return coordinate_list


def main(points, fname):
    """
    write list of coordinates to file

    :param points: number of points to generate
    :param fname: name of output file

    """
    fullstring = '{0}, {1}, "{2}", \n'
    coordinates = []
    if os.path.isfile(fname):
        proceed_message = "File {} exists, proceed(y or n)? "
        proceed_prompt = raw_input(proceed_message.format(fname))
        if proceed_prompt.lower() == 'y':
            fout = open(fname, 'a')
            number_of_points = points
            coordinates = coordinate_generator(number_of_points)
            # fout.close()
            for loc in coordinates:
                fout.write(fullstring.format(loc[0][1], loc[0][0], loc[1]))
        else:
            print 'Aborting . . .'
            exit()
    else:
        fout = open(fname, 'a')
        number_of_points = points
        coordinates = coordinate_generator(number_of_points)
        for loc in coordinates:
            fout.write(fullstring.format(loc[0][1], loc[0][0], loc[1]))
        fout.close()


if __name__ == '__main__':
    #pylint: disable=invalid-name
    parser = argparse.ArgumentParser()
    parser.add_argument("points", type=int, help="number of points to generate")
    parser.add_argument("fname", help="name of output file")
    args = parser.parse_args()

    main(args.points, args.fname)
