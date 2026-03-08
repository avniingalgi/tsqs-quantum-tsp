from qiskit import QuantumCircuit

def validity_oracle(n_qubits):

    qc = QuantumCircuit(n_qubits)

    # simplified phase flip
    qc.z(0)
    qc.z(2)
    qc.z(4)

    return qc