from qiskit import QuantumCircuit, transpile #used to create a quantum circuit, function to optimize QC's for a specfic device
from qiskit.visualization import plot_histogram #just plots a hist for measured outcomes
from qiskit_aer import AerSimulator #a quantum circuit simulator 


circuit = QuantumCircuit(2,2) #creates a QC with two qubits and 2 classical bits, in that order

circuit.x(1) #applies the NOT gate to quibit 1
circuit.barrier() #makes gates before and after the barrier their own seperate units 

