from itertools import combinations
import subprocess

# O(n^2*2^n):
def tsp_held_karp(distances):
    n = len(distances)
    if n <= 1:
        print("Invalid input. The number of locations must be at least 2.")
        return None, None
    sub_routes = dict()

    # Base case: starting from location 0, visiting each location directly
    for location in range(1, n):
        sub_routes[(1 << location, location)] = (distances[0][location], 0) # = distance, parent

    # Iterate over subsets of size 2 to n-1 (excluding the start location 0)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            subset_mask = sum(1 << location for location in subset)  # Mask for the subset
            for location in subset:
                prev_mask = subset_mask ^ (1 << location)  # Remove location from the subset
                min_cost = float('inf')
                for p in subset:
                    if p == location:
                        continue
                    if (prev_mask, p) in sub_routes:
                        cost = sub_routes[(prev_mask, p)][0] + distances[p][location]
                        if cost < min_cost:
                            min_cost = cost
                        parent = p
                if min_cost is not float('inf'):
                    sub_routes[(subset_mask, location)] = (min_cost, parent)

    # Compare best routes ending at each location
    # All locations except the start (0) are visited
    all_visited = (1 << n) - 2  # Binary 111...1110 (exclude location 0)

    # Find the minimum cost to return to the start
    min_total = float('inf')
    last_location = None
    for location in range(1, n):
        if (all_visited, location) in sub_routes:
            cost = sub_routes[(all_visited, location)][0] + distances[location][0]
            if cost < min_total:
                min_total = cost
                last_location = location

    # Reconstruct the path
    path = []
    mask = all_visited
    current = last_location
    for _ in range(n - 1):
        path.append(current)
        parent = sub_routes[(mask, current)][1]
        mask ^= (1 << current)  # Remove current from the mask
        current = parent
    path.append(0)  # Return to the starting location
    path.reverse()  # Reverse the path to start from location 0

    return min_total, path

def convert_seconds(seconds):
    days = seconds // (3600 * 24)
    seconds = seconds % (3600 * 24)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} days {hours} hours {minutes} minutes"

def main():
    try:
        output = subprocess.check_output(
            ["python", "GoogleDistanceMatrix.py"], 
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        distances = eval(output.strip())
        cost, path = tsp_held_karp(distances)
        print(f"Minimum cost: {convert_seconds(cost)}")
        print(f"Optimal path: {path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except SyntaxError:
        print("Invalid matrix format")

if __name__ == "__main__":
    main()