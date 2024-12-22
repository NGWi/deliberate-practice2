import sys
from collections import deque

protein_costs = {'BASIC': [1, 0, 0, 0], 'TENTACLE': [0, 1, 1, 0], 'HARVESTER': [0, 0, 1, 1],
                 'SPORER': [0, 1, 0, 1], 'ROOT': [1, 1, 1, 1]}

def subtract_costs(organ_type):
    costs = protein_costs[organ_type]
    global my_a, my_b, my_c, my_d
    my_a -= costs[0]
    my_b -= costs[1]
    my_c -= costs[2]
    my_d -= costs[3]

def wrapper(organism_index, function, organ_type=None):
    organism_id = my_root_ids[organism_index]
    print("Organism:", organism_index, f"'{organism_id}'", file=sys.stderr, flush=True)
    global organism_entities
    organism_entities = my_entities[organism_id]
    global its_free_spaces
    its_free_spaces = adj_free_spaces[organism_index]
    if organ_type is None:
        return function()
    else:
        return function(organ_type)

def find_spaces():
    adj_free_spaces = []
    for key, value in organism_entities.items():
        (start_x, start_y) = key
        (type_, owner, organ_id, organ_parent_id, organ_root_id) = value
        if owner == 1 and organ_id:
            for dx, dy in directions:
                new_x, new_y = start_x + dx, start_y + dy
                if 0 <= new_x < width and 0 <= new_y < height and \
                    ((new_x, new_y) not in entities or grid[new_y][new_x] in ['A', 'B', 'C', 'D']) and \
                    (new_x, new_y) not in red_cells and \
                    ((new_x, new_y) not in my_farm_locs or retrying):
                    adj_free_spaces.append((organ_id, string[directions.index((dx, dy))], (new_x, new_y)))

    return adj_free_spaces

def bfs(start_x, start_y, grid, width, height):
    queue = deque([(start_x, start_y, [])])  # (x, y, path)
    visited = set(my_farm_locs.keys())  # Create a set of all the locations in my_farm_locs
    visited.add((start_x, start_y))

    while queue:
        x, y, path = queue.popleft()
        
        # Check if current position is a protein source
        if grid[y][x] in ['A', 'B', 'C', 'D'] and (((x, y) not in my_farm_locs) or retrying):
            return path + [(x, y)]  # Return the path to the protein source
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check bounds and if not visited
            if 0 <= new_x < width and 0 <= new_y < height and (new_x, new_y) not in visited:
                if grid[new_y][new_x] in ["", "A", "B", "C", "D"]:  # Open for moving
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, path + [(x, y)]))
    
    return None  # No path found

def farm():
    print("Checking if we should farm", file=sys.stderr, flush=True)
    closest_protein = closest_proteins[organism_index]
    closest_path = closest_paths[organism_index]
    closest_organ_id = closest_organ_ids[organism_index]
    target_x, target_y = closest_protein  # Get the last position in the path
    # Determine direction to the protein source
    adjacent_tile = closest_path[1]  # The first step in the path
    adj_x, adj_y = adjacent_tile
    if adj_y < target_y:  # Protein is below
        direction_to_protein = 'S'
    elif adj_y > target_y:  # Protein is above
        direction_to_protein = 'N'
    elif adj_x < target_x:  # Protein is to the right
        direction_to_protein = 'E'
    elif adj_x > target_x:  # Protein is to the left
        direction_to_protein = 'W'

    print(f"GROW {closest_organ_id} {adj_x} {adj_y} HARVESTER {direction_to_protein}", file=sys.stderr, flush=True)
    my_entities[organism_id][(adj_x, adj_y)] = ('HARVESTER', 1, None, closest_organ_id, organism_id)
    grid[adj_y][adj_x] = 'HARVESTER'
    my_farm_locs[(target_x, target_y)] = grid[target_y][target_x]
    subtract_costs('HARVESTER')
    return f"GROW {closest_organ_id} {adj_x} {adj_y} HARVESTER {direction_to_protein}"

                    
