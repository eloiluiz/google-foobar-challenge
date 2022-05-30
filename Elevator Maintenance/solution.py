#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on.

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloiluiz@gmail.com"
__version__ = "1.0.0"
__status__ = "Production"


# Enable the debug options
DEBUG = True


def solution(l):
    """Sorts the input list of version numbers.
    """
    import re

    sorted_list = list()
    pattern = "^\d+(\.\d+)*$"

    # Check if the input object is a list
    if (not isinstance(l, list)):
        if (DEBUG == True):
            print("Not a list")
        return sorted_list

    # Check for a valid list size
    if ((len(l) <= 0) or (len(l) > 100)):
        if (DEBUG == True):
            print("Invalid length")
        return sorted_list

    # Check if the content are only strings
    if (not all(isinstance(s, str) for s in l)):
        if (DEBUG == True):
            print("Invalid data type")
        return sorted_list

    # Check if the string is compliant with the defined pattern
    if (not all(re.match(pattern, s) for s in l)):
        if (DEBUG == True):
            print("Invalid string pattern")
        return sorted_list

    # Then, start the sorting process
    # Start parsing splitting the input list to integer values
    sorted_list = []
    for s in l:
        element = [int(x) for x in s.split(".")]
        element.insert(0, s)
        sorted_list.append(element)

    # Then, sort the list using the version number integer values
    version_sort(sorted_list)

    # Lastly, return the sorted list
    return [row[0] for row in sorted_list]


def version_sort(array):
    """Sorting function based on the Bubble Sort approach.

    This function performs the sorting of the input array taking as a reference the columns of its composition. The
    scanning method used is based on the Bubble Sort algorithm.
    """
    # Iterate over the input array
    for i in range(len(array)):
        # Iterate over the unsorted elements
        for j in range(0, len(array) - i - 1):
            sort_decision(array, j, 1)


def sort_decision(array, row, column):
    """Performs the input array sorting based on the selection of row and column parameters.

    This function evaluates the selected row and its next row positions taking as reference the integer values of the
    selected column. If the one row element is bigger than the next, the row positions are swapped. If the elements are
    equal, the next column is referenced.
    """
    # First, make sure the selected column exists
    # If the first element column doesn't exist, nothing to do
    if (len(array[row]) <= column):
        return
    # If the second element length is smaller, swap the elements
    if (len(array[row + 1]) <= column):
        temp = array[row]
        array[row] = array[row + 1]
        array[row + 1] = temp
        return
    # Compare two adjacent elements
    if (array[row][column] > array[row + 1][column]):
        # Swap if the elements are not in the intended order
        temp = array[row]
        array[row] = array[row + 1]
        array[row + 1] = temp
    if (array[row][column] == array[row + 1][column]):
        sort_decision(array, row, column + 1)


