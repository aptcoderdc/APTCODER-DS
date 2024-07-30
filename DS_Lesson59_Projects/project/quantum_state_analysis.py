import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define Quantum States
def create_quantum_state(theta, phi):
    """Create a quantum state |ψ⟩ = cos(θ/2)|0⟩ + exp(i*φ)*sin(θ/2)|1⟩"""
    alpha = np.cos(theta / 2)
    beta = np.exp(1j * phi) * np.sin(theta / 2)
    return np.array([alpha, beta])

# Generate data for superposition states
theta_values = np.linspace(0, np.pi, 50)
phi_values = np.linspace(0, 2 * np.pi, 50)
states = np.array([create_quantum_state(theta, phi) for theta in theta_values for phi in phi_values])

# Step 2: Analyze Superposition
def plot_quantum_states(states):
    """Plot the real and imaginary parts of quantum states"""
    real_parts = np.real(states)
    imag_parts = np.imag(states)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(real_parts[:, 0], real_parts[:, 1], c='blue', label='Real Part')
    plt.title('Real Part of Quantum States')
    plt.xlabel('α')
    plt.ylabel('β')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(imag_parts[:, 0], imag_parts[:, 1], c='red', label='Imaginary Part')
    plt.title('Imaginary Part of Quantum States')
    plt.xlabel('α')
    plt.ylabel('β')
    plt.legend()

    plt.tight_layout()
    plt.show()

plot_quantum_states(states)