def spore_root_farm(its_free_spaces):
    print("Checking if we should grow a sporer", file=sys.stderr, flush=True)
    for space in its_free_spaces:
        roots_visited = set()
        sporer_loc = space[2]
        sporer_x, sporer_y = sporer_loc
        for (dx, dy), direction in zip(directions, string):
            root_x, root_y = sporer_x + dx, sporer_y + dy
            # print(f"Checking from space {sporer_x} {sporer_y} towards {direction}", file=sys.stderr, flush=True)
            while 0 <= root_x < width and 0 <= root_y < height and \
                ((root_x, root_y) not in entities or grid[root_y][root_x] in ['A', 'B', 'C', 'D']):
                # print(f"Checking space {root_x} {root_y}", file=sys.stderr, flush=True)
                if (root_x, root_y) not in roots_visited and (root_x, root_y) not in entities:
                    roots_visited.add((root_x, root_y))
                    harvests_visited = set()
                    for hx, hy in directions:
                        harvest_x, harvest_y = root_x + hx, root_y + hy
                        if 0 <= harvest_x < width and 0 <= harvest_y < height and \
                            (harvest_x, harvest_y) not in harvests_visited and \
                            (harvest_x, harvest_y) not in entities and \
                            (harvest_x, harvest_y) != (sporer_x, sporer_y) and \
                            (harvest_x, harvest_y) not in red_cells:

                                harvests_visited.add((harvest_x, harvest_y))
                                for px, py in directions:
                                    protein_x, protein_y = harvest_x + px, harvest_y + py
                                    if 0 <= protein_x < width and 0 <= protein_y < height and \
                                        grid[protein_y][protein_x] in ['A', 'B', 'C', 'D'] and \
                                        (protein_x, protein_y) not in my_farm_locs:
                                            print(f"GROW {space[0]} {sporer_x} {sporer_y} SPORER {direction}", file=sys.stderr, flush=True)
                                            my_entities[organism_id][(sporer_x, sporer_y)] = ('SPORER', 1, None, organ_parent_id, organ_root_id)
                                            grid[sporer_y][sporer_x] = 'SPORER'
                                            subtract_costs('SPORER')
                                            return f"GROW {space[0]} {sporer_x} {sporer_y} SPORER {direction}"
                root_x, root_y = root_x + dx, root_y + dy

def root_farm():
    print("Checking if we should grow a root", file=sys.stderr, flush=True)
    sporers = my_sporers[organism_id]
    for sporer_x, sporer_y, organ_id, organ_dir in sporers:
        roots_visited = set()
        dx, dy = directions[string.index(organ_dir)]
        root_x, root_y = sporer_x + dx, sporer_y + dy
        print(f"Checking from sporer {sporer_x} {sporer_y} towards {organ_dir}", file=sys.stderr, flush=True)
        while 0 <= root_x < width and 0 <= root_y < height and \
            ((root_x, root_y) not in entities or grid[root_y][root_x] in ['A', 'B', 'C', 'D']):
            print(f"Checking space {root_x} {root_y}", file=sys.stderr, flush=True)
            if (root_x, root_y) not in roots_visited and (root_x, root_y) not in entities:
                roots_visited.add((root_x, root_y))
                harvests_visited = set()
                for hx, hy in directions:
                    harvest_x, harvest_y = root_x + hx, root_y + hy
                    if 0 <= harvest_x < width and 0 <= harvest_y < height and \
                        (harvest_x, harvest_y) not in harvests_visited and \
                        (harvest_x, harvest_y) not in entities and \
                        (harvest_x, harvest_y) != (sporer_x, sporer_y) and \
                        (harvest_x, harvest_y) not in red_cells: # Sporer check only to make this a duplicate of spore_root_farm so can turn it into function.

                            harvests_visited.add((harvest_x, harvest_y))
                            for px, py in directions:
                                protein_x, protein_y = harvest_x + px, harvest_y + py
                                if 0 <= protein_x < width and 0 <= protein_y < height and \
                                    grid[protein_y][protein_x] in ['A', 'B', 'C', 'D'] and \
                                    (protein_x, protein_y) not in my_farm_locs:
                                        print(f"SPORE {organ_id} {root_x} {root_y} ROOT", file=sys.stderr, flush=True)
                                        my_entities[organism_id][(root_x, root_y)] = ('ROOT', 1, None, organ_parent_id, organ_root_id)
                                        grid[root_y][root_x] = 'ROOT'
                                        subtract_costs('ROOT')
                                        return f"SPORE {organ_id} {root_x} {root_y}"
            root_x, root_y = root_x + dx, root_y + dy

