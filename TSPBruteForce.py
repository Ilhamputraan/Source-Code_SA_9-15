import itertools

def calculate_distance(path, dist_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += dist_matrix[path[i]][path[i + 1]]
    total_distance += dist_matrix[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_path = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(cities[1:]):  # Fix: Start permutations from the second city
        current_path = [0] + list(perm) + [0]  # Fix: Ensure the path starts and ends at the first city
        current_distance = calculate_distance(current_path, dist_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path
    
    return min_path, min_distance

# Contoh penggunaan
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = tsp_brute_force(dist_matrix)
print(f"Minimum cost: {distance}")
print(f"Path: {path}")