# Importing necessary libraries
import numpy as np

# Function to simulate the BB84 protocol
def bb84_protocol():
    # Step 1: Alice generates a random sequence of bits
    alice_bits = np.random.randint(2, size=10)
    
    # Step 2: Alice randomly chooses bases (0: standard, 1: Hadamard)
    alice_bases = np.random.randint(2, size=10)
    
    # Step 3: Bob randomly chooses bases (0: standard, 1: Hadamard)
    bob_bases = np.random.randint(2, size=10)
    
    # Step 4: Bob measures the qubits sent by Alice
    bob_results = []
    for bit, alice_base, bob_base in zip(alice_bits, alice_bases, bob_bases):
        if alice_base == bob_base:
            bob_results.append(bit)
        else:
            bob_results.append(np.random.randint(2))
    
    # Step 5: Alice and Bob compare bases publicly and discard mismatches
    key = [alice_bit for alice_bit, alice_base, bob_base in zip(alice_bits, alice_bases, bob_bases) if alice_base == bob_base]
    
    return key

# Running the BB84 protocol simulation
key = bb84_protocol()
print("Generated Key:", key)
