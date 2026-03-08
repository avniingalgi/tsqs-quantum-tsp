from tsp_data import distance_matrix, n_cities
from quantum_circuit import create_superposition
from run_simulation import run_circuit
from decode import decode_tour
from cost_function import compute_cost
from validity_oracle import validity_oracle
from grover_diffusion import diffusion_operator

# Create circuit
qc = create_superposition(n_cities)

# Step-1 oracle
oracle = validity_oracle(qc.num_qubits)
qc.compose(oracle, inplace=True)

# Diffusion
diff = diffusion_operator(qc.num_qubits)
qc.compose(diff, inplace=True)
print(qc.draw()) 
# Measurement
qc.measure(range(qc.num_qubits), range(qc.num_qubits))

# Run circuit
counts = run_circuit(qc)

print("Measured states:")
print(counts)

best_cost = 999
best_tour = None

for bitstring in counts:

    tour = decode_tour(bitstring, n_cities)

    # remove invalid cities
    if any(city >= n_cities for city in tour):
        continue

    # remove duplicates
    if len(set(tour)) != n_cities:
        continue

    cost = compute_cost(tour, distance_matrix)

    if cost < best_cost:
        best_cost = cost
        best_tour = tour

print("\nBest tour:", best_tour + [best_tour[0]])
print("Cost:", best_cost)