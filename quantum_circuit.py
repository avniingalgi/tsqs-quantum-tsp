from qiskit import QuantumCircuit
import math

def create_superposition(n):

    k = math.ceil(math.log2(n))
    n_qubits = n * k

    qc = QuantumCircuit(n_qubits, n_qubits)

    for i in range(n_qubits):
        qc.h(i)

    qc.barrier()

    return qc