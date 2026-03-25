import itertools
import math
from tsp_data import distance_matrix
from cost_function import compute_cost

def apply_cost_oracle(qc, total_qubits):

    n = len(distance_matrix)
    k = math.ceil(math.log2(n))

    # Step 1: Generate all routes
    all_routes = list(itertools.permutations(range(n)))

    # Step 2: Find best route
    best_route = None
    min_cost = float('inf')

    for route in all_routes:
        cost = compute_cost(list(route), distance_matrix)

        if cost < min_cost:
            min_cost = cost
            best_route = route

    print("Best route (classical):", best_route)
    print("Minimum cost:", min_cost)

    # Step 3: Convert route to HOBO binary
    target_state = ""

    for city in best_route:
        binary = format(city, f'0{k}b')  # k-bit binary
        target_state += binary

    # Step 4: Match total_qubits
    target_state = target_state.ljust(total_qubits, '0')

    # Step 5: Apply phase flip
    for i in range(total_qubits):
        if target_state[i] == '0':
            qc.x(i)

    qc.h(total_qubits - 1)
    qc.mcx(list(range(total_qubits - 1)), total_qubits - 1)
    qc.h(total_qubits - 1)

    for i in range(total_qubits):
        if target_state[i] == '0':
            qc.x(i)

    return qc