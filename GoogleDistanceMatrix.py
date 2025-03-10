import googlemaps

def get_matrix(locations):
    API_key = 'GM_KEY'  # Replace with your actual API key
    gmaps = googlemaps.Client(key=API_key)
    matrix_result = gmaps.distance_matrix(locations, locations, mode="driving")
    return matrix_result


def structure_driving_time(matrix_result):
    driving_time_matrix = []
    for row in matrix_result['rows']:
        driving_time_row = []
        for element in row['elements']:
            if element['status'] == 'OK':
                driving_time_row.append(element['duration']['value'])  # Duration in seconds
            else:
                driving_time_row.append(float('inf'))  # Use infinity for unreachable routes
        driving_time_matrix.append(driving_time_row)
    return driving_time_matrix

if __name__ == "__main__":
    locations = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Phoenix, AZ"
    ]
    matrix_result = get_matrix(locations)
    driving_time_matrix = structure_driving_time(matrix_result)

    print("Driving Time Matrix:")
    for row in driving_time_matrix:
        print(row)