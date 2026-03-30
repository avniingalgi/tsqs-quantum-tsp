from qiskit_aer import AerSimulator
from qiskit import transpile

def run_circuit(qc):

    simulator = AerSimulator()

    compiled = transpile(qc, simulator)

    result = simulator.run(compiled, shots=4096).result()

    counts = result.get_counts()

    return counts