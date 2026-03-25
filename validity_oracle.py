from tsp_data import distance_matrix
import itertools

def is_valid_route(route, n):
    return sorted(route) == list(range(n))


def apply_validity_oracle(qc, num_qubits):
    """
    Marks valid routes by phase flipping.
    Uses classical validation logic for simplicity.
    """

    # Generate all possible routes
    n = num_qubits
    all_routes = list(itertools.permutations(range(n)))

    # Find valid routes (all permutations are valid in TSP basic form)
    valid_routes = []

    for route in all_routes:
        if is_valid_route(route, n):
            valid_routes.append(route)

    # For simplicity, mark ONE valid route
    # (full marking requires complex circuit)
    target_route = valid_routes[0]

    # Convert route to binary string
    target_state = ''.join([str(x % 2) for x in target_route])

    # Apply phase flip for that state
    for i in range(num_qubits):
        if target_state[i] == '0':
            qc.x(i)

    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)

    for i in range(num_qubits):
        if target_state[i] == '0':
            qc.x(i)

    return qc