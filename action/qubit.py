"""
Functions for working with qubit values.
"""

import numpy as np

def is_valid_qubit_state(qubit_state_0: float, qubit_state_1: float, round_digits: int = 0) -> bool:
    """
    Validates the qubit states.

    Args:
        qubit_state_0 (float): The state of the qubit 0 component.
        qubit_state_1 (float): The state of the qubit 1 component.
        round_digits (int): The number of digits to round to (Default = 0).
            If set to 0 then no rounding is performed.
    
    Returns:
        bool: True if the qubit states are valid, otherwise False.
    """
    total_qubit_components: float = abs(qubit_state_0) ** 2 + abs(qubit_state_1) ** 2
    if round_digits > 0:
        return round(total_qubit_components, round_digits) == 1.0

    return total_qubit_components == 1.0

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
        round_digits (int): The number of digits to round to (Default = 0).
            If set to 0 then no rounding is performed.
    
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

def measure_qubit(qubit: np.ndarray) -> int:
    """
    Measures a qubit.

    Args:
        qubit (np.ndarray): The qubit.
    
    Returns:
        int: The value from the measurement.
    """
    zero_probability = float(qubit[0][0]) ** 2
    return 0 if np.random.rand() < zero_probability else 1
