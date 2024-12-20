import sys
from collections import deque

def bfs(start_x, start_y, grid, width, height):
    queue = deque([(start_x, start_y, [])])  # (x, y, path)
    visited = farm_locs.copy()  # Use a deep copy of farm_locs to not modify the original set
    visited.add((start_x, start_y))

    while queue:
        x, y, path = queue.popleft()
        
        # Check if current position is a protein source
        if grid[y][x] in ['A', 'B', 'C', 'D'] and (x, y) not in farm_locs:
            return path + [(x, y)]  # Return the path to the protein source
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check bounds and if not visited
            if 0 <= new_x < width and 0 <= new_y < height and (new_x, new_y) not in visited:
                if grid[new_y][new_x] not in ['WALL', 'ROOT', 'BASIC', 'HARVESTER']:  # Ensure not moving into walls
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, path + [(x, y)]))
    
    return None  # No path found

def farm():
    print("Checking if we should farm", file=sys.stderr, flush=True)
    target_x, target_y = closest_protein  # Get the last position in the path
    # Determine direction to the protein source
    adjacent_tile = closest_path[1]  # The second step in the path
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
    my_entities[organism_id][(adj_x, adj_y)] = ('HARVESTER', 1, None, organ_parent_id, organ_root_id)
    grid[adj_y][adj_x] = 'HARVESTER'
    return f"GROW {closest_organ_id} {adj_x} {adj_y} HARVESTER {direction_to_protein}"

def find_spaces():
    sporer_spaces = []
    for key, value in organism_entities.items():
        (start_x, start_y) = key
        (type_, owner, organ_id, organ_parent_id, organ_root_id) = value
        if owner == 1:
            for dx, dy in directions:
                new_x, new_y = start_x + dx, start_y + dy
                if 0 <= new_x < width and 0 <= new_y < height and (new_x, new_y) not in entities:
                    sporer_spaces.append((organ_id, (new_x, new_y)))

    return sporer_spaces
                    
def spore_root_farm(sporer_spaces):
    print("Checking if we should grow a sporer", file=sys.stderr, flush=True)
    for space in sporer_spaces:
        roots_visited = set()
        sporer_loc = space[1]
        sporer_x, sporer_y = sporer_loc
        for (dx, dy), direction in zip(directions, string):
            root_x, root_y = sporer_x + dx, sporer_y + dy
            print(f"Checking from space {sporer_x} {sporer_y} towards {direction}", file=sys.stderr, flush=True)
            while 0 <= root_x < width and 0 <= root_y < height:
                print(f"Checking space {root_x} {root_y}", file=sys.stderr, flush=True)
                if (root_x, root_y) not in roots_visited and (root_x, root_y) not in entities:
                    roots_visited.add((root_x, root_y))
                    harvests_visited = set()
                    for hx, hy in directions:
                        harvest_x, harvest_y = root_x + hx, root_y + hy
                        if (harvest_x, harvest_y) != sporer_loc and \
                            (harvest_x, harvest_y) not in harvests_visited and \
                            (harvest_x, harvest_y) not in entities and \
                            0 <= harvest_x < width and 0 <= harvest_y < height:
                                harvests_visited.add((harvest_x, harvest_y))
                                for px, py in directions:
                                    protein_x, protein_y = harvest_x + px, harvest_y + py
                                    if 0 <= protein_x < width and 0 <= protein_y < height and \
                                        grid[protein_y][protein_x] in ['A', 'B', 'C', 'D'] and \
                                        (protein_x, protein_y) not in farm_locs:
                                            print(f"GROW {space[0]} {sporer_x} {sporer_y} SPORER {direction}", file=sys.stderr, flush=True)
                                            my_entities[organism_id][(sporer_x, sporer_y)] = ('SPORER', 1, None, organ_parent_id, organ_root_id)
                                            grid[sporer_y][sporer_x] = 'SPORER'
                                            return f"GROW {space[0]} {sporer_x} {sporer_y} SPORER {direction}"
                root_x, root_y = root_x + dx, root_y + dy

