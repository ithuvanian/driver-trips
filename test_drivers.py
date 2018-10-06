"""Unit tests for drivers.py."""

import unittest
from drivers import *


class ReadInputTestCase(unittest.TestCase):
    """Tests for drivers.read_input()."""

    def test_one_line(self):
        """Test reading a single line."""
        ip_text = 'Driver Adam'
        filename = 'test_drivers.txt'

        with open(filename, 'w') as txt:
            txt.write(ip_text)
        line = [['Driver', 'Adam']]

        result = read_input(filename)
        self.assertEqual(result, line)


    def test_multiple_lines(self):
        """Test reading multiple lines."""
        ip_list = [['Driver', 'Tricia'], ['Trip', 'Tricia', '07:22', '08:32', '22.8']]
        filename = 'test_drivers.txt'

        with open(filename, 'w') as txt:
            for line in ip_list:
                for index in line:
                    txt.write(index + ' ')
                txt.write('\n')

        result = read_input(filename)
        self.assertEqual(result, ip_list)


class GetDriversTestCase(unittest.TestCase):
    """Tests for drivers.get_drivers()."""

    def test_get_drivers(self):
        """Test properties of Driver object."""
        ip_list = [['Driver', 'Pam'], ['Trip', 'Pam', '12:00', '13:00', '30']]

        driver_list = get_drivers(ip_list)
        self.assertEqual(driver_list[0].name, 'Pam')
        self.assertEqual(len(driver_list[0].trips), 1)
        self.assertEqual(driver_list[0].miles, 30)
        self.assertEqual(driver_list[0].hours, 1)
        self.assertEqual(driver_list[0].avg_speed, 30)


    def test_multiple_drivers(self):
        """Test with multiple drivers."""
        ip_list = [
            ['Driver', 'Pam'],
            ['Trip', 'Pam', '12:00', '13:00', '30'],
            ['Driver', 'Joe'],
            ['Trip', 'Joe', '05:00', '07:00', '88']
        ]
        driver_list = get_drivers(ip_list)
        self.assertEqual(driver_list[0].name, 'Pam')
        self.assertEqual(len(driver_list[0].trips), 1)
        self.assertEqual(driver_list[0].miles, 30)
        self.assertEqual(driver_list[0].hours, 1)
        self.assertEqual(driver_list[0].avg_speed, 30)
        self.assertEqual(driver_list[1].name, 'Joe')
        self.assertEqual(len(driver_list[1].trips), 1)
        self.assertEqual(driver_list[1].miles, 88)
        self.assertEqual(driver_list[1].hours, 2)
        self.assertEqual(driver_list[1].avg_speed, 44)


    def test_multiple_trips(self):
        """Test driver with multiple trips."""
        ip_list = [
            ['Driver', 'Pam'],
            ['Trip', 'Pam', '12:00', '13:00', '30'],
            ['Trip', 'Pam', '12:30', '15:00', '150']
        ]
        driver_list = get_drivers(ip_list)
        self.assertEqual(len(driver_list[0].trips), 2)
        self.assertEqual(driver_list[0].miles, 180)
        self.assertEqual(driver_list[0].hours, 3.5)
        self.assertEqual(round(driver_list[0].avg_speed, 4), 51.4286)


    def test_discarded_trips(self):
        """Test driver with trips below 5mph and over 100mph."""
        ip_list = [
            ['Driver', 'Pam'],
            ['Trip', 'Pam', '12:00', '13:00', '4.9'],
            ['Trip', 'Pam', '12:00', '13:00', '100.1']
        ]
        driver_list = get_drivers(ip_list)
        self.assertEqual(len(driver_list[0].trips), 0)
        self.assertEqual(driver_list[0].miles, 0)
        self.assertEqual(driver_list[0].hours, 0)
        self.assertEqual(driver_list[0].avg_speed, 0)


class WriteOutputTestCase(unittest.TestCase):
    """Tests for drivers.write_output()."""

    def test_write_one_line(self):
        """Test writing one line to file."""
        driver_Greg = Driver('Greg')
        driver_Greg.miles = 80
        driver_Greg.avg_speed = 40
        driver_list = [driver_Greg]
        filename = 'test_drivers.txt'

        write_output(driver_list, filename)
        with open(filename) as txt:
            result = txt.read().rstrip()
        self.assertEqual(result, 'Greg: 80 miles @ 40 mph')


    def test_write_without_trips(self):
        """Test writing for a driver with no recorded trips."""
        driver_Greg = Driver('Greg')
        driver_Greg.miles = 0
        driver_Greg.avg_speed = 0
        driver_list = [driver_Greg]
        filename = 'test_drivers.txt'

        write_output(driver_list, filename)
        with open(filename) as txt:
            result = txt.read().rstrip()
        self.assertEqual(result, 'Greg: 0 miles')


    def test_write_multiple_lines(self):
        """Test writing multiple lines to file."""
        driver_Greg = Driver('Greg')
        driver_Greg.miles = 80
        driver_Greg.avg_speed = 40
        driver_Jen = Driver('Jen')
        driver_Jen.miles = 120
        driver_Jen.avg_speed = 55
        driver_list = [driver_Greg, driver_Jen]
        filename = 'test_drivers.txt'
        op_list = []

        write_output(driver_list, filename)
        with open(filename) as txt:
            for line in txt:
                op_list.append(line.rstrip())
        self.assertEqual(op_list, ['Jen: 120 miles @ 55 mph', 'Greg: 80 miles @ 40 mph'])


unittest.main()