def hunting_path(hunter):
    print(f"Checking if we should grow a {hunter} towards a protein", file=sys.stderr, flush=True)
    # Find the first step in the path to grow a BASIC organ
    closest_path = closest_paths[organism_index]
    direction_str = closest_path[0]
    new_x, new_y = closest_path[1]  # The next step in the path
    """
    We should prefer facing a side that has an enemy organ, if there is none then the direction then the direction we are growing 
    as I wrote here but only if there's no wall. If there's a wall, then towards a side that has an empty space or protein, 
    if there is none then one of our own organs, and if there is none then default back the direction we were growing in.
    (and this should be a seperate function for readability and to reuse it in free_grow())
    Codeium suggestion:

    for enemy_dir in string:
        enemy_x, enemy_y = new_x + directions[string.index(enemy_dir)][0], new_y + directions[string.index(enemy_dir)][1]
        if 0 <= enemy_x < width and 0 <= enemy_y < height and (enemy_x, enemy_y) in entities and entities[(enemy_x, enemy_y)][1] == 0:
            direction = enemy_dir
            break
    else:
        for empty_dir in string:
            empty_x, empty_y = new_x + directions[string.index(empty_dir)][0], new_y + directions[string.index(empty_dir)][1]
            if 0 <= empty_x < width and 0 <= empty_y < height and (empty_x, empty_y) not in entities:
                direction = empty_dir
                break
        else:
            for protein_dir in string:
                protein_x, protein_y = new_x + directions[string.index(protein_dir)][0], new_y + directions[string.index(protein_dir)][1]
                if 0 <= protein_x < width and 0 <= protein_y < height and grid[protein_y][protein_x] in ['A', 'B', 'C', 'D']:
                    direction = protein_dir
                    break
            else:
                for my_dir in string:
                    my_x, my_y = new_x + directions[string.index(my_dir)][0], new_y + directions[string.index(my_dir)][1]
                    if 0 <= my_x < width and 0 <= my_y < height and (my_x, my_y) in entities and entities[(my_x, my_y)][1] == 1:
                        direction = my_dir
                        break
                else:
    """
    print(f"HUNT {closest_organ_ids[organism_index]} {new_x} {new_y} {hunter}", file=sys.stderr, flush=True)
    my_entities[organism_id][(new_x, new_y)] = (hunter, 1, None, organ_parent_id, organ_root_id)
    grid[new_y][new_x] = hunter
    subtract_costs(hunter)
    return f"GROW {closest_organ_ids[organism_index]} {new_x} {new_y} {hunter} {direction_str if hunter in ['TENTACLE', 'HARVESTER'] else ''}"

def tentacle():
    # Perform BFS to check if there's an enemy organ two steps away
    print("Checking if we should grow a tentacle", file=sys.stderr, flush=True)
    target = None
    trimmed_spaces = set()
    for organ_id, direction_str, (adj_x, adj_y) in its_free_spaces:
        if (adj_x, adj_y) not in trimmed_spaces: 
            trimmed_spaces.add((adj_x, adj_y))
            path = [(adj_x, adj_y)]
            for dx, dy in directions:
                new_x, new_y = adj_x + dx, adj_y + dy

                # Check bounds and if current position is an enemy organ:
                if 0 <= new_x < width and 0 <= new_y < height and (new_x, new_y) in entities and entities[(new_x, new_y)][1] == 0:
                    attack = path + [(new_x, new_y)]  # Return the path to the enemy organ
                    direction = ''
                    if attack[0][0] > attack[1][0]:
                        direction = 'W'
                    elif attack[0][0] < attack[1][0]:
                        direction = 'E'
                    elif attack[0][1] > attack[1][1]:
                        direction = 'N'
                    elif attack[0][1] < attack[1][1]:
                        direction = 'S'
                    print(f"GROW {organ_id} {attack[0][0]} {attack[0][1]} TENTACLE {direction} to attack {attack[1][0]} {attack[1][1]}", file=sys.stderr, flush=True)
                    my_entities[organism_id][(attack[0][0], attack[0][1])] = ('TENTACLE', 1, None, organ_parent_id, organ_root_id)
                    grid[attack[0][1]][attack[0][0]] = 'TENTACLE'
                    subtract_costs('TENTACLE')
                    return f"GROW {organ_id} {attack[0][0]} {attack[0][1]} TENTACLE {direction}"


def free_grow(filler):
    print(f"Checking if we should just grow a {filler} organ", file=sys.stderr, flush=True)
    # If there's no proteins available:
    for organ_id, direction_str, (adj_x, adj_y) in its_free_spaces:
        if grid[adj_y][adj_x] == '': # Check if the tile is still empty
            print(f"GROW {organ_id} {adj_x} {adj_y} {filler} {direction_str if filler in ['TENTACLE', 'HARVESTER'] else ''}", file=sys.stderr, flush=True)
            my_entities[organism_id][(adj_x, adj_y)] = (filler, 1, None, organ_parent_id, organ_root_id)
            grid[adj_y][adj_x] = filler
            subtract_costs(filler)
            return f"GROW {organ_id} {adj_x} {adj_y} {filler} {direction_str if filler in ['TENTACLE', 'HARVESTER'] else ''}"