def root_farm():
    print("Checking if we should grow a root", file=sys.stderr, flush=True)
    for sporer_x, sporer_y, organ_id, organ_dir in sporers:
        harvests_visited = set()
        dx, dy = directions[string.index(organ_dir)]
        root_x, root_y = sporer_x + dx, sporer_y + dy
        print(f"Checking from sporer {sporer_x} {sporer_y} towards {organ_dir}", file=sys.stderr, flush=True)
        while 0 <= root_x < width and 0 <= root_y < height and (root_x, root_y) not in entities:
            print(f"Checking space {root_x} {root_y}", file=sys.stderr, flush=True)
            for (hx, hy), direction in zip(directions, string):
                harvest_x, harvest_y = root_x + hx, root_y + hy
                if 0 <= harvest_x < width and 0 <= harvest_y < height and \
                    (harvest_x, harvest_y) not in harvests_visited and \
                    (harvest_x, harvest_y) not in entities:
                        harvests_visited.add((harvest_x, harvest_y))
                        for px, py in directions:
                            protein_x, protein_y = harvest_x + px, harvest_y + py
                            if 0 <= protein_x < width and 0 <= protein_y < height and \
                                grid[protein_y][protein_x] in ['A', 'B', 'C', 'D'] and \
                                    (protein_x, protein_y) not in farm_locs:
                                        print(f"SPORE {organ_id} {root_x} {root_y} ROOT", file=sys.stderr, flush=True)
                                        my_entities[organism_id][(root_x, root_y)] = ('ROOT', 1, None, organ_parent_id, organ_root_id)
                                        grid[root_y][root_x] = 'ROOT'
                                        return f"SPORE {organ_id} {root_x} {root_y}"
            root_x, root_y = root_x + dx, root_y + dy

def hunting_path(hunter):
    print(f"Checking if we should grow towards a {hunter} protein", file=sys.stderr, flush=True)
    # Find the first step in the path to grow a BASIC organ
    next_step = closest_path[1]  # The next step in the path
    new_x, new_y = next_step
    print(f"HUNT {closest_organ_id} {new_x} {new_y} {hunter}", file=sys.stderr, flush=True)
    my_entities[organism_id][(new_x, new_y)] = (hunter, 1, None, organ_parent_id, organ_root_id)
    grid[new_y][new_x] = hunter
    return f"GROW {closest_organ_id} {new_x} {new_y} {hunter}"

def tentacle():
    print("Checking if we should grow a tentacle", file=sys.stderr, flush=True)
    target = None
    for key, value in organism_entities.items():
        (start_x, start_y) = key
        (type_, owner, organ_id, organ_parent_id, organ_root_id) = value
        if owner == 1:  # Check only your organs
            # Perform BFS to check if there's an enemy organ two steps away
            queue = deque([(start_x, start_y, [], 0)])  # (x, y, path, depth)
            visited = set()
            visited.add((start_x, start_y))

            while queue:
                x, y, path, depth = queue.popleft()
                if depth > 1:
                    continue
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    # Check bounds and if not visited
                    if 0 <= new_x < width and 0 <= new_y < height and (new_x, new_y) not in visited:
                    # Check if current position is an enemy organ
                        if (new_x, new_y) in  entities and entities[(new_x, new_y)][1] == 0 and len(path) == 1:  # Check if the entity is an enemy organ
                            attack = path + [(new_x, new_y)]  # Return the path to the enemy organ
                            print(f"Attack_route: {attack}", file=sys.stderr, flush=True)
                            adj_organ_id = entities[(start_x, start_y)][2]
                            direction = ''
                            if attack[0][0] > attack[1][0]:
                                direction = 'W'
                            elif attack[0][0] < attack[1][0]:
                                direction = 'E'
                            elif attack[0][1] > attack[1][1]:
                                direction = 'N'
                            elif attack[0][1] < attack[1][1]:
                                direction = 'S'
                            print(f"GROW {adj_organ_id} {attack[0][0]} {attack[0][1]} TENTACLE {direction}", file=sys.stderr, flush=True)
                            my_entities[organism_id][(attack[0][0], attack[0][1])] = ('TENTACLE', 1, None, organ_parent_id, organ_root_id)
                            grid[attack[0][1]][attack[0][0]] = 'TENTACLE'
                            return f"GROW {adj_organ_id} {attack[0][0]} {attack[0][1]} TENTACLE {direction}"
                        elif grid[new_y][new_x] not in ['WALL', 'ROOT', 'BASIC', 'HARVESTER', 'TENTACLE']:  # Ensure not moving into walls
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y, path + [(new_x, new_y)], depth + 1))


