import itertools
import math
from tsp_data import distance_matrix

def apply_validity_oracle(qc, total_qubits,distance_matrix):

    n = len(distance_matrix)
    k = math.ceil(math.log2(n))

    # pick one valid permutation
    valid_route = list(itertools.permutations(range(n)))[0]

    target_state = ""

    for city in valid_route:
        target_state += format(city, f'0{k}b')

    target_state = target_state.ljust(total_qubits, '0')

    # mark valid state
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