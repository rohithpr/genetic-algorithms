# The possible moves that can be made by the particle
MOVES = ['l', 'r', 'u', 'd', 's']

# No. of generations
GENERATIONS = 500

# No. of specimens per generation
POPULATION = 100

# Number of moves per turn, per particle
CHROMOSOME_LENGTH = 50

# Probability that a given move in the chromosome will be replaced with a random move
# Value should be in the interval [0, 1]
# If this is 1 (or too high) the entire chromosome will be rewritten on each trial. This means that the required traits from the previous generation are lost and will lead to suboptimal results.
# Setting it too low will result in very mutations which causes the chromosomes to get stuck in local optimums
# 0.007 was suggested as a good value for mutation probability by some white paper, it has worked out well for me
MUTATION_PROBABILITY = 0.007

# Maze dimensions
MAZE_HEIGHT = 12
MAZE_WIDTH = 12

# Select the maze to be solved
# A maze with no walls will be created if an invalid number is given
MAZE_NUMBER = 1

# Reward for finishing the maze
# This reward will be awarded if the maze has a position marked 'f'.
# Reaching this element also stops execution of subsequent moves
REWARD = 5000
