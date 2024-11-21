"""
Functions for working with qubit values.
"""

import numpy as np

def is_valid_qubit_state(qubit_state_0: float, qubit_state_1: float) -> bool:
    """
    Validates the qubit states.

    Args:
        qubit_state_0 (float): The state of the qubit 0 component.
        qubit_state_1 (float): The state of the qubit 1 component.
    
    Returns:
        bool: True if the qubit states are valid, otherwise False.
    """
    return abs(qubit_state_0) ** 2 + abs(qubit_state_1) ** 2 == 1

def create_qubit(qubit_state_0: float, qubit_state_1: float) -> np.ndarray:
    """
    Creates a qubit from the given states.

    Args:
        qubit_state_0 (float): The state of the qubit 0 component.
        qubit_state_1 (float): The state of the qubit 1 component.
    
    Returns:
        np.ndarray: The qubit.
    """
    return np.array([[qubit_state_0], [qubit_state_1]])

def apply_quantum_gate(gate: np.ndarray, qubit: np.ndarray, round_digits: int = 0) -> np.ndarray:
    """
    Applies a quantum gate to a qubit.

    Args:
        gate (np.ndarray): The quantum gate.
        qubit (np.ndarray): The qubit.
    
    Returns:
        np.ndarray: The qubit after the gate is applied.
    """
    result: np.ndarray = gate @ qubit
    if round_digits == 0:
        return result

    return np.round(result, round_digits)

def convert_qubit_to_float(qubit: np.ndarray) -> list[float]:
    """
    Converts the qubit state vector to float values.

    Args:
        qubit (np.ndarray): The qubit.
    
    Returns:
        list: The qubit as a list of floats.
    """
    return [
        float(qubit[0][0]),
        float(qubit[1][0])
    ]
