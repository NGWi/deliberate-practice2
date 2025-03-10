import subprocess
import json

def get_distance_matrix(locations):
    try:
        output = subprocess.check_output(
            ["python", "GoogleDistanceMatrix.py"] + locations, 
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        distance_matrix = eval(output.strip())  # Assuming the output is a string representation of a list
        return distance_matrix
    except subprocess.CalledProcessError as e:
        print(f"Error while calling GoogleDistanceMatrix.py: {e.stderr}")
    except SyntaxError:
        print("Invalid matrix format")
    return None

def get_fastest_route(distance_matrix):
    try:
        # Serialize the distance matrix to JSON
        matrix_json = json.dumps(distance_matrix)
        
        # Call travelingSalesman.py and pass the distance matrix
        process = subprocess.Popen(
            ['python', 'travelingSalesman.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Send the matrix JSON to the subprocess
        stdout, stderr = process.communicate(input=matrix_json.encode())
        
        if process.returncode != 0:
            print(f"Error in travelingSalesman.py: {stderr.decode()}")
            return None
        
        return json.loads(stdout.decode().strip())
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    user_input = ["San Francisco, CA", "Los Angeles, CA", "New York, NY", "Chicago, IL"]
    
    # Get distance matrix
    distance_matrix = get_distance_matrix(user_input)
    
    if distance_matrix is None:
        print("Failed to retrieve the distance matrix.")
        return
    
    print("Distance Matrix:")
    for row in distance_matrix:
        print(row)
        
    # Get fastest route
    result = get_fastest_route(distance_matrix)
    
    if result is None:
        print("Failed to retrieve the fastest route.")
        return
    
    time, path = result  # Assuming result is a tuple of (time, path)
    
    print(f"Minimum time: {time}")
    print(f"Optimal path: {path}")

if __name__ == "__main__":
    main()