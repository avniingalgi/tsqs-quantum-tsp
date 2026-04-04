import math
from cost_function import compute_cost


def decode_result(counts,distance_matrix):

    # Sort states by probability
    sorted_states = sorted(counts, key=counts.get, reverse=True)

    n = len(distance_matrix)
    k = math.ceil(math.log2(n))

    best_route = None
    min_cost = float('inf')

    # Check top probable states
    for state in sorted_states[:10]:

        state = state.split()[0]

        route = []
        used = set()

        for i in range(0, len(state), k):
            bits = state[i:i+k]

            if len(bits) < k:
                continue

            # Proper binary decoding
            city = int(bits, 2)

            # Fix: ensure valid range
            city = city % n

            if city not in used:
                route.append(city)
                used.add(city)

        # Add missing cities
        for city in range(n):
            if city not in used:
                route.append(city)

        cost = compute_cost(route, distance_matrix)

        if cost < min_cost:
            min_cost = cost
            best_route = route

    return best_route, min_cost