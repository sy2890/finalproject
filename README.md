# TOOLS FOR ANALYTICS FINAL PROJECT
## Group Information
* Project Group 37, Section 2
* Contributors: Siyuan Ying, Guinan Xiang
* UNIs: [[sy2890](https://github.com/sy2890), [gx2143](https://github.com/Amber-Xiang)]         

## Description
This project contains two web applications, namely sightings and map.     
The web application SIGHTINGS can show the list including each squirrel's ID, add and edit squirrels' information, and it can also display some general statistics about squirrels.      
The web application MAP can visualize sightings of squirrels on the map around Central Park at NYC.       

## Dataset
Dataset for this project can be downloaded [here](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).
It comes from [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).        

## API links
* [Map](https://engaged-plasma-253100.appspot.com/map/)
* [Sightings](https://engaged-plasma-253100.appspot.com/sightings/)
* [Add squirrels](https://engaged-plasma-253100.appspot.com/sightings/add/)
* [Edit squirrels](https://engaged-plasma-253100.appspot.com/sightings/37F-PM-1014-03/)
* [Stats about squirrels](https://engaged-plasma-253100.appspot.com/sightings/stats/)     

## Management Commands
* Import     
A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
```
python manage.py import_squirrel_data /path/to/file.csv
```     
* Export      
A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.
```
python manage.py export_squirrel_data /path/to/file.csv
```



## Requirements
* Python 3.6
* Django 3.0