width, height = [int(i) for i in input().split()]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # S, E, N, W
string = ["S", "E", "N", "W"]
#-----------------------------------------------------------------------------------------------------------------#
# Game loop
while True:
    first_loop = True
    global retrying
    retrying = False

    entity_count = int(input())
    entities = dict()  # Dictionary to store entity information
    grid = [['' for _ in range(width)] for _ in range(height)]  # Initialize grid
    my_root_ids = []
    my_entities = dict()
    my_sporers = dict()
    my_harvesters = []
    my_farm_count = 0
    my_farm_locs = dict()
    enemy_harvesters = []
    enemy_farm_locs = dict()
    red_cells = set()
    loose_proteins = 0

    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        type_ = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        organ_dir = inputs[5]  # N,E,S,W or X if not an organ
        organ_parent_id = int(inputs[6])
        organ_root_id = int(inputs[7])
        entities[(x, y)] = (type_, owner, organ_id, organ_parent_id, organ_root_id)
        grid[y][x] = type_  # Fill the grid with the entity type_
        if owner == 1:
            if type_ == 'ROOT':
                my_root_ids.append(organ_id)
            if organ_root_id not in my_entities:
                my_entities[organ_root_id] = dict()
            my_entities[organ_root_id][(x, y)] = (type_, owner, organ_id, organ_parent_id, organ_root_id)
            if type_ == 'SPORER':
                if organ_parent_id not in my_sporers:
                    my_sporers[organ_parent_id] = []
                my_sporers[organ_parent_id].append((x, y, organ_id, organ_dir))
            if type_ == 'HARVESTER':
                my_harvesters.append((x, y, organ_dir))

        elif owner == 0:
            if type_ == 'TENTACLE':
                direction_vector = directions[string.index(organ_dir)]
                red_cell = (x + direction_vector[0], y + direction_vector[1])
                red_cells.add(red_cell)
            if type_ == 'HARVESTER':
                enemy_harvesters.append((x, y, organ_dir))


        if type_ in ['A', 'B', 'C', 'D']:
            loose_proteins += 1

    for x, y, organ_dir in my_harvesters:
        dx, dy = directions[string.index(organ_dir)]
        protein_x, protein_y = (x + dx, y + dy)
        if 0 <= protein_x < width and 0 <= protein_y < height:
            entity = grid[protein_y][protein_x]
            if entity in ['A', 'B', 'C', 'D']:
                if (protein_x, protein_y) not in my_farm_locs:
                    my_farm_count += 1  
                    my_farm_locs[(protein_x, protein_y)] = entity

    for x, y, organ_dir in enemy_harvesters:
        dx, dy = directions[string.index(organ_dir)]
        protein_x, protein_y = (x + dx, y + dy)
        if 0 <= protein_x < width and 0 <= protein_y < height:
            entity = grid[protein_y][protein_x]
            if entity in ['A', 'B', 'C', 'D']:
                if (protein_x, protein_y) not in enemy_farm_locs:
                    enemy_farm_locs[(protein_x, protein_y)] = entity

    loose_proteins -= my_farm_count

    # Print the grid for debugging
    print("Grid:", grid, file=sys.stderr, flush=True)

    # Your protein stock
    global my_a, my_b, my_c, my_d
    my_a, my_b, my_c, my_d = [int(i) for i in input().split()]
    # Opponent's protein stock
    opp_a, opp_b, opp_c, opp_d = [int(i) for i in input().split()]
    required_actions_count = int(input())

    """ Replacing with wrapper(function):
    for organism_index in range(required_actions_count):
        organism_id = my_root_ids[organism_index]
        print("Organism:", organism_index, f"'{organism_id}'", file=sys.stderr, flush=True)
        organism_entities = my_entities[organism_id]
    """
