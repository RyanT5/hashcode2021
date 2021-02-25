import operator
import collections
import hashlib
import itertools

file_names = {'a': "a.txt",
              "b": "b.txt",
              "c": "c.txt",
              "d": "d.txt",
              "e": "e.txt",
              "f": "f.txt"}

# Reads the input text file and retrieves the variables
# D - duration of the simulation
# I - number of intersections
# S - number of streets
# V - number of cars
# F - bonus points
# streets -map of street name -> [B, E, L]
# cars - map of cars (number) -> [street names]
# intersections - map of intersection numbers -> [street names]
def read_input(input_file):
    streets = {}
    cars = {}
    intersection_frequency = {}
    entering_streets = {}
    exiting_streets = {}
    
    # opens the file
    input = open(input_file, 'r')
    
    # reads duration, streets etc.
    DISVF = input.readline()
    split = DISVF.split()
    D = int(split[0])
    I = int(split[1])
    S = int(split[2])
    V = int(split[3])
    F = int(split[4])

    #map of street name -> [B, E, L]
    #map of intersection no -> [street names]
    street = 0
    while street < S:
        split = input.readline().split()
        B = int(split[0])
        street_name = split[2]
        E = int(split[1])
        L = int(split[3])
        
        if B not in entering_streets:
            entering_streets[B] = []
        entering_streets[B].append(street_name)
        if E not in exiting_streets:
            exiting_streets[E] = []
        exiting_streets[E].append(street_name)            
        
        if street_name not in streets:
            streets[street_name] = []
        streets[street_name].append(B)
        streets[street_name].append(E)
        streets[street_name].append(L)
        street += 1

    car = 0
    # map of cars -> [street names]
    while car < V:
        split = input.readline().split()
        P = int(split[0])
        street = 1
        street_path = []
        while street < P:
            street_path.append(split[street])
            street +=1
        cars[car] = street_path
        car += 1

    input.close()

    return D, I, S, V, F, streets, cars, entering_streets, exiting_streets

def write_solution(schedule, input_letter):
    with open('{}_soln.txt'.format(input_letter), 'w') as solution:
        num_intersections = len(schedule)
        text = "" + str(num_intersections) + "\n"
        for intersection, streets in schedule.items():
            text += str(intersection) + "\n"
            text += str(len(streets)) + "\n"
            for (street, seconds) in streets:
                text += street + " " + str(seconds) + "\n"
            text.rstrip()
        solution.write(text)

# INPUT YOUR SOLUTION HERE
def scheduler(D, I, S, V, F, streets, cars, entering_streets, exiting_streets):
    # map of intersection no. -> [(street, seconds per cycle)]
    schedule = {}
    street_in_schedule = {}
    car_paths = {}
    for car, path in cars.items():
        length = 0
        for street in path:
            BEL = streets[street]
            length += BEL[2]
        car_paths[car] = length
    
    sort_by_path_length = sorted(car_paths.items(),key=operator.itemgetter(1),reverse=False)
    sorted_car_paths = collections.OrderedDict(sort_by_path_length)

    for car, path in sorted_car_paths.items():
        for street in cars[car]:
            if street not in street_in_schedule:
                BEL = streets[street]
                E = BEL[1]
                if E not in schedule:
                    schedule[E] = []

                no_entering_streets = len(entering_streets[E])
                no_exiting_streets = len(exiting_streets[E])
                no_streets = no_exiting_streets + no_entering_streets
                time = 0
                for (_,t) in schedule[E]:
                    time += t
                if time == 0:
                    schedule[E].append((street, no_entering_streets))
                elif time > 0 and time < no_streets:
                    schedule[E].append((street, no_streets-time))
                else:
                    schedule[E].append((street, 1))
                street_in_schedule[street] = True
    return schedule

# Pass in a letter, eg. problem "A" and this will do the rest
def get_file_and_write_output(problem):
    file_name = file_names[problem]

    print("Parsing: ", file_name)

    # Get the input
    D, I, S, V, F, streets, cars, entering_streets, exiting_streets = read_input('inputs/{}'.format(file_name))

    print("Attempting Solution for: ", file_name)

    #Process the input
    soln = scheduler(D, I, S, V, F, streets, cars, entering_streets, exiting_streets)

    write_solution(soln, problem)

for problem in ["a", "b", "c", "d", "e", "f"]:
    get_file_and_write_output(problem)
