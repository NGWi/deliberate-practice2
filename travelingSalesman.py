import itertools


# O(n^2*2^n):
def tsp_held_karp(distances):
    n = len(distances)
    C = {}

    # Base case: starting from city 0, visiting each city directly
    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], 0)

    # Iterate over subsets of size 2 to n-1 (excluding the start city 0)
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            subset_mask = sum(1 << city for city in subset)  # Mask for the subset
            for k in subset:
                prev_mask = subset_mask ^ (1 << k)  # Remove k from the subset
                min_cost = None
                for m in subset:
                    if m == k:
                        continue
                    if (prev_mask, m) in C:
                        cost = C[(prev_mask, m)][0] + distances[m][k]
                        if min_cost is None or cost < min_cost:
                            min_cost = cost
                            parent = m
                if min_cost is not None:
                    C[(subset_mask, k)] = (min_cost, parent)

    # All cities except the start (0) are visited
    all_visited = (1 << n) - 1 - 1  # Binary 111...1110 (exclude city 0)
    # Find the minimum cost to return to the start
    min_total = float('inf')
    last_city = -1
    for k in range(1, n):
        if (all_visited, k) in C:
            cost = C[(all_visited, k)][0] + distances[k][0]
            if cost < min_total:
                min_total = cost
                last_city = k

    # Reconstruct the path
    path = []
    mask = all_visited
    current = last_city
    for _ in range(n - 1):
        path.append(current)
        parent = C[(mask, current )][1]
        mask ^= (1 << current)  # Remove current from the mask
        current = parent
    path.append(0)  # Return to the starting city
    path.reverse()  # Reverse the path to start from city 0

    return min_total, path


if __name__ == "__main__":
    # Distance matrix (symmetric)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    cost, path = tsp_held_karp(distances)
    print("Minimum cost:", cost)
    print("Path:", path)