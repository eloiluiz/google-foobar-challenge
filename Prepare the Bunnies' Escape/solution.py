#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
"""


__author__ = "Eloi Giacobbo"
__email__ = "eloiluiz@gmail.com"
__version__ = "1.0.0"
__status__ = "Production"


# Import libraries
import Queue


# **************************************************************
#                           Solution
# **************************************************************
def solution(map):
    # Create the agent
    agent = AStarAgent(map)
    agent.start()
    path = agent.get_path()
    return len(path)

# **************************************************************
#                          Agent Class
# **************************************************************
class Agent:
    """Intelligent agent base class.
    """

    def __init__(self, maze):
        """Initializes the agent attributes.
        """
        # Initialize the map parameters
        self._maze = maze
        self._height = len(maze)
        self._width = len(maze[self._height - 1])
        self._start_position = [(self._height - 1), (self._width - 1)]
        self._goal_position = [0, 0]
        self._path = []
        # Parse the map values
        # self._maze = []
        # for row in range(self._height):
        #     self._maze.append([map(int, maze[row])])
            # for column in range(self._width):
            #     maze[row][column] = int(maze[row][column])

    def get_neighbors(self, coordinates=[], y=None, x=None):
        """Return the selected coordinate neighbors.

        Args:
            coordinates (list): The movement coordinates [y, x].
        """
        # Parse the input parameters
        _y = 0
        _x = 0
        if (len(coordinates) > 0):
            _y = coordinates[0]
            _x = coordinates[1]
        elif ((y != None) and (x != None)):
            _y = y
            _x = x
        else:
            return []
        # Get the possible neighbor positions
        candidate = [[(_y + 1), _x], [(_y - 1), _x], [_y, (_x - 1)], [_y, (_x + 1)]]
        # Return the valid neighbors
        neighbor = []
        for i in range(len(candidate)):
            if ((candidate[i][0] >= 0) and (candidate[i][1] >= 0) and 
                (candidate[i][0] < self._height) and (candidate[i][1] < self._width)):
                neighbor.append(candidate[i])
        return neighbor

    def get_position_value(self, y, x):
        """Returns the selected position value.

        Args:
            y (int): The selected position y coordinate.
            x (int): The selected position x coordinate.

        Returns:
            int: The selected position value.
        """
        return self._maze[y][x]

    def is_goal_position(self, y, x):
        """Verifies if the agent has reached the goal position using the input coordinates.

        Args:
            y (int): The selected position y coordinate.
            x (int): The selected position x coordinate.

        Returns:
            bool: The verification result, where True means the goal position is reached and False that it hasn't.
        """
        if ((y == 0) and (x == 0)):
            return True
        else:
            return False

    def get_path(self):
        """Return the agent mapped path

        Returns:
            list: The mapped path from the start position to the goal.
        """
        return self._path

class AgentSearchNode:
    """Agent Search Methode node.

    This class represents the nodes used in the search process.
    """

    def __init__(self, parent, rank, cost, position, break_wall):
        self.parent = parent
        self.rank = rank
        self.cost = cost
        self.position = position
        self.break_wall = break_wall

    def __cmp__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (A_Star_Node): The other node under comparison.

        Returns:
            int: Returns 1 if self rank is bigger, 0 if both are equal and -1 if other rank is bigger.
        """
        return (self.rank > other.rank) - (self.rank < other.rank)

    def __lt__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (A_Star_Node): The other node under comparison.

        Returns:
            bool: Returns True if self rank is less than other and False otherwise.
        """
        return (self.rank < other.rank)

    def __le__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (A_Star_Node): The other node under comparison.

        Returns:
            bool: Returns True if self rank is less or equal than other and False otherwise.
        """
        return (self.rank <= other.rank)

    def __gt__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (A_Star_Node): The other node under comparison.

        Returns:
            bool: Returns True if self rank is greater than other and False otherwise.
        """
        return (self.rank > other.rank)

    def __ge__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (A_Star_Node): The other node under comparison.

        Returns:
            bool: Returns True if self rank is greater or equal than other and False otherwise.
        """
        return (self.rank >= other.rank)