#------------------------------------------------------------------------------------------------#
    while first_loop or retrying:
        if retrying:
            print("Retrying", file=sys.stderr, flush=True)
        # Logic to determine where to grow
        commands = [""] * required_actions_count
        adj_free_spaces = [] # Will be filled with each of my organism's list of adjacent free spaces
        closest_proteins = [None for _ in range(required_actions_count)]
        closest_paths = [None for _ in range(required_actions_count)]
        closest_organ_ids = [None for _ in range(required_actions_count)]

        global organism_index
        for organism_index in range(required_actions_count):
            organism_id = my_root_ids[organism_index]
            organism_entities = my_entities[organism_id]
            adj_free_spaces.append(find_spaces())

        for organism_index, command in enumerate(commands):
            organism_id = my_root_ids[organism_index]
            organism_entities = my_entities[organism_id]
            its_free_spaces = adj_free_spaces[organism_index]
            for starting_id, direction_str, (first_x, first_y) in its_free_spaces:
                # Perform BFS to find the nearest protein source
                path = bfs(first_x, first_y, grid, width, height)
                if path:
                    # If a path is found, check if it's the closest one
                    if closest_paths[organism_index] is None or len(path) < len(closest_paths[organism_index]):
                        closest_organ_ids[organism_index] = starting_id  # Store the organ ID that can grow
                        closest_paths[organism_index] = [direction_str] + path
                        closest_proteins[organism_index] = path[-1]  # Get the protein source position
            print(f"Path for organism {organism_index}:", closest_paths[organism_index], file=sys.stderr, flush=True)

        # Check if we should build a ROOT with a HARVESTER
            organism_id = my_root_ids[organism_index]
            if organism_id in my_sporers and loose_proteins > 0 and my_a > 0 and my_b > 0 and my_c > 1 and my_d > 1:
                commands[organism_index] = wrapper(organism_index, root_farm) or ""
            print("Command:", command, file=sys.stderr, flush=True)

        # Check if we should grow a SPORER-to-HARVESTER_chain
            if commands[organism_index] == "" and loose_proteins > 0 and my_a > 0 and my_b > 1 and my_c > 1 and my_d > 2:
                sporer_spaces = wrapper(organism_index, find_spaces)
                print("Available adjacent spaces:", sporer_spaces, file=sys.stderr, flush=True)
                if sporer_spaces:
                    commands[organism_index] = wrapper(organism_index, spore_root_farm, sporer_spaces) or ""
            print("Command:", command, file=sys.stderr, flush=True)

        # Check if we can grow a HARVESTER
            if commands[organism_index] == "" and closest_paths[organism_index]:
                if my_c > 0 and my_d > 0 and len(closest_paths[organism_index]) == 3:  # If the path is two steps long:
                    commands[organism_index] = wrapper(organism_index, farm) or ""
                # If we cannot grow a HARVESTER, grow another organ towards the closest protein
                elif my_b > 0 and my_c > 1: # So have extra protein for a harvester when we get there.
                    commands[organism_index] = wrapper(organism_index, hunting_path, organ_type="TENTACLE") or ""
                elif my_a > 0: 
                    commands[organism_index] = wrapper(organism_index, hunting_path, organ_type="BASIC") or ""
                elif my_b > 0 and my_c > 0:
                    commands[organism_index] = wrapper(organism_index, hunting_path, organ_type="TENTACLE") or ""
                elif my_b > 0 and my_d > 0:
                    commands[organism_index] = wrapper(organism_index, hunting_path, organ_type="SPORER") or ""
                elif my_c > 0 and my_d > 0:
                    commands[organism_index] = wrapper(organism_index, hunting_path, organ_type="HARVESTER") or ""
            print("Command:", command, file=sys.stderr, flush=True)
        print("Farming commands:", commands, file=sys.stderr, flush=True)

        # Check for TENTACLE growth
        for organism_index, command in enumerate(commands):
            if command == "": # If there's no proteins available to harvest:
                commands[organism_index] = (my_b > 0 and my_c > 0 and (wrapper(organism_index, tentacle) or \
                    wrapper(organism_index, free_grow, organ_type="TENTACLE"))) or \
                    (my_a > 0 and wrapper(organism_index, free_grow, organ_type="BASIC")) or \
                    (my_b > 0 and my_d > 0 and wrapper(organism_index, free_grow, organ_type="SPORER")) or \
                    (my_c > 0 and my_d > 0 and wrapper(organism_index, free_grow, organ_type="HARVESTER")) or \
                            ""
        print("Commands:", commands, file=sys.stderr, flush=True)

        if all(command == "" for command in commands) and first_loop:
            print("We need to retry", file=sys.stderr, flush=True)
            retrying = True

        elif retrying:
            retrying = False
        first_loop = False
    

    for organism_index, command in enumerate(commands):
        if command == "":
            command = "WAIT"
        print(command)

    print("My proteins:", my_a, my_b, my_c, my_d, file=sys.stderr, flush=True)