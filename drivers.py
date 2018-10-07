"""Process data on drivers from an input file, and write the results to an output file."""

class Driver():
    """Holds data on drivers from input.txt."""

    def __init__(self, name):
        """Initialize with name from input.txt- trips, miles, hours, and avg_speed are initialized for later use."""
        self.name = name
        self.trips = []
        self.miles = 0
        self.hours = 0
        self.avg_speed = 0


class Trip():
    """Holds data on trips from input.txt."""

    def __init__(self, driver, starting, ending, miles):
        """Initialize with driver, start time, end time, and miles from input.txt. The total trip duration will be assigned to hours."""
        self.driver = driver
        self.starting = starting
        self.ending = ending
        self.miles = miles
        self.hours = 0


class TextFiles():
    """Holds filenames for input and output text files."""

    def __init__(self, ip, op):
        """Initialize with values for input and output."""
        self.ip = ip
        self.op = op


def read_input(ip_file):
    """Read input file, create a list of lists from each line."""
    with open(ip_file) as ip:
        ip_lines = []
        for line in ip:
            line_data = line.split()
            ip_lines.append(line_data)
    return ip_lines


def get_duration(trip):
    """Return total time of each trip in hours."""
    start_hhmm = trip.starting.split(':')
    end_hhmm = trip.ending.split(':')
    hrs = int(end_hhmm[0]) - int(start_hhmm[0])
    m_hrs = (int(end_hhmm[1]) - int(start_hhmm[1])) / 60
    return hrs + m_hrs


def get_trips(driver_list, ip_lines):
    """Get data for each trip, and associate trips with drivers."""
    for line in ip_lines:
        if line[0] == 'Trip':
            trip = Trip(line[1], line[2], line[3], float(line[4]))
            trip.hours = get_duration(trip)

            for driver in driver_list:
                if trip.driver == driver.name:
                    trip_speed = trip.miles / trip.hours
                    if trip_speed >= 5 and trip_speed <= 100:
                        driver.trips.append(trip)
    return driver_list


def get_speed(driver_list):
    """Calculate speed for each driver, from total miles and total hours."""
    for driver in driver_list:
        for trip in driver.trips:
            driver.miles += trip.miles
            driver.hours += trip.hours
        if driver.hours > 0:
            driver.avg_speed = driver.miles / driver.hours
    return driver_list


def get_drivers(ip_lines):
    """Get data on drivers."""
    driver_list = []

    for line in ip_lines:
        if line[0] == 'Driver':
            new_driver = Driver(line[1])
            driver_list.append(new_driver)
    driver_list = get_trips(driver_list, ip_lines)
    driver_list = get_speed(driver_list)
    return driver_list


def write_output(driver_list, op_file):
    """Use list of drivers and corresponding data to write to output.txt."""
    sorted_drivers = sorted(driver_list, key=lambda x: x.miles, reverse=True)

    with open(op_file, 'w') as op:
        op.close()
    for driver in sorted_drivers:
        miles = str(int(round(driver.miles)))
        op_line = driver.name + ': ' + miles + ' miles'
        if driver.avg_speed > 0:
            speed = str(int(round(driver.avg_speed)))
            op_line += ' @ ' + speed + ' mph'
        with open(op_file, 'a') as op:
            op.write(op_line + '\n')


files = TextFiles('input.txt', 'output.txt')
ip_lines = read_input(files.ip)
driver_list = get_drivers(ip_lines)
write_output(driver_list, files.op)
