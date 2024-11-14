from typing import List

# Brute force:
def findOptimalCohort(groups: List[int], targetRatio: float) -> List[int]:
    total_users = sum(groups)
    target_count = total_users * targetRatio
    groups.sort()  # Sort groups to ensure lexicographic order
    best_cohort = []
    best_diff = float('inf')

    def backtrack(start, current_cohort, current_size):
        nonlocal best_cohort, best_diff
        
        if current_size > target_count:  # Prune if over target
            return
        
        if current_size > 0:  # Only consider non-empty cohorts
            current_ratio = current_size / total_users
            current_diff = abs(current_ratio - targetRatio)
            
            # Update best cohort if this one is better
            if (current_diff < best_diff) or (current_diff == best_diff and len(current_cohort) < len(best_cohort) or (len(current_cohort) == len(best_cohort) and sorted(current_cohort) < sorted(best_cohort))):
                best_diff = current_diff
                best_cohort = sorted(current_cohort)

        for i in range(start, len(groups)):
            backtrack(i + 1, current_cohort + [groups[i]], current_size + groups[i])

    backtrack(0, [], 0)
    return best_cohort

# Example usage:
print(findOptimalCohort([5, 3, 7, 4, 4, 1], 0.5))  # Output: [1, 4, 7]
print(findOptimalCohort([245, 165, 144, 217, 114, 107, 81, 166], 0.7))  # Expected Output: [81, 165, 166, 217, 245]

# Pruning:
def findOptimalCohort(groups: List[int], targetRatio: float) -> List[int]:
    total_users = sum(groups)
    target_count = total_users * targetRatio
    groups.sort()  # Sort groups to ensure lexicographic order
    best_cohort = []
    best_diff = float('inf')

    def backtrack(start, current_cohort, current_size):
        nonlocal best_cohort, best_diff
        
        if current_size > target_count:  # Prune if over target
            return
        
        if current_size > 0:  # Only consider non-empty cohorts
            current_ratio = current_size / total_users
            current_diff = abs(current_ratio - targetRatio)
            
            # Update best cohort if this one is better
            if (current_diff < best_diff) or (current_diff == best_diff and 
                                              len(current_cohort) < len(best_cohort) or (len(current_cohort) == len(best_cohort) and 
                                                                                         sorted(current_cohort) < sorted(best_cohort))):
                best_diff = current_diff
                best_cohort = sorted(current_cohort)

        for i in range(start, len(groups)):
            backtrack(i + 1, current_cohort + [groups[i]], current_size + groups[i])

    backtrack(0, [], 0)
    return best_cohort

# Example usage:
passing = [5, 3, 7, 4, 4, 1]
target_ratio = 0.5
result = findOptimalCohort(passing, target_ratio)
print(result, sum(result), sum(passing), sum(passing) * target_ratio)  # Output: [1, 3, 4, 4] , not [1, 4, 7]
passing = [245, 165, 144, 217, 114, 107, 81, 166]
target_ratio = 0.7
result = findOptimalCohort(passing, target_ratio)
print(result, sum(result), sum(result)/sum(passing), sum(passing), sum(passing) * target_ratio)  # Output: [81, 107, 114, 144, 166, 245], but supposed to be [81, 165, 166, 217, 245]
print(sum([81, 165, 166, 217, 245]), sum([81, 165, 166, 217, 245])/sum(passing))