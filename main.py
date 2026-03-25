from tsp_data import num_cities
from quantum_circuit import create_circuit
from validity_oracle import apply_validity_oracle
from cost_oracle import apply_cost_oracle
from grover_diffusion import apply_diffusion
from run_simulation import run_circuit
from decode import decode_result

def main():

    print("Starting TSQS for TSP...\n")

    num_qubits = num_cities

    # Step 1: Create circuit
    qc, total_qubits, k = create_circuit(num_cities)

    # Step 2: Validity oracle
    qc = apply_validity_oracle(qc, total_qubits)

    # Step 3: Diffusion
    qc = apply_diffusion(qc, total_qubits)

    # Step 4: Cost oracle
    qc = apply_cost_oracle(qc, total_qubits)

    # Step 5: Diffusion again
    qc = apply_diffusion(qc, total_qubits)

    # Step 6: Measurement
    qc.measure_all()

    # ✅ THIS LINE WAS MISSING
    counts = run_circuit(qc)

    print("\nMeasurement Results:")
    print(counts)

    # Step 7: Decode
    route, cost = decode_result(counts)

    print("\nFinal Output:")
    print("Optimal Route:", route)
    print("Minimum Cost:", cost)


if __name__ == "__main__":
    main()