def test():
    """ Application test function
    """
    pass_results = 0
    fail_results = 0
    # Define every test case for the application
    test_cases = [
        [
            ["\0"],
            []
        ],
        [
            1,
            []
        ],
        [
            [],
            []
        ],
        [
            ["1"],
            ["1"]
        ],
        [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            []
        ],
        [
            [1],
            []
        ],
        [
            ["1", 1],
            []
        ],
        [
            [""],
            []
        ],
        [
            ["1.0.0", "1", "1.0"],
            ["1", "1.0", "1.0.0"]
        ],
        [
            ["1,", "1.0", "1.0.0"],
            []
        ],
        [
            ["1", ".0", "1.0.0"],
            []
        ],
        [
            ["1", "1.0", "1.0."],
            []
        ],
        [
            ["a", "1.0", "1.0.0"],
            []
        ],
        [
            ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
            ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
        ],
        [
            ["5.1.2600", "6.0.6000", "6.0.6001", "6.0.6002", "6.1.7600", "6.1.7601", "6.2.9200", "6.3.9200", "6.3.9600", "10.0.10240", "10.0.10586", "10.0.14393",
                "10.0.15063", "10.0.16299", "10.0.17134", "10.0.17763", "10.0.18362", "10.0.18363", "10.0.19041", "10.0.19042", "10.0.19043", "10.0.19044", "10.0.22000"],
            ["5.1.2600", "6.0.6000", "6.0.6001", "6.0.6002", "6.1.7600", "6.1.7601", "6.2.9200", "6.3.9200", "6.3.9600", "10.0.10240", "10.0.10586", "10.0.14393",
                "10.0.15063", "10.0.16299", "10.0.17134", "10.0.17763", "10.0.18362", "10.0.18363", "10.0.19041", "10.0.19042", "10.0.19043", "10.0.19044", "10.0.22000"]
        ],
        [
            ["10.0.22000", "10.0.19044", "10.0.19043", "10.0.19042", "10.0.19041", "10.0.18363", "10.0.18362", "10.0.17763", "10.0.17134", "10.0.16299", "10.0.15063",
                "10.0.14393", "10.0.10586", "10.0.10240", "6.3.9600", "6.3.9200", "6.2.9200", "6.1.7601", "6.1.7600", "6.0.6002", "6.0.6001", "6.0.6000", "5.1.2600"],
            ["5.1.2600", "6.0.6000", "6.0.6001", "6.0.6002", "6.1.7600", "6.1.7601", "6.2.9200", "6.3.9200", "6.3.9600", "10.0.10240", "10.0.10586", "10.0.14393",
                "10.0.15063", "10.0.16299", "10.0.17134", "10.0.17763", "10.0.18362", "10.0.18363", "10.0.19041", "10.0.19042", "10.0.19043", "10.0.19044", "10.0.22000"]
        ],
        [
            ["10.0.16299", "6.0.6002", "10.0.19042", "10.0.19041", "10.0.18363", "10.0.18362", "10.0.17763", "10.0.17134", "10.0.22000", "10.0.15063", "10.0.14393",
                "10.0.10586", "10.0.10240", "6.3.9600", "6.3.9200", "6.2.9200", "6.1.7601", "6.1.7600", "10.0.19044", "6.0.6001", "6.0.6000", "5.1.2600", "10.0.19043"],
            ["5.1.2600", "6.0.6000", "6.0.6001", "6.0.6002", "6.1.7600", "6.1.7601", "6.2.9200", "6.3.9200", "6.3.9600", "10.0.10240", "10.0.10586", "10.0.14393",
                "10.0.15063", "10.0.16299", "10.0.17134", "10.0.17763", "10.0.18362", "10.0.18363", "10.0.19041", "10.0.19042", "10.0.19043", "10.0.19044", "10.0.22000"]
        ],
        [
            ["1.0", "1.1", "1.5", "1.6", "2.0", "2.0.1", "2.1", "2.2", "2.2.3", "2.3", "2.3.2", "2.3.3", "2.3.7", "3.0", "3.1", "3.2", "3.2.6", "4.0", "4.0.2", "4.0.3", "4.0.4", "4.1", "4.1.2",
                "4.2", "4.2.2", "4.3", "4.3.1", "4.4", "4.4.4", "4.5", "4.5.2", "5.0", "5.0.2", "5.1", "5.1.1", "6.0", "6.0.1", "7.0", "7.1", "7.1.2", "8.0", "8.1", "9", "10", "11", "12", "12.1", "13"],
            ["1.0", "1.1", "1.5", "1.6", "2.0", "2.0.1", "2.1", "2.2", "2.2.3", "2.3", "2.3.2", "2.3.3", "2.3.7", "3.0", "3.1", "3.2", "3.2.6", "4.0", "4.0.2", "4.0.3", "4.0.4", "4.1", "4.1.2",
                "4.2", "4.2.2", "4.3", "4.3.1", "4.4", "4.4.4", "4.5", "4.5.2", "5.0", "5.0.2", "5.1", "5.1.1", "6.0", "6.0.1", "7.0", "7.1", "7.1.2", "8.0", "8.1", "9", "10", "11", "12", "12.1", "13"]
        ],
        [
            ["13", "12.1", "12", "11", "10", "9", "8.1", "8.0", "7.1.2", "7.1", "7.0", "6.0.1", "6.0", "5.1.1", "5.1", "5.0.2", "5.0", "4.5.2", "4.5", "4.4.4", "4.4", "4.3.1", "4.3", "4.2.2", "4.2",
                "4.1.2", "4.1", "4.0.4", "4.0.3", "4.0.2", "4.0", "3.2.6", "3.2", "3.1", "3.0", "2.3.7", "2.3.3", "2.3.2", "2.3", "2.2.3", "2.2", "2.1", "2.0.1", "2.0", "1.6", "1.5", "1.1", "1.0"],
            ["1.0", "1.1", "1.5", "1.6", "2.0", "2.0.1", "2.1", "2.2", "2.2.3", "2.3", "2.3.2", "2.3.3", "2.3.7", "3.0", "3.1", "3.2", "3.2.6", "4.0", "4.0.2", "4.0.3", "4.0.4", "4.1", "4.1.2",
                "4.2", "4.2.2", "4.3", "4.3.1", "4.4", "4.4.4", "4.5", "4.5.2", "5.0", "5.0.2", "5.1", "5.1.1", "6.0", "6.0.1", "7.0", "7.1", "7.1.2", "8.0", "8.1", "9", "10", "11", "12", "12.1", "13"]
        ],
        [
            ["2.2", "3.1", "2.0", "4.0.4", "12.1", "1.0", "1.6", "5.1", "2.3.7", "2.3", "3.2", "8.1", "2.0.1", "4.2.2", "2.1", "1.5", "4.5.2", "4.1", "6.0", "4.3.1", "2.3.2", "4.0.3", "13", "2.2.3",
                "1.1", "7.1", "4.0.2", "4.2", "3.0", "12", "4.4", "10", "5.0", "2.3.0", "4.4.4", "9", "7.1.2", "6.0.1", "4.1.2", "5.1.1", "4.0", "4.3", "4.5", "8.0", "11", "3.2.6", "2.3.3", "7.0", "5.0.2"],
            ["1.0", "1.1", "1.5", "1.6", "2.0", "2.0.1", "2.1", "2.2", "2.2.3", "2.3", "2.3.0", "2.3.2", "2.3.3", "2.3.7", "3.0", "3.1", "3.2", "3.2.6", "4.0", "4.0.2", "4.0.3", "4.0.4", "4.1", "4.1.2",
                "4.2", "4.2.2", "4.3", "4.3.1", "4.4", "4.4.4", "4.5", "4.5.2", "5.0", "5.0.2", "5.1", "5.1.1", "6.0", "6.0.1", "7.0", "7.1", "7.1.2", "8.0", "8.1", "9", "10", "11", "12", "12.1", "13"]
        ],
    ]

    # Run every test case
    for test in test_cases:
        # Print the input array
        print("Input: " + str(test[0]))
        result = solution(test[0])
        # Print the output array
        print("Output: " + str(result))
        # Print the test result
        if (result == test[1]):
            pass_results += 1
            print(u"Test: \033[1;32m PASSED\u001b[0m")
        else:
            fail_results += 1
            print(u"Test: \u001b[31mFAILED\u001b[0m")
        print("============================================")
    # Print the test summary
    print(u"Test Results: \033[1;32m" + str(pass_results) +
          u" PASSED\u001b[0m and \u001b[31m" + str(fail_results) + u" FAILED\u001b[0m.")


# Application entry point
if __name__ == "__main__":
    test()
