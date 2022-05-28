#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloiluiz@gmail.com"
__version__ = "0.1.0"
__status__ = "Development "

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


def test():
    """ Application test function
    """
    input = "\0"
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = 1
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = []
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1"])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                 "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
                 )
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                 "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                  "1"]
                 )
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list([1])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", 1])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list([""])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", "1.0", "1.0.0"])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1,", "1.0", "1.0.0"])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", ".0", "1.0.0"])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["1", "1.0", "1.0."])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    input = list(["a", "1.0", "1.0.0"])
    print("Input: " + str(input))
    print("Output: " + str(solution(input)))
    print("============================================")

    # input = ">----<"
    # print("Input: " + input)
    # print("Output: " + str(solution(input)))
    # print("============================================")

    # input = "<<>><"
    # print("Input: " + input)
    # print("Output: " + str(solution(input)))
    # print("============================================")

    # input = "--->-><-><-->-"
    # print("Input: " + input)
    # print("Output: " + str(solution(input)))
    # print("============================================")


# Application entry point
if __name__ == "__main__":
    test()
