import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# Step 1: Define Quantum Gates and State
def create_quantum_state(theta, phi):
    """Create a quantum state |ψ⟩ = cos(θ/2)|0⟩ + exp(i*φ)*sin(θ/2)|1⟩"""
    alpha = np.cos(theta / 2)
    beta = np.exp(1j * phi) * np.sin(theta / 2)
    return np.array([alpha, beta])

def apply_gate(state, gate):
    """Apply a quantum gate to a quantum state"""
    return np.dot(gate, state)

def pauli_x_gate():
    """Pauli-X gate (NOT gate)"""
    return np.array([[0, 1], [1, 0]])

def pauli_z_gate():
    """Pauli-Z gate"""
    return np.array([[1, 0], [0, -1]])

def hadamard_gate():
    """Hadamard gate"""
    return np.array([[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]])

# Step 2: Simulate Quantum System
def simulate_quantum_system(theta, phi, gate_sequence):
    """Simulate quantum system with given gate sequence"""
    state = create_quantum_state(theta, phi)
    for gate in gate_sequence:
        state = apply_gate(state, gate)
    return state

# Parameters
theta = np.pi / 3  # Example value for theta
phi = np.pi / 4    # Example value for phi
gate_sequence = [hadamard_gate(), pauli_x_gate(), pauli_z_gate()]

# Simulate quantum system
final_state = simulate_quantum_system(theta, phi, gate_sequence)

# Step 3: Analyze Results
def plot_quantum_state(state):
    """Plot the real and imaginary parts of the quantum state"""
    real_part = np.real(state)
    imag_part = np.imag(state)
    plt.figure(figsize=(8, 8))
    plt.bar(['|0⟩', '|1⟩'], real_part, color='b', label='Real Part')
    plt.bar(['|0⟩', '|1⟩'], imag_part, color='r', bottom=real_part, label='Imaginary Part')
    plt.title('Quantum State after Applying Gates')
    plt.xlabel('Basis States')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

plot_quantum_state(final_state)
