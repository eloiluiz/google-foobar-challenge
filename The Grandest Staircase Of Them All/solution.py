#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Grandest Staircase Of Them All
==================================

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloiluiz@gmail.com"
__version__ = "1.0.0"
__status__ = "Production"

# Configuration Parameters
PRINT_DEBUG = False

# **************************************************************
#                           Solution
# **************************************************************
def solution(n):
    """ Receives the number of available bricks and calculate the number of different staircases that can be built.
    """

    # First, check the input parameter
    if (isinstance(n, int) == False):
        return 0

    if ((n < 3) or (n > 200)):
        return 0

    agent = DFS_Search(start_position=[2, 1], goal_value=n)
    return agent.get_goal_number()


# **************************************************************
#                          Agent Class
# **************************************************************
class Agent:
    """Intelligent agent base class.
    """

    def __init__(self, start_position=[], goal_value=0, search_all=True):
        """Initializes the agent attributes.
        """
        # Initialize the search tree parameters
        self._start_position = start_position
        self._goal = goal_value
        self._goal_number = 0
        self._visited = list()
        self._search_all = search_all

    def get_neighbors(self, node):
        """Return the selected coordinate neighbors.

        Args:
            node (AgentSearchNode): current node used in the search process.
        """

        # print("node.position_length", len(node.position))

        # Parse the input parameters
        if (len(node.position) < 2):
            return []

        # Get the possible neighbor positions
        neighbors = list()
        
        # Get neighboring positions
        for index in range(0, len(node.position) + 1):

            # print("index", index)

            candidate_position = []

            if (index == 0):
                candidate_position = node.position[:]
                candidate_position[index] += 1

            elif (index == len(node.position)):
                if (node.position[index - 1] > 1):
                    candidate_position = node.position[:]
                    candidate_position.append(1)

            elif ((node.position[index - 1] - node.position[index]) > 1):
                candidate_position = node.position[:]
                candidate_position[index] += 1

            # print("candidate_position", candidate_position)

            candidate_rank = sum(candidate_position)

            # print("rank", rank)

            if (candidate_rank > 3) and (candidate_rank <= self._goal):
                neighbor_node = AgentSearchNode(candidate_rank, candidate_position)
                neighbors.append(neighbor_node)

        # Return the neighbors
        return neighbors

    def is_position_new(self, node):
        """Verifies if the agent is using new coordinate values.

        Args:
            node (AgentSearchNode): current node used in the search process.

        Returns:
            bool: The verification result, where True means the node position is new and False means the position have been visited already.
        """

        # Check if the input node is valid
        if (isinstance(node, AgentSearchNode) == False):
            return False

        # Check if the node position is new
        for i in range(len(self._visited)):

            if (self._visited[i] == node):
                return False

        return True

    def is_search_goal(self, node):
        """Verifies if the agent has reached the search goal using the input coordinates.

        Args:
            node (AgentSearchNode): current node used in the search process.

        Returns:
            bool: The verification result, where True means the goal is reached and False that it hasn't.
        """
        return (node.rank == self._goal)

    def get_goal_number(self):
        """Return the agent number of goal positions found.

        Returns:
            int: The number of goal positions.
        """
        return self._goal_number


class AgentSearchNode:
    """Agent Search Method node.

    This class represents a node in the tree search process.
    """

    def __init__(self, rank=0, position=[]):
        self.rank = rank
        self.position = position
        self.key = ''.join([str(x) + "," for x in position])

    def __eq__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            int: Returns True if self key equals the other and False otherwise.
        """
        return (self.key == other.key)

    def __ne__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            int: Returns True if self key differs from the other and False otherwise.
        """
        return (self.key != other.key)

    def __cmp__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            int: Returns 1 if self key is bigger, 0 if both are equal and -1 if other key is bigger.
        """
        return (self.key > other.key) - (self.key < other.key)

    def __lt__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self key is less than other and False otherwise.
        """
        return (self.key < other.key)

    def __le__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self key is less or equal than other and False otherwise.
        """
        return (self.key <= other.key)

    def __gt__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self key is greater than other and False otherwise.
        """
        return (self.key > other.key)

    def __ge__(self, other):
        """Compare two nodes using the key attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self key is greater or equal than other and False otherwise.
        """
        return (self.key >= other.key)


# **************************************************************
#                          Search Class
# **************************************************************
class DFS_Search(Agent):
    """Depth-First Search Method

    This class implements the Depth-First Search algorithm.

    Args:
        Agent (object): The search algorithm intelligent agent parent class.

    Returns:
        object: The DFS agent object.
    """

    def __init__(self, start_position, goal_value):
        """Initialize the search agent and execute.
        """
        # Initialization process
        Agent.__init__(self, start_position, goal_value)
        
        # Create the first tree node
        rank = sum(start_position)
        node = AgentSearchNode(rank, start_position)

        # Execute the search
        self.move(node)

    def move(self, node):
        """Agent movement method.

        Args:
            node (AgentSearchNode): current node used in the search process.

        Returns:
            bool: The movement result, where True means the goal position is reached and False that it hasn't.
        """

        # Update the visited positions list
        self._visited.append(node)

        # Print current movement step
        if (PRINT_DEBUG == True):
            print("Current coordinate = ", node.position)
            print("Current visited = ", self._visited)
            raw_input("PRESS ANY KEY TO CONTINUE...")

        # Test for goal position
        # If True, increment the path number and return
        if (self.is_search_goal(node)):
            self._goal_number += 1
            return True

        # If the current position isn't the goal,

        # Search on the neighboring positions
        neighbors = self.get_neighbors(node)
        
        for neighbor in neighbors:
        
            # Check if the position is new, move and continue the search
            if (self.is_position_new(neighbor) == True):
                
                is_goal_found = self.move(neighbor)

                # Check the search stop condition and return True if the goal is found
                if ((self._search_all == False) and (is_goal_found == True)):
                    return True

        # If none of its neighbors is the goal, return false
        return False

# **************************************************************
#                          Test Routine
# **************************************************************
def test():
    """ Application test function
    """

    pass_results = 0
    fail_results = 0

    # Define every test case for the application
    test_cases = [
        [
            '\0', # Input
            0,    # Expected result   
        ],
        ['',  0],
        ['a', 0],
        [-1,  0],
        [0,   0],
        [1,   0],
        [201, 0],

        [3,   1],
        [4,   1],
        [5,   2],
        [6,   3],
        [7,   4],
        [8,   5],

        # [
        #     200,       # Input
        #     487067745, # Expected result   
        # ],
    ]

    # Run every test case
    for test in test_cases:

        # Print the input array
        print("Input:")
        print("\t" + str(test[0]))

        # Run the solution
        result = solution(test[0])

        # Print the output array
        print("Output:\n" + str(result))

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

    # from datetime import datetime

    # for i in range(201):
        
    #     start_time = datetime.now()

    #     value = solution(i)

    #     stop_time = datetime.now()
    #     elapsed_time = (stop_time - start_time) 

    #     print("(" + str(i) + ", " + str(value) + ", " + str(elapsed_time) + ")")