class AStarAgent(Agent):
    """A* Search Agent

    This class implements the A* Search algorithm.

    Args:
        Agent (object): The search algorithm intelligent agent parent class.

    Returns:
        object: The A* agent object.
    """

    def __init__(self, maze):
        """Initialize the search agent and execute.
        """
        # Initialization process
        Agent.__init__(self, maze)
        self._open = Queue.PriorityQueue()
        self._closed = []

    def start(self):
        """Method that starts the goal search process and returns the resulting path.
        """
        # Execute the search
        start_node = AgentSearchNode(0, 0, self._f(self._start_position), self._start_position, 1)
        self._search(start_node)

    def _movement_cost(self, origin=[], destination=[]):
        """Agent heuristic function that calculates movement costs.

        This algorithm uses the Manhattan distance to calculates movement cost as this is the standard heuristic for a
        square grid.

        Args:
            origin (list): The origin (start) position coordinates [y, x].
            destination (list): The destination (end) position coordinates [y, x].

        Returns:
            int: The movement cost estimation.
        """
        dy = abs(destination[0] - origin[0])
        dx = abs(destination[1] - origin[1])
        return (dx + dy)

    def _g(self, coordinates=[]):
        """Agent heuristic function that calculates movement costs from the start position.

        This is a heuristic function that represents the exact cost of the path from the start position to the input 
        coordinate values. This algorithm uses the Manhattan distance as this is the standard heuristic for a square 
        grid.

        Args:
            coordinates (list): The movement coordinates [x, y].

        Returns:
            int: The movement cost estimation.
        """
        return self._movement_cost(self._start_position, coordinates)

    def _h(self, coordinates=[]):
        """Agent heuristic function the calculates movement costs to the goal position.

        This is a heuristic function that estimates the cost of the cheapest path from the input coordinate values to 
        the goal. This algorithm uses the Manhattan distance as this is the standard heuristic for a square grid.

        Args:
            coordinates (list): The movement coordinates [y, x].

        Returns:
            int: The movement cost estimation.
        """
        return self._movement_cost(coordinates, self._goal_position)

    def _f(self, coordinates=[]):
        """Agent heuristic function the calculates the total cost of the selected coordinate.

        This is a heuristic function that estimates the total movement cost of the input coordinate. This algorithm uses
        the Manhattan distance as this is the standard heuristic for a square grid.

        Args:
            coordinates (list): The movement coordinates [y, x].

        Returns:
            int: The movement cost estimation.
        """
        return (self._g(coordinates) + self._h(coordinates))

    def _search(self, node):
        """Agent search method.

        Args:
            node (A_Star_Node): current A* node used in the search process.

        Returns:
            bool: The movement result, where True means the goal position is reached and False that it hasn't.
        """

        # Rename the input node
        current_node = node
        # Update the visited positions list
        self._open.put(current_node)

        # Iterate over the open queue
        while (not self._open.empty()):

            # Remove the lowest ranking node from the queue
            current_node = self._open.get()
            current_position = current_node.position

            # Put the visited node to the closed list
            self._closed.append(current_node)

            # Test for goal position
            # If True, set path and return True
            if (self.is_goal_position(current_position[0], current_position[1])):
                while (isinstance(current_node, AgentSearchNode)):
                    self._path.append(current_node.position)
                    current_node = current_node.parent
                return True

            # If current position isn't the goal, search it's neighbors
            for neighbor_position in self.get_neighbors(current_position):

                # First, check if the neighbor is a valid position (open path)
                neighbor_position_value = self.get_position_value(neighbor_position[0], neighbor_position[1])
                if (current_node.break_wall > 0):
                    current_node.break_wall -= 1
                elif (neighbor_position_value == 1):
                    continue

                # Calculate the neighbor costs (from current and from start position)
                neighbor_new_cost = current_node.cost + self._movement_cost(current_position, neighbor_position)
                neighbor_gcost = self._g(neighbor_position)

                # Check if the neighbor is at any of the open and closed lists
                is_neighbor_open = False
                is_neighbor_closed = False

                # Check if neighbor is at the open list and is a viable path
                for open_node in self._open.queue:
                    open_position = open_node.position
                    if (neighbor_position == open_position):
                        if (neighbor_new_cost < neighbor_gcost):
                            # Remove position from the open queue
                            self._open.queue.remove(open_node)
                        else:
                            is_neighbor_open = True

                # Check if neighbor is at the closed list and is a viable path
                for closed_node in self._closed:
                    closed_position = closed_node.position
                    if (neighbor_position == closed_position):
                        if (neighbor_new_cost < neighbor_gcost):
                            # Remove position from the closed list
                            self._closed.remove(closed_node)
                        else:
                            is_neighbor_closed = True

                # If neightbor is not in any of the lists, add it to open
                if ((is_neighbor_open == False) and (is_neighbor_closed == False)):
                    neighbor_node = AgentSearchNode(current_node, neighbor_new_cost + self._f(neighbor_position), neighbor_new_cost, neighbor_position, current_node.break_wall)
                    self._open.put(neighbor_node)

        # If the open list gets empty, the goal was not found
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
            [[0, 1, 1, 0], 
             [0, 0, 0, 1], 
             [1, 1, 0, 0], 
             [1, 1, 1, 0]],
            7
        ],
        [
            [[0, 0, 0, 0, 0, 0], 
             [1, 1, 1, 1, 1, 0], 
             [0, 0, 0, 0, 0, 0], 
             [0, 1, 1, 1, 1, 1], 
             [0, 1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 0, 0]],
            11
        ],
        [
            [[0, 1, 0, 0, 0, 0], 
             [1, 1, 1, 1, 1, 0], 
             [1, 0, 0, 0, 0, 0], 
             [0, 0, 1, 1, 1, 1], 
             [0, 1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 0, 0]],
            21
        ],
    ]
    # Run every test case
    for test in test_cases:
        # Print the input array
        print("Input:")
        for row in range(len(test[0])):
            print("\t" + str(test[0][row]))
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