from qiskit import QuantumCircuit

def diffusion_operator(n_qubits):

    qc = QuantumCircuit(n_qubits)

    for i in range(n_qubits):
        qc.h(i)

    for i in range(n_qubits):
        qc.x(i)

    qc.h(n_qubits-1)

    qc.mcx(list(range(n_qubits-1)), n_qubits-1)

    qc.h(n_qubits-1)

    for i in range(n_qubits):
        qc.x(i)

    for i in range(n_qubits):
        qc.h(i)

    return qc