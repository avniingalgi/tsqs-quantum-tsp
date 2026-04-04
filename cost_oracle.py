import itertools
import math
import numpy as np
from cost_function import compute_cost


def apply_cost_oracle(qc, total_qubits,distance_matrix):

    n = len(distance_matrix)
    k = math.ceil(math.log2(n))

    # Step 1: generate all routes
    all_routes = list(itertools.permutations(range(n)))

    # Step 2: compute costs
    costs = []
    for route in all_routes:
        cost = compute_cost(list(route), distance_matrix)
        costs.append(cost)

    # Normalize costs (important)
    max_cost = max(costs)
    min_cost = min(costs)

    # Step 3: apply phase shifts
    for idx, route in enumerate(all_routes):

        cost = costs[idx]

        # normalize between 0 and π
        if max_cost != min_cost:
            phase = (cost - min_cost) / (max_cost - min_cost) * np.pi
        else:
            phase = 0

        # encode route into HOBO binary
        target_state = ""
        for city in route:
            target_state += format(city, f'0{k}b')

        target_state = target_state.ljust(total_qubits, '0')

        # Apply phase only to matching state
        for i in range(total_qubits):
            if target_state[i] == '0':
                qc.x(i)

        # Phase rotation (THIS IS NEW)
        qc.rz(phase, total_qubits - 1)

        for i in range(total_qubits):
            if target_state[i] == '0':
                qc.x(i)

    return qc