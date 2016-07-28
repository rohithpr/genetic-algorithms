from pprint import pprint
import random

import config
import particle

def trial(particles):
    [i.run() for i in particles]
    particles.sort(key=lambda x: x.fitness, reverse = True)

def get_survivors(generation, old):
    # Top 5 particles will be selected for sure
    selected = old[:5]
    print(generation, [(i.fitness, i.generation) for i in selected], (old[-1].fitness, old[-1].generation))

    # Pick 10 particles from the next 25
    others = old[5:30]
    random.shuffle(others)
    selected += others[:10]

    # Pick 35 from the remaining
    others = old[30:]
    random.shuffle(others)
    selected += others[:35]

    return selected

def make_child(p1, p2, generation):
    chromosomes = []
    for i in range(len(p1.chromosomes)):
        # Pick chromosomes from parents randomly
        cur = random.choice([p1, p2])
        chromosomes += cur.chromosomes[i]

    child = particle.Particle(chromosomes=chromosomes, generation=generation)
    return child

def make_children(particles, num, generation):
    children = []
    for i in range(num):
        # Pick parents randomly, fitness is not considered here
        parent1 = random.choice(particles)
        parent2 = random.choice(particles)
        child = make_child(parent1, parent2, generation)
        children.append(child)
    return children

def mutate(particles):
    for part in particles:
        for i in range(len(part.chromosomes)):
            if random.random() < config.MUTATION_PROBABILITY:
                part.chromosomes[i] = particle.Particle.random_move()

def main():
    # Create the zeroth generation
    particles = [particle.Particle(generation=0) for i in range(config.POPULATION)]

    # Uncomment this to start with one element having the most optimal chromosome
    # particles[0].chromosomes = ['d', 'r'] * (config.CHROMOSOME_LENGTH // 2)

    # Run the trials and sort particles based on their fitness (zeroth gen)
    trial(particles)

    generation = 0
    while generation < config.GENERATIONS:
        generation += 1

        # Get the survivors from this generation
        particles = get_survivors(generation-1, particles)

        # Increase population by making children!
        children = make_children(particles, 50, generation)

        for i in particles:
            children.append(particle.Particle(chromosomes=i.chromosomes, generation=i.generation))

        mutate(children)

        particles = children
        trial(particles)

    get_survivors(generation, particles)
    print(particles[0].fitness, particles[0].chromosomes, particles[0].position)
    # print(particles[0].fitness, particles[0].position)
    # pprint(particles[0].maze)

if __name__ == '__main__':
    main()
