#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Commander Lambda loves efficiency and hates anything that wastes time. The Commander is a busy lamb, after all! Henchmen who identify sources of inefficiency and come up with ways to remove them are generously rewarded. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other -- one at a time -- before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show the Commander how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloiluiz@gmail.com"
__version__ = "1.0.2"
__status__ = "Production"


# Enable the debug options
DEBUG = True


def solution(s):
    """ Decodes the input string and counts the number of salutes.
    """
    from sets import Set

    salute_number = 0
    has_employee = True
    hall_length = len(s)

    if (DEBUG == True):
        print("Hall: " + s)

    # Check for a valid string size
    if ((hall_length <= 0) or (hall_length > 100)):
        return salute_number

    # Check if string only has valid characters
    allowed_chars = Set("-<>")
    if (Set(s).issubset(allowed_chars) == False):
        return salute_number

    # Iterate over the input string
    s = list(s)
    while (has_employee == True):
        has_employee = False
        i = 0
        while (i < hall_length):

            if (DEBUG == True):
                print("Hall[" + str(i).zfill(2) + "]: " + "".join(s))
                print("salute_number: " + str(salute_number) + "\n")

            # Check if the hall spot is empty
            if (s[i] == "-"):
                i += 1
                continue

            # Check for employee
            if (s[i] == "<"):
                # Check if is the end of the hall
                if (i == 0):
                    s[i] = "-"
                # Otherwise, check for crossings and update position
                else:
                    has_employee = True
                    # Don't move the the space in front is blocked
                    if (s[i - 1] == "<"):
                        i += 1
                        continue
                    # Process the situation when the employee comes across someone in the opposite direction
                    elif (s[i - 1] == ">"):
                        salute_number += 2
                        s[i] = ">"
                    else:
                        s[i] = "-"

                    s[i - 1] = "<"

            elif (s[i] == ">"):
                # Check if is the end of the hall
                if (i == (hall_length - 1)):
                    s[i] = "-"
                # Otherwise, check for crossings and update position
                else:
                    has_employee = True
                    # Don't move the the space in front is blocked
                    if (s[i + 1] == ">"):
                        i += 1
                        continue
                    # Process the situation when the employee comes across someone in the opposite direction
                    if (s[i + 1] == "<"):
                        salute_number += 2
                        s[i] = "<"
                    else:
                        s[i] = "-"

                    s[i + 1] = ">"
                    i += 1

            i += 1

    return salute_number


def test():
    """ Application test function
    """
    input = "\0"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = ""
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "a"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = ">----<"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "<<>><"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")

    input = "--->-><-><-->-"
    print("Input: " + input)
    print("Output: " + str(solution(input)))
    print("============================================")


# Application entry point
if __name__ == "__main__":
    test()
