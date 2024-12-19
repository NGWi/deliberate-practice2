import sys
from collections import deque

def bfs(start_x, start_y, grid, width, height):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
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

def farm(farm_count):
    target_x, target_y = closest_protein  # Get the last position in the path
    # Determine direction to the protein source
    adjacent_tile = closest_path[1]  # The second step in the path
    adj_y, adj_x = adjacent_tile
    if adj_y < target_y:  # Protein is below
        direction_to_protein = 'S'
    elif adj_y > target_y:  # Protein is above
        direction_to_protein = 'N'
    elif adj_x < target_x:  # Protein is to the right
        direction_to_protein = 'E'
    elif adj_x > target_x:  # Protein is to the left
        direction_to_protein = 'W'

    farm_count += 1
    farm_locs.add((target_x, target_y))
    print(f"GROW {closest_organ_id} {adj_x} {adj_y} HARVESTER {direction_to_protein}", file=sys.stderr, flush=True)
    return f"GROW {closest_organ_id} {adj_x} {adj_y} HARVESTER {direction_to_protein}"

def basic_path():
    # Find the first step in the path to grow a BASIC organ
    next_step = closest_path[1]  # The next step in the path
    new_x, new_y = next_step
    print(f"HUNT {closest_organ_id} {new_x} {new_y} BASIC", file=sys.stderr, flush=True)
    return f"GROW {closest_organ_id} {new_x} {new_y} BASIC"

def free_grow():
    # If there's no proteins available:
    for x, y, type, owner, organ_id, organ_parent_id, organ_root_id in entities:
        if owner == 1:
            # Check adjacent tiles for growing a BASIC organ
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # S, E, N, W
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < width and 0 <= new_y < height:
                    # Check if the tile is empty
                    if grid[new_y][new_x] == '':
                        print(f"GROW {organ_id} {new_x} {new_y} BASIC", file=sys.stderr, flush=True)
                        return f"GROW {organ_id} {new_x} {new_y} BASIC"

# Game loop
width, height = [int(i) for i in input().split()]

farm_count = 0
farm_locs = set()

while True:
    command = ""

    entity_count = int(input())
    entities = []  # List to store entity information
    grid = [['' for _ in range(width)] for _ in range(height)]  # Initialize grid
    loose_proteins = -farm_count

    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        type = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        organ_dir = inputs[5]  # N,E,S,W or X if not an organ
        organ_parent_id = int(inputs[6])
        organ_root_id = int(inputs[7])
        entities.append((x, y, type, owner, organ_id, organ_parent_id, organ_root_id))
        grid[y][x] = type  # Fill the grid with the entity type
        if type in ['A', 'B', 'C', 'D']:
            loose_proteins += 1

    # Print the grid for debugging
    print("Grid:", grid, file=sys.stderr, flush=True)

    # Your protein stock
    my_a, my_b, my_c, my_d = [int(i) for i in input().split()]
    # Opponent's protein stock
    opp_a, opp_b, opp_c, opp_d = [int(i) for i in input().split()]
    required_actions_count = int(input())

    closest_protein = None
    closest_path = None
    closest_organ_id = None
    direction_to_protein = None

#------------------------------------------------------------------------------------------------#
    # Logic to determine where to grow
    for x, y, type, owner, organ_id, organ_parent_id, organ_root_id in entities:
        if owner == 1:  # Check only your organs
            # Perform BFS to find the nearest protein source
            path = bfs(x, y, grid, width, height)
            if path:
                # If a path is found, check if it's the closest one
                if closest_path is None or len(path) < len(closest_path):
                    closest_path = path
                    closest_protein = path[-1]  # Get the protein source position
                    closest_organ_id = organ_id  # Store the organ ID that can grow
    print("Path:", closest_path, file=sys.stderr, flush=True)

    if closest_path: # Check if we can grow a HARVESTER
        if my_c > 0 and my_d > 0 and len(closest_path) == 3:  # If the path is two steps long:
            command = farm(farm_count) or ""
        else: # If we cannot grow a HARVESTER, grow a BASIC organ
            # Find the closest protein and grow a BASIC organ
            command = basic_path() or ""
    else: # If there's no proteins available:
        command = free_grow() or ""

    if command == "": # Just in case...
        command = "WAIT"
    print(command)