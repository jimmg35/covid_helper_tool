# Data conversion/visualization tool
Main program is under scripts folder.
Currently, it only supports the conversion of this csv:

csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv

convert daily aggregated confirmed cases to daily confirmed cases.
you can find the example output csv file in scripts folder

Notice
==========================================================
Be awared of the absolute path written inside the main.py,
for those who want to run this program on their own PC
please substitute it to relative path.

Future version
==========================================================
I will dev some function such as auto-graph-making, which can be 
designed based on different scales(county, province). 

for analysis & deep learning, I'm planing to cluster each county based on
the daily confirmed cases(time serires), using algorith such as SOM, to see 
if there exist some trend among counties or province.

