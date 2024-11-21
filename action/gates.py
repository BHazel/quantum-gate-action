"""
Matrix representations of common quantum gates.
"""

import numpy as np

H = np.array([
    [1, 1],
    [1, -1]
]) / np.sqrt(2)

I = np.eye(2)

X = np.array([
    [0, 1],
    [1, 0]
])

Z = np.array([
    [1, 0],
    [0, -1]
])

GATES_MAP = {
    'H': H,
    'I': I,
    'X': X,
    'Z': Z
}

def get_gate_matrix(gate: str) -> np.ndarray:
    """
    Returns the matrix representation of the given quantum gate.

    Args:
        gate (str): The quantum gate code.
    
    Returns:
        np.ndarray: The matrix representation of the quantum gate.
    """
    return GATES_MAP.get(gate)
