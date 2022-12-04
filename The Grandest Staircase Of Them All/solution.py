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
__version__ = "1.1.0"
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

    # Start solving the problem using the most simple staircase design
    start_position = [n - 1, 1]

    agent = DFS_Search(start_position, goal_value=n)
    return agent.get_visited_number()


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

        # Parse the input parameters
        steps_number = len(node.position)
        if (steps_number < 2):
            return []

        # Get the possible neighbor positions
        neighbors = list()

        # Get neighboring positions
        for base_index in range(0, steps_number):

            # In case we are removing a brick from the last step
            if (base_index == (steps_number - 1)):

                # Check if we can create a new step position
                if (node.position[base_index] > 2):

                    candidate_position = node.position[:]
                    candidate_position[base_index] -= 1
                    candidate_position.append(1)

                    neighbor_node = AgentSearchNode(position=candidate_position)
                    neighbors.append(neighbor_node)

            # Otherwise, check where we can put new bricks
            else:

                # Check if we can remove a brick from the base position
                height_difference = node.position[base_index] - node.position[base_index + 1]
                
                if (height_difference <= 1):
                        continue

                for target_index in range(base_index + 1, steps_number + 1):
                    
                    # Check if we can create a new step position
                    if (target_index == steps_number):

                        if (node.position[target_index - 1] >= 2):

                            candidate_position = node.position[:]
                            candidate_position[base_index] -= 1
                            candidate_position.append(1)

                            neighbor_node = AgentSearchNode(position=candidate_position)
                            neighbors.append(neighbor_node)

                    else:    
                        
                        # Check if we can put a brick at the target position
                        height_difference = node.position[target_index - 1] - node.position[target_index]
                    
                        if ((height_difference > 2) or ((target_index > (base_index + 1)) and (height_difference > 1))):

                            candidate_position = node.position[:]
                            candidate_position[base_index] -= 1
                            candidate_position[target_index] += 1

                            # if (candidate_rank == self._goal):
                            neighbor_node = AgentSearchNode(position=candidate_position)
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

    def get_visited_number(self):
        """Return the agent number of goal positions found.

        Returns:
            int: The number of goal positions.
        """
        return len(self._visited)


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
            print("Current visited number = ", len(self._visited))
            input("PRESS ANY KEY TO CONTINUE...")

        # Search on the neighboring positions
        neighbors = self.get_neighbors(node)
        
        for neighbor in neighbors:
        
            # Check if the position is new, move and continue the search
            if (self.is_position_new(neighbor) == True):
                
                self.move(neighbor)

# **************************************************************
#                          Test Routine
# **************************************************************
def test():
    """ Application test function
    """

    from datetime import datetime

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
        [2,   0],
        [201, 0],

        [3,  1],
        [4,  1],
        [5,  2],
        [6,  3],
        [7,  4],
        [8,  5],
        [9,  7],
        [10, 9],
        [11, 11],
        [12, 14],
        [13, 17],
        [14, 21],
        [15, 26],
        [16, 31],
        [17, 37],
        [18, 45],
        [19, 53],
        [20, 63],
        [21, 75],
        [22, 88],
        [23, 103],
        [24, 121],
        [25, 141],
        [26, 164],
        [27, 191],
        [28, 221],
        [29, 255],
        [30, 295],
        [31, 339],
        [32, 389],
        [33, 447],
        [34, 511],
        [35, 584],
        [36, 667],
        [37, 759],
        [38, 863],
        [39, 981],
        [40, 1112],
        [41, 1259],
        [42, 1425],
        [43, 1609],
        [44, 1815],
        [45, 2047],
        [46, 2303],
        [47, 2589],
        [48, 2909],
        [49, 3263],

        # [
        #     200,       # Input
        #     487067745, # Expected result   
        # ],
    ]

    # Run every test case
    for test in test_cases:

        # Print the input array
        print("Input:\t   " + str(test[0]))

        # Measure the solution time
        start_time = datetime.now()
        
        # Run the solution
        result = solution(test[0])

        # Measure the solution time
        elapsed_time = (datetime.now() - start_time) 

        # Print the output array
        print("Output:\t   " + str(result))

        # Print the test result
        if (result == test[1]):
            pass_results += 1
            print(u"Test:     \033[1;32m PASSED\u001b[0m")
        else:
            fail_results += 1
            print("Expected:  " + str(test[1]))
            print(u"Test:      \u001b[31mFAILED\u001b[0m")

        # Print the solution time
        print("Test time: " + str(elapsed_time))

        print("============================================")

    # Print the test summary
    print(u"Test Results: \033[1;32m" + str(pass_results) +
          u" PASSED\u001b[0m and \u001b[31m" + str(fail_results) + u" FAILED\u001b[0m.")


# Application entry point
if __name__ == "__main__":
    # solution(9)

    test()

    # from datetime import datetime

    # for i in range(10):
        
    #     start_time = datetime.now()

    #     value = solution(i)

    #     stop_time = datetime.now()
    #     elapsed_time = (stop_time - start_time) 

    #     print("(" + str(i) + ", " + str(value) + ", " + str(elapsed_time) + ")")