def tsp_greedy(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    path = [0]  # Start from the first city
    visited[0] = True
    total_cost = 0
    
    current_city = 0
    for _ in range(n - 1):
        next_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city] and dist_matrix[current_city][city] < min_distance:
                min_distance = dist_matrix[current_city][city]
                next_city = city
        visited[next_city] = True
        path.append(next_city)
        total_cost += min_distance
        current_city = next_city
    
    # Return to the starting city
    total_cost += dist_matrix[current_city][0]
    path.append(0)
    
    return path, total_cost

# Contoh penggunaan
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = tsp_greedy(dist_matrix)
print(f"Minimum cost: {distance}")
print(f"Path: {path}")