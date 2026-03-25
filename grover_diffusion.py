def apply_diffusion(qc, num_qubits):

    for i in range(num_qubits):
        qc.h(i)
        qc.x(i)

    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)

    for i in range(num_qubits):
        qc.x(i)
        qc.h(i)

    return qc