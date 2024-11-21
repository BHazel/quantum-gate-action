"""
Applies a quantum gate to a qubit.
"""

import os
import numpy as np
from gates import get_gate_matrix
from qubit import (
    apply_quantum_gate,
    convert_qubit_to_float,
    create_qubit,
    is_valid_qubit_state
)

qubit_state_0: str = os.environ['QUBIT_STATE_0']
qubit_state_1: str = os.environ['QUBIT_STATE_1']
gate: str = os.environ['GATE']

def main():
    """
    Program entry point.
    """
    qubit_0: float = float(qubit_state_0)
    qubit_1: float = float(qubit_state_1)
    if not is_valid_qubit_state(qubit_0, qubit_1):
        raise ValueError('Invalid qubit state.')

    qubit: np.ndarray = create_qubit(qubit_0, qubit_1)

    gate_matrix: np.ndarray = get_gate_matrix(gate)
    if gate_matrix is None:
        raise ValueError('Invalid quantum gate.')

    result: np.ndarray = apply_quantum_gate(gate_matrix, qubit, round_digits=4)
    result_sanitised: list[float] = convert_qubit_to_float(result)

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as github_output:
        github_output.write(f'final-qubit-state-0={result_sanitised[0]}\n')
        github_output.write(f'final-qubit-state-1={result_sanitised[1]}\n')

if __name__ == '__main__':
    main()
