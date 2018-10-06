Root Insurance Kata
Michael D Weaver
4/23/2018

This is a short program designed to read a list of drivers and a record of each of their trips (with a start time, end time, and miles driven) from an input file, and write a line for each driver to an output file, with the driver's total miles driven and average speed, arranged by each driver's total miles (highest to lowest).

-------
classes
-------
Instances of both class Driver and Trip are initialized with values from the input file, (each driver's name, plus each trip's driver, start/end time, and distance) as well as properties that will be used for calculations and output. The class TextFiles is initialized with a filename for both the txt file to read and to write.


-------
functions
-------
read_input()
The first function called is read_input(), which reads input.txt, and appends each line in the file to a list, ip_lines.

get_drivers()
The list ip_lines is then passed as an argument to get_drivers(), the function which assembles data on drivers. For each list in ip_lines beginning with "Driver", a Driver object is created, the driver's name being the next item in that list. That object is then appended to driver_list.

get_trips()
Driver_list and ip_lines are then passed to get_trips(), which uses ip_lines to create an Trip object from each line beginning with "Trip" in input.txt.

get_duration()
The get_duration() function assigns a duration property to each Trip object by casting Trip.starting and Trip.ending as sets of integers. Since the duration will be used to calculate miles per hour, the function returns a duration expressed in number of hours (the number of minutes being divided by sixty and added to the number of hours).

In get_trips(), each trip's speed is calculated using Trip.miles and Trip.hours. If the speed falls within the range of 5 to 100 mph, the Trip object is then added to the corresponding Driver object by matching Driver.name with Trip.driver.

get_speed()
If a driver has any trips recorded, the driver's average speed is calculated using Trip.miles and Trip.hours from each object in Driver.trips, and passed back to get_drivers().

write_output()
Driver_list is passed to write_output(), which sorts the list according to each driver's number of miles. Each driver's total mileage and (if applicable) average speed are then converted to strings for file writing, and written to output.txt in the specified format.


-------
notes
-------
One of the first decisions I made was to create a class Driver and Trip, as those are the two basic categories of data from the input file. It also seemed obvious to take the values after "Driver" and "Trip" in the file and create corresponding parameters in the __init__ function for each class. The other properties (which were initialized as zero or an empty list) were based on the values that I thought I would need once the data had been processed and was ready to write.

Since this program was not very complex, I elected to include all the class and function definitions in a single .py file, along with the function calls to run the program.

I broke the process down into three basic steps...
1) Read from the input file
2) Process the data
3) Write to the output file
...and these correspond to the three function calls at the end, the result of each function being passed as an argument to the next.

The second step is by far the most involved, and rather than building out get_drivers() to an excessive length, I tried to split the functionality into logical steps, with a separate function for each step that passes a result back to get_drivers().

I tried to keep the numerical data in the most convenient format for calculations up until the last function formats it for file writing. For example, when parsing the trip start and end times, I decided to convert the duration in minutes to a floating decimal as a portion of hours, since that time will be used to calculate mph. Each driver's total miles and average speed are kept in decimal form until write_output(), where they are rounded to integers and converted to strings in the same line, for purposes of writing to the file.

One thing I changed after most of the program was finished was to pass arguments for filenames to read_input() and write_output(). I had originally hard-coded the filenames directly into the functions, but then I remembered I needed to run the same functions in both the program and the tests, and I thought it best to use a different file in the tests. I decided on creating a class named TextFiles, with properties for an input and output filename, which I felt would work much better if the program were ever modified or expanded.