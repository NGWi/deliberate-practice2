import googlemaps
import numpy as np

def get_driving_times(api_key, locations):
    gmaps = googlemaps.Client(key=api_key)
    n = len(locations)
    time_matrix = np.zeros((n, n))  # Matrix to store driving times in seconds

    for i in range(n):
        for j in range(n):
            if i != j:
                result = gmaps.distance_matrix(
                    origins=locations[i],
                    destinations=locations[j],
                    mode="driving",
                    units="metric"
                )
                # Extract duration in seconds
                time_seconds = result['rows'][0]['elements'][0]['duration']['value']
                time_matrix[i][j] = time_seconds

    return time_matrix

# Example usage
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"  # Replace with your key
    locations = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX"
    ]
    
    time_matrix = get_driving_times(API_KEY, locations)
    print("Driving Time Matrix (in seconds):")
    print(time_matrix)