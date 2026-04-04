def run_tsqs(custom_matrix):

    n = len(custom_matrix)

    qc, total_qubits, k = create_circuit(n)

    # G1
    for _ in range(4):
        qc = apply_validity_oracle(qc, total_qubits, custom_matrix)
        qc = apply_diffusion(qc, total_qubits)

    # G2
    for _ in range(4):
        qc = apply_cost_oracle(qc, total_qubits, custom_matrix)
        qc = apply_diffusion(qc, total_qubits)

    qc.measure_all()

    counts = run_circuit(qc)

    route, cost = decode_result(counts, custom_matrix)

    return route, cost