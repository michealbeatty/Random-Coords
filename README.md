Small program used to generate random coordinate points in the 
contiguous United States and then write them to a CSV file.
Program also reverse geocodes the latitude, longitude to retrieve an address if one is available

This program uses Python 2.7

Dependencies
------------
[geocoder](https://github.com/DenisCarriere/geocoder)


Usage
-----

### Running the program
`$ python randomCoords.py number_of_points output_file`

It is recommended that you limit the number of points to no more than ten at 
any one time otherwise you may run up against the limits set by Google.

Because this program appends results to the specified file, the user will be 
prompted to proceed if the specified output file already exists.

### Output format
The points are written to the CSV file in the following format

`longitude, latitude, address`

(see example.csv provided in the repository)

TODO
====

* Add the option to generate Canadian points.

