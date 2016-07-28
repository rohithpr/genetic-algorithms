import random

import config

WIDTH = range(config.MAZE_WIDTH)
HEIGHT = range(config.MAZE_HEIGHT)
LENGTH = range(config.CHROMOSOME_LENGTH)

class Particle:

    @staticmethod
    def random_move():
        return random.choice(config.MOVES)

    @staticmethod
    def get_chromosomes():
        return [Particle.random_move() for i in LENGTH]

    @staticmethod
    def get_maze():
        maze = [[i*j for j in WIDTH] for i in HEIGHT]

        # Optional: position where the maze terminates
        # maze[-1][-1] = 'f'

        # Add borders
        # Sides
        for i in HEIGHT:
            maze[i] = ['b'] + maze[i] + ['b']
        # Top and bottom
        blanks = [['b'] * (config.MAZE_WIDTH + 2)]
        maze = blanks + maze + blanks
        # print(maze[10][9], maze[9][10])
        return maze

    def __init__(self, chromosomes=None, maze=None, fitness=0, position=[1, 1], generation=-1):
        # Moves that the particle will make
        self.chromosomes = chromosomes or Particle.get_chromosomes()

        # Maze that the particle has to solve
        self.maze = maze or Particle.get_maze()

        # Metric of how good the current set of moves are
        self.fitness = fitness

        # Position of the particle in the maze at a point of time
        self.position = position

        # Generation to which the particle belongs
        self.generation = generation

        # Keeps track of the next move to be made
        self.index = -1

        # Flag to check if maze has been solved
        self.done = False

    def __str__(self):
        items = [self.generation, self.fitness, self.position, self.maze]
        str_items = list(map(str, items))
        output = ', '.join(str_items)
        return output

    def can_move(self):
        return (self.index != len(self.chromosomes) - 1) and not self.done

    def get_next_move(self):
        self.index += 1
        return self.chromosomes[self.index]

    def update_position(self, move):
        new_pos = self.position[:]
        if move == 'l':
            new_pos[0] -= 1
        elif move == 'r':
            new_pos[0] += 1
        elif move == 'u':
            new_pos[1] -= 1
        elif move == 'd':
            new_pos[1] += 1

        value = self.maze[new_pos[0]][new_pos[1]]
        if value == 'b':
            # Reduce fitness by 1 if the particle runs into a wall
            # Position of the particle is not updated
            return -1
        elif value == 'f':
            self.maze[new_pos[0]][new_pos[1]] = 'r'
            self.done = True
            return None
        else:
            self.position = new_pos[:]
            return value

    def move(self):
        move = self.get_next_move()
        value = self.update_position(move)

        if value is not None:
            # Add the value from maze to fitness
            self.fitness += value

            # Value of the position on the board is halved
            # This discourages the particle from getting stuck in local maxima's
            self.maze[self.position[0]][self.position[1]] /= 2
        else:
            self.fitness += config.REWARD

    def run(self):
        while self.can_move():
            self.move()
