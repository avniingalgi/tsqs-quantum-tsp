import math
from tsp_data import distance_matrix
from cost_function import compute_cost

def decode_result(counts):

    best_state = max(counts, key=counts.get)
    best_state = best_state.split()[0]

    print("Best quantum state:", best_state)

    n = len(distance_matrix)
    k = math.ceil(math.log2(n))

    route = []
    used = set()

    # Step 1: Decode into cities
    for i in range(0, len(best_state), k):
        bits = best_state[i:i+k]
        city = int(bits, 2)

        if city < n and city not in used:
            route.append(city)
            used.add(city)

    # Step 2: Add missing cities
    for city in range(n):
        if city not in used:
            route.append(city)

    # Step 3: Compute cost
    cost = compute_cost(route, distance_matrix)

    return route, cost