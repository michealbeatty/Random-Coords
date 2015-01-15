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
import geocoder


#TODO create function to handle processing of generated coordinates

def coordinate_generator(number_of_points):
    northernmost = 49.
    southernmost = 25.
    easternmost = -66.
    westernmost = -124.

    coordinate_list = []


    fullstring = '{0}, {1}, "{2}", \n'
    #TODO refactor for separation of concerns This function should only generate coords

    counter = 0

    while counter < number_of_points:
        latlng = round(random.uniform(southernmost, northernmost), 6), round(random.uniform(easternmost, westernmost), 6)
        g = geocoder.reverse(latlng)
        if g.country != 'US':
            continue
        else:
            counter += 1
            coordinate_list.append(g.x, g.y, g.address)
            # output_file.write(fullstring.format(g.x, g.y, g.address))

    return coordinate_list
    print 'Finished generating %d coordinate points' % counter


def main():
    #TODO: main function should handle the actual writing to file
    fname = raw_input("Filename: ")
    if os.path.isfile(fname):
        proceed_prompt = raw_input("File exists, proceed(y or n)? ")
        if proceed_prompt.lower() == 'y':
            fout = open(fname, 'a')
            number_of_points = int(raw_input("Number of points to generate: "))
            coordinate_generator(number_of_points, fout)
            fout.close()
        else:
            print 'Aborting . . .'
            exit()
    else:
        fout = open(fname, 'a')
        number_of_points = int(raw_input("Number of points to generate: "))
        coordinate_generator(number_of_points, fout)
        fout.close()


#TODO Add command line arguments for filename and number of locations

if __name__ == '__main__':
    main()
