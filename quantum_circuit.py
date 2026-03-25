from qiskit import QuantumCircuit
import math

def create_circuit(n_cities):

    k = math.ceil(math.log2(n_cities))   # qubits per city
    total_qubits = n_cities * k

    qc = QuantumCircuit(total_qubits, total_qubits)

    # Create superposition
    for i in range(total_qubits):
        qc.h(i)

    return qc, total_qubits, k