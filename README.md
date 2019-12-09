# TOOLS FOR ANALYTICS FINAL PROJECT
## Group Information
* Project Group 37, Section 2
* Contributors: Siyuan Ying, Guinan Xiang
* UNIs: [[sy2890](https://github.com/sy2890), [gx2143](https://github.com/Amber-Xiang)]         

## Description
The project is designed to track squirrels in Central Park at NYC.    
It is a web application project based on Django development.      
Users can see a list with each squirrel's ID, add and edit squirrels' information, and they can also get some general statistics about squirrels. Moreover, users can get the visualization of the map with sightings of squirrels around Central Park at NYC.       

## Dataset
Dataset for this project can be downloaded [here](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).
It comes from [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).         

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

## API links
* [Map](https://engaged-plasma-253100.appspot.com/map/)
* [Sightings](https://engaged-plasma-253100.appspot.com/sightings/)
* [Add squirrels](https://engaged-plasma-253100.appspot.com/sightings/add/)
* [Edit squirrels](https://engaged-plasma-253100.appspot.com/sightings/37F-PM-1014-03/)
* [Stats about squirrels](https://engaged-plasma-253100.appspot.com/sightings/stats/)        

## Requirements
* Python 3.6
* Django 3.0

