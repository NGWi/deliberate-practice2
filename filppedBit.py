from typing import List

# The following failed for extremely long binaries:
def findInvalidMetric(metrics: List[str]) -> List[int]:
    # Dictionary to store the metrics and their indices
    metrics_dict = dict()
    
    # Iterate through each metric
    for index, metric in enumerate(metrics):
        # Generate all possible variations by flipping each bit
        for i in range(len(metric)):
            # Create a new metric by flipping the i-th bit
            flip = '1' if metric[i] == '0' else '0'
            flipped = metric[:i] + flip + metric[i+1:]
            
            # Check if the flipped metric is already in the metrics_dict dictionary
            if flipped in metrics_dict:
                # If found, return the indices of the two metrics
                return sorted([metrics_dict[flipped], index])
        
        # Store the current metric in the metrics_dict dictionary
        metrics_dict[metric] = index
    
    # If no pair is found, return an empty list (though the problem guarantees a solution)
    return []

# Example usage
metrics = ["011", "110", "001"]
print(findInvalidMetric(metrics))  # Output: [0, 2]