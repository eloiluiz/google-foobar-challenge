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


# Import Libraries
import Queue

# Configuration Parameters
PRINT_DEBUG = False

# **************************************************************
#                           Solution
# **************************************************************
def solution(map):
    # Create the agent
    agent = AStarAgent(map, False, 1)
    # Run the search
    agent.start()
    # Return the result
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
        self._path_length = 0

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
    """Agent Search Method node.

    This class represents a node in the A* search path.
    """

    def __init__(self, parent, rank, cost, position, path, break_wall):
        self.parent = parent
        self.rank = rank
        self.cost = cost
        self.position = position
        self.agent_path = path
        self.break_wall = break_wall

    def __hash__(self):
      """Defines the hash method of the AgentSearchNode class.

      Returns:
          int: The object hash identification value.
      """
      return hash(str(self.position))

    def __cmp__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            int: Returns 1 if self rank is bigger, 0 if both are equal and -1 if other rank is bigger.
        """
        return (self.rank > other.rank) - (self.rank < other.rank)

    def __lt__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self rank is less than other and False otherwise.
        """
        return (self.rank < other.rank)

    def __le__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self rank is less or equal than other and False otherwise.
        """
        return (self.rank <= other.rank)

    def __gt__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self rank is greater than other and False otherwise.
        """
        return (self.rank > other.rank)

    def __ge__(self, other):
        """Compare two nodes using the rank attribute as reference.

        Args:
            other (AgentSearchNode): The other node under comparison.

        Returns:
            bool: Returns True if self rank is greater or equal than other and False otherwise.
        """
        return (self.rank >= other.rank)

class AStarAgent(Agent):
    """A* Search Method

    This class implements the A* Search algorithm.

    Args:
        Agent (object): The search algorithm intelligent agent parent class.

    Returns:
        object: The A* agent object.
    """

    def __init__(self, maze, return_first=True, break_wall=0):
        """Initialize the search agent and execute.
        """
        # Initialization process
        Agent.__init__(self, maze)
        self._path = []
        self._frontier = Queue.PriorityQueue()
        self._explored = set()
        self._return_first = return_first
        self._break_wall = break_wall

    def start(self):
        """Method that starts the goal search process and returns the resulting path.
        """
        # Execute the search
        start_node = AgentSearchNode(0, 0, self._heuristics(self._start_position), self._start_position,
                                     [self._start_position], self._break_wall)
        return self._search(start_node)

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

    def _heuristics(self, coordinates=[]):
        """Agent heuristic function the calculates movement costs to the goal position.

        This is a heuristic function that estimates the cost of the cheapest path from the input coordinate values to 
        the goal. This algorithm uses the Manhattan distance as this is the standard heuristic for a square grid.

        Args:
            coordinates (list): The movement coordinates [y, x].

        Returns:
            int: The movement cost estimation.
        """
        return self._movement_cost(coordinates, self._goal_position)

    def _search(self, node):
        """Agent search method.

        Args:
            node (AgentSearchNode): current A* node used in the search process.

        Returns:
            bool: The movement result, where True means the goal position is reached and False that it hasn't.
        """

        # Rename the input node
        current_node = node
        # Update the frontier list (search border)
        self._frontier.put(current_node)

        # Iterate over the frontier queue
        while (not self._frontier.empty()):

            # Remove the lowest ranking node from the queue
            current_node = self._frontier.get()
            current_position = current_node.position

            # Include current node to the explored list
            self._explored.add(current_node)

            # Print current movement step
            if (PRINT_DEBUG == True):
                print("Current position = ", current_position)
                for agent_position in current_node.agent_path:
                    self._maze.mark_position(agent_position[0], agent_position[1])
                self._maze.select_position(current_position[0], current_position[1])
                self._maze.print_map()
                input("PRESS ANY KEY TO CONTINUE...")
                self._maze.clear_path()

            # Test for goal position
            # If True, store the path just found (if it is shorter)
            if (self.is_goal_position(current_position[0], current_position[1])):
                new_path = current_node.agent_path
                new_path_length = len(new_path)
                # Check for the shorter path
                if ((self._path_length == 0) or (new_path_length < self._path_length)):
                    self._path = new_path
                    self._path_length = new_path_length
                # Check if the search must continue or stop at the first path found
                if (self._return_first == True):
                    return True
                else:
                    continue

            # If current position isn't the goal, search it's neighbors
            for neighbor_position in self.get_neighbors(current_position):

                # First, check if the neighbor is a valid position (frontier path or breakable wall)
                neighbor_break_wall = current_node.break_wall
                neighbor_position_value = self.get_position_value(neighbor_position[0], neighbor_position[1])
                if (neighbor_position_value == 1):
                    if (neighbor_break_wall > 0):
                        neighbor_break_wall -= 1
                    else:
                        continue

                # Check if neighbor is at current path already
                is_neighbor_in_agent_path = False
                for agent_path_position in current_node.agent_path:
                    if (neighbor_position == agent_path_position):
                        is_neighbor_in_agent_path = True
                        break

                # Checks if the cost of the current path is already greater than the best result found
                neighbor_path = current_node.agent_path[:]
                neighbor_path.append(neighbor_position)
                neighbor_path_length = len(neighbor_path)
                if ((self._path_length > 0) and (self._path_length < neighbor_path_length)):
                    # Discard neighbor if it's path is too long
                    continue

                # If neighbor is not in any of the lists, add it to frontier
                if (is_neighbor_in_agent_path == False):
                    neighbor_new_cost = current_node.cost + self._movement_cost(current_position, neighbor_position)
                    neighbor_rank = neighbor_new_cost + self._heuristics(neighbor_position)
                    neighbor_node = AgentSearchNode(current_node, neighbor_rank, neighbor_new_cost, neighbor_position,
                                                    neighbor_path, neighbor_break_wall)
                    self._frontier.put(neighbor_node)

            # Print current search
            if (PRINT_DEBUG == True):
                for explored_node in self._explored:
                    self._maze.mark_position(explored_node.position[0], explored_node.position[1])
                for frontier_node in self._frontier.queue:
                    self._maze.select_position(frontier_node.position[0], frontier_node.position[1])
                self._maze.select_position(current_position[0], current_position[1])
                self._maze.print_map()
                input("PRESS ANY KEY TO CONTINUE...")
                self._maze.clear_path()

        # If the frontier list gets empty, the goal was not found
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
            [[0, 1], 
             [0, 0]],
            3
        ],
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
        [
          [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
          57
        ],
        [
          [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
           [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
          57
        ],
        [
          [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
           [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
           [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
           [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
           [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 0, 1, 0],
           [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
           [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
           41
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