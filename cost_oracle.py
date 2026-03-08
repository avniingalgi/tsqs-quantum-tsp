from qiskit import QuantumCircuit
from decode import decode_tour
from cost_function import compute_cost

def cost_oracle(n_qubits, counts, n_cities, distance_matrix):

    qc = QuantumCircuit(n_qubits)

    best_cost = 999

    for bitstring in counts:

        tour = decode_tour(bitstring, n_cities)

        # remove invalid tours
        if any(city >= n_cities for city in tour):
            continue

        if len(set(tour)) != n_cities:
            continue

        cost = compute_cost(tour, distance_matrix)

        if cost < best_cost:
            best_cost = cost

    # simplified phase marking
    qc.z(1)

    return qc