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
def read_input(input_file):
    streets = {}
    cars = {}
    
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
    street = 0
    while street < S:
        split = input.readline().split()
        BEL = []
        BEL.append(int(split[0]))
        BEL.append(int(split[1]))
        BEL.append(int(split[3]))
        street_name = split[2]
        streets[street_name] = BEL

    car = 0
    # map of cars -> [street names]
    while car < V:
        split = input.readline().split()
        P = split[0]
        street = 1
        streets = []
        while street < P:
            streets.append(split[street])
        cars[car] = streets

    input.close()

    return D, I, S, V, F, streets, cars

def write_solution(schedule, input_letter):
    with open('{}_soln.txt'.format(input_letter), 'w') as solution:
        num_intersections = len(schedule)
        text = "" + str(num_intersections) + "\n"
        for intersection, streets in schedule.items:
            text += str(intersection) + " "
            text += str(len(streets)) + "\n"
            for (street, seconds) in streets:
                text += street + " " + str(seconds)
            text.rstrip()
            text += "\n"
        solution.write(text)

# INPUT YOUR SOLUTION HERE
def scheduler(D, I, S, V, F, streets, cars):
    # map of intersection no. -> [(street, seconds per cycle)]
    schedule = {}
    return schedule

# Pass in a letter, eg. problem "A" and this will do the rest
def get_file_and_write_output(problem):
    file_name = file_names[problem]

    print("Parsing: ", file_name)

    # Get the input
    D, I, S, V, F, streets, cars = read_input('inputs/{}'.format(file_name))

    #Process the input
    soln = scheduler(D, I, S, V, F, streets, cars)

    write_solution(soln, problem)

for problem in ["a", "b", "c", "d", "e", "f"]:
    get_file_and_write_output(problem)