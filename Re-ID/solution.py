#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme.

Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloi.filho@electrolux.com"
__version__ = "1.0.0"
__status__ = "Released"


class solution:
    """Static class designed to calculate a set of prime numbers and return selected ranges concatenated in string format.
    """

    # Configuration Parameters
    SOLUTION_INDEX_RANGE_START = 0
    SOLUTION_INDEX_RANGE_END = 10000
    PRIME_NUMBER_SEQUENCE_LENGTH = 5
    PRIME_NUMBER_STRING_LENGTH = SOLUTION_INDEX_RANGE_END + PRIME_NUMBER_SEQUENCE_LENGTH

    # Class Variables
    Initialized = False
    PrimeNumberString = ""

    def __init__(self):
        """solution class' initialization.

        This method initializes the solution class' static attributes "Initialized" and "PrimeNumberString", defining a concatenated string of prime numbers for executing the solution method.
        """
        solution.initialize_vector()

    @classmethod
    def initialize_vector(self):
        """solution class' static initialization method.

        This method initializes the solution class' static attributes "Initialized" and "PrimeNumberString", defining a concatenated string of prime numbers for executing the solution method.
        """
        # First, check if the initialization is necessary
        if (solution.Initialized == False):
            num = 1
            while (len(solution.PrimeNumberString) < solution.PRIME_NUMBER_STRING_LENGTH):
                  num += 1
                  # Identify if num is a prime number and append to the list
                  for i in range(2, num):
                      if (num % i) == 0:
                          break
                  else:
                      solution.PrimeNumberString += str(num)

            solution.Initialized = True

    @classmethod
    def solution(self, index):
        """Returns a sequence of characters located in the static string PrimeNumberString, starting from the input index.

        Args:
            index (int): Defines index of the first character that will compose the resulting sequence, located in the static string PrimeNumberString.

        Returns:
            str: the resultant string sequence.
        """
        if (solution.Initialized == False):
            solution.initialize_vector()

        # Check for input parameter errors
        if ((index < solution.SOLUTION_INDEX_RANGE_START) or (index > solution.SOLUTION_INDEX_RANGE_END)):
            return ""

        # Return the selected number sequence
        return solution.PrimeNumberString[index: index + solution.PRIME_NUMBER_SEQUENCE_LENGTH]


def test():
    """ Application test function
    """
    # With object creation
    test_object = solution()
    print(test_object.solution(solution.SOLUTION_INDEX_RANGE_START))
    print(test_object.solution(solution.SOLUTION_INDEX_RANGE_END))
    print(test_object.solution(solution.SOLUTION_INDEX_RANGE_START - 1))
    print(test_object.solution(solution.SOLUTION_INDEX_RANGE_END + 1))
    print(test_object.solution(0))
    print(test_object.solution(3))

    # Static execution
    print(solution.solution(solution.SOLUTION_INDEX_RANGE_START))
    print(solution.solution(solution.SOLUTION_INDEX_RANGE_END))
    print(solution.solution(solution.SOLUTION_INDEX_RANGE_START - 1))
    print(solution.solution(solution.SOLUTION_INDEX_RANGE_END + 1))
    print(solution.solution(0))
    print(solution.solution(3))


# Application entry point
if __name__ == "__main__":
    test()