def free_grow(filler):
    print("Checking if we should just grow filler organs", file=sys.stderr, flush=True)
    # If there's no proteins available:
    for key, value in organism_entities.items():
        (x, y) = key
        (type_, owner, organ_id, organ_parent_id, organ_root_id) = value
        if owner == 1:
            # Check adjacent tiles for growing a BASIC organ

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < width and 0 <= new_y < height:
                    # Check if the tile is empty
                    if grid[new_y][new_x] == '':
                        print(f"GROW {organ_id} {new_x} {new_y} {filler}", file=sys.stderr, flush=True)
                        my_entities[organism_id][(new_x, new_y)] = (filler, 1, None, organ_parent_id, organ_root_id)
                        grid[new_y][new_x] = filler
                        return f"GROW {organ_id} {new_x} {new_y} {filler}"

width, height = [int(i) for i in input().split()]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # S, E, N, W
string = ["S", "E", "N", "W"]
#-----------------------------------------------------------------------------------------------------------------#
# Game loop
while True:
    command = ""

    entity_count = int(input())
    entities = dict()  # Dictionary to store entity information
    grid = [['' for _ in range(width)] for _ in range(height)]  # Initialize grid
    my_root_ids = []
    my_entities = dict()
    sporers = []
    harvesters = []
    farm_count = 0
    farm_locs = set()
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
                sporers.append((x, y, organ_id, organ_dir))
            if type_ == 'HARVESTER':
                harvesters.append((x, y, organ_dir))
        if type_ in ['A', 'B', 'C', 'D']:
            loose_proteins += 1

    for x, y, organ_dir in harvesters:
        dx, dy = directions[string.index(organ_dir)]
        protein_loc = (x + dx, y + dy)
        if grid[protein_loc[1]][protein_loc[0]] in ['A', 'B', 'C', 'D'] and \
            protein_loc not in farm_locs:
                farm_count += 1
                farm_locs.add(protein_loc)

    loose_proteins -= farm_count

    # Print the grid for debugging
    print("Grid:", grid, file=sys.stderr, flush=True)

    # Your protein stock
    my_a, my_b, my_c, my_d = [int(i) for i in input().split()]
    # Opponent's protein stock
    opp_a, opp_b, opp_c, opp_d = [int(i) for i in input().split()]
    required_actions_count = int(input())

    for organism_index in range(required_actions_count):
        organism_id = my_root_ids[organism_index]
        print("Organism:", organism_index, f"'{organism_id}'", file=sys.stderr, flush=True)
        organism_entities = my_entities[organism_id]
#------------------------------------------------------------------------------------------------#
        # Logic to determine where to grow
        closest_protein = None
        closest_path = None
        closest_organ_id = None
        direction_to_protein = None

        for key, value in organism_entities.items():
            (x, y) = key
            (type_, owner, organ_id, organ_parent_id, organ_root_id) = value
            # Perform BFS to find the nearest protein source
            path = bfs(x, y, grid, width, height)
            if path:
                # If a path is found, check if it's the closest one
                if closest_path is None or len(path) < len(closest_path):
                    closest_path = path
                    closest_protein = path[-1]  # Get the protein source position
                    closest_organ_id = organ_id  # Store the organ ID that can grow
        print("Path:", closest_path, file=sys.stderr, flush=True)

        # Check if we should build a ROOT with a HARVESTER
        if sporers and loose_proteins > 0 and my_a > 0 and my_b > 0 and my_c > 1 and my_d > 1:
            command = root_farm() or ""

        # Check if we should grow a SPORER-to-HARVESTER_chain
        if command == "" and loose_proteins > 0 and my_a > 0 and my_b > 1 and my_c > 1 and my_d > 2:
            sporer_spaces = find_spaces()
            print("Available adjacent spaces:", sporer_spaces, file=sys.stderr, flush=True)
            if sporer_spaces:
                command = spore_root_farm(sporer_spaces) or ""

        # Check if we can grow a HARVESTER
        if command == "" and closest_path:
            if my_c > 0 and my_d > 0 and len(closest_path) == 3:  # If the path is two steps long:
                command = farm() or ""
            elif my_a > 0: # If we cannot grow a HARVESTER, grow a BASIC organ
                # Find the closest protein and grow a BASIC organ
                command = hunting_path("BASIC") or ""
            elif my_c > 0 and my_d > 0:
                command = hunting_path("HARVESTER") or ""

        # Check for TENTACLE growth
        elif command == "": # If there's no proteins available to harvest:
            if my_b > 0 and my_c > 0:  # Check if we have enough proteins to grow a TENTACLE
                command = tentacle() or ""
            elif my_a > 0:    
                command = free_grow("BASIC") or ""
            elif my_c > 0 and my_d > 0:
                command = free_grow("HARVESTER") or ""

        if command == "":
            command = "WAIT"
        print(command)
        command = ""