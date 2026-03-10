# Two-Step Quantum Search (TSQS) Algorithm for Solving the Traveling Salesman Problem

## Overview

This project implements a simplified version of the **Two-Step Quantum Search (TSQS) algorithm** to solve the **Traveling Salesman Problem (TSP)** using quantum computing principles.

The Traveling Salesman Problem is a well-known **NP-hard combinatorial optimization problem** where a salesman must visit each city exactly once and return to the starting city while minimizing the total travel cost.

The implementation is built using **Python** and the **Qiskit quantum computing framework** and demonstrates how quantum circuits can be used to explore possible tours using **superposition and Grover-style amplification**.

---

## Problem Statement

Given a set of cities and distances between them, the objective is to find the **minimum-cost tour** that:

* Visits each city exactly once
* Returns to the starting city
* Minimizes the total travel distance

Example distance matrix:

```
[ [0,2,4],
  [3,0,5],
  [6,1,0] ]
```

---

## Key Concepts Used

The project demonstrates several fundamental quantum computing concepts:

* **Quantum superposition** using Hadamard gates
* **Grover-style oracle marking**
* **Diffusion operator for amplitude amplification**
* **Binary encoding of TSP routes**
* **Measurement and decoding of quantum states**
* **Classical post-processing for route validation**

---

## Algorithm Pipeline

The implemented pipeline follows the structure of the TSQS approach:

```
Input Distance Matrix
        ↓
Binary Encoding of Cities
        ↓
Quantum Superposition (Hadamard Gates)
        ↓
Validity Oracle (Step-1 of TSQS)
        ↓
Grover Diffusion Operator
        ↓
Measurement
        ↓
Decode Bitstrings into Tours
        ↓
Compute Tour Costs
        ↓
Select Minimum Cost Route
```

---

## Project Structure

```
tsqs-quantum-tsp
│
├── main.py                # Main program execution
├── tsp_data.py            # Distance matrix and city data
├── quantum_circuit.py     # Quantum circuit initialization
├── validity_oracle.py     # Oracle marking candidate states
├── grover_diffusion.py    # Grover diffusion operator
├── decode.py              # Convert measured bitstrings to tours
├── cost_function.py       # Compute tour cost
├── run_simulation.py      # Executes circuit on simulator
├── README.md              # Project documentation
└── .gitignore             # Files ignored by Git
```

---

## Quantum Encoding

Cities are encoded using a **binary representation similar to HOBO encoding**.

For `n` cities:

```
K = ceil(log₂(n)) qubits per city
```

Example for **3 cities**:

```
City1 → q0 q1
City2 → q2 q3
City3 → q4 q5
```

Total qubits used:

```
n × K = 3 × 2 = 6 qubits
```

---

## Example Output

Example program output:

```
Measured states:
{'001001': 18, '010010': 17, '111000': 19 ...}

Best tour: [1, 0, 2, 1]
Cost: 8
```

This indicates the algorithm identified the lowest-cost route.

---

## Installation

Install required dependencies:

```
pip install qiskit
pip install numpy
```

Optional packages:

```
pip install matplotlib
pip install networkx
```

---

## Running the Project

Run the main program:

```
python main.py
```

The simulator will execute the quantum circuit and display the best route found.

---

## Current Limitations

This implementation is designed for **educational purposes and small problem sizes**.

Limitations include:

* Simplified oracle implementation
* Classical validation of tours after measurement
* Tested only for small city counts (e.g., 3 cities)

---

## Future Improvements

Possible enhancements include:

* Full quantum implementation of feasibility constraints
* Step-2 cost oracle from the TSQS algorithm
* Multiple Grover iterations
* Visualization of routes using graphs
* Larger TSP instances

---

## Technologies Used

* Python
* Qiskit
* NumPy
* Quantum Circuit Simulation

---

## References

The project is based on the research paper:

**Two-Step Quantum Search Algorithm for Solving Traveling Salesman Problems**
IEEE Transactions on Quantum Engineering.

Additional references include works on Grover's algorithm and quantum optimization.

---

## Author

Avni Ingalgi
Computer Engineering Student

---

## License

This project is created for **educational and research purposes**.
