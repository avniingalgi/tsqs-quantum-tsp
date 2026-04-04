from tsp_data import num_cities, distance_matrix
from quantum_circuit import create_circuit
from validity_oracle import apply_validity_oracle
from cost_oracle import apply_cost_oracle
from grover_diffusion import apply_diffusion
from run_simulation import run_circuit
from decode import decode_result


# ======================================
# MAIN TSQS FUNCTION (USED BY GUI)
# ======================================
def run_tsqs(custom_matrix):

    import tsp_data

    # Override distance matrix dynamically
    tsp_data.distance_matrix = custom_matrix
    tsp_data.num_cities = len(custom_matrix)

    n = tsp_data.num_cities

    print("Starting TSQS for TSP...\n")

    # Create circuit using HOBO encoding
    qc, total_qubits, k = create_circuit(n)

    # ========================
    # STEP 1 → G₁ (Feasible)
    # ========================
    print("\n--- Step 1: Feasible Solution Search (G1) ---")

    for _ in range(4):
        qc = apply_validity_oracle(qc, total_qubits,custom_matrix)
        qc = apply_diffusion(qc, total_qubits)

    # ========================
    # STEP 2 → G₂ (Optimal)
    # ========================
    print("\n--- Step 2: Optimal Solution Search (G2) ---")

    for _ in range(4):
        qc = apply_cost_oracle(qc, total_qubits,custom_matrix)
        qc = apply_diffusion(qc, total_qubits)

    # ========================
    # Measurement
    # ========================
    qc.measure_all()

    counts = run_circuit(qc)

    print("\nMeasurement Results:")
    print(counts)

    route, cost = decode_result(counts,custom_matrix)

    return route, cost


# ======================================
# OPTIONAL: RUN FROM TERMINAL
# ======================================
def main():

    print("Running TSQS with default matrix...\n")

    route, cost = run_tsqs(distance_matrix)

    print("\nFinal Output:")
    print("Optimal Route:", route)
    print("Minimum Cost:", cost)


if __name__ == "__main__":
    main()