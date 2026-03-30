from tsp_data import num_cities
from quantum_circuit import create_circuit
from validity_oracle import apply_validity_oracle
from cost_oracle import apply_cost_oracle
from grover_diffusion import apply_diffusion
from run_simulation import run_circuit
from decode import decode_result

def main():

    print("Starting TSQS for TSP...\n")

    qc, total_qubits, k = create_circuit(num_cities)

    # ========================
    # STEP 1 → G₁ (Feasible)
    # ========================
    print("\n--- Step 1: Feasible Solution Search (G1) ---")

    for _ in range(4):   # number of Grover iterations
        qc = apply_validity_oracle(qc, total_qubits)
        qc = apply_diffusion(qc, total_qubits)

    # ========================
    # STEP 2 → G₂ (Optimal)
    # ========================
    print("\n--- Step 2: Optimal Solution Search (G2) ---")

    for _ in range(2):
        qc = apply_cost_oracle(qc, total_qubits)
        qc = apply_diffusion(qc, total_qubits)

    # ========================
    # Measurement
    # ========================
    qc.measure_all()

    counts = run_circuit(qc)

    print("\nMeasurement Results:")
    print(counts)

    route, cost = decode_result(counts)

    print("\nFinal Output:")
    print("Optimal Route:", route)
    print("Minimum Cost:", cost)


if __name__ == "__main__":
    main()