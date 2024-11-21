"""
Applies a quantum gate to a qubit.
"""

from argparse import ArgumentParser, Namespace
import io
import os
import numpy as np
from gates import get_gate_matrix
from qubit import (
    apply_quantum_gate,
    convert_qubit_to_float,
    create_qubit,
    is_valid_qubit_state
)

ROUND_DIGITS: int = 4

parser: ArgumentParser = ArgumentParser(description='Applies a quantum gate to a qubit.')
parser.add_argument('-0', '--qubit-state-0',
                    type=float,
                    dest='qubit_state_0',
                    default=1.0,
                    help='The qubit 0 component.')
parser.add_argument('-1', '--qubit-state-1',
                    type=float,
                    dest='qubit_state_1',
                    default=0.0,
                    help='The qubit 1 component.')
parser.add_argument('-g', '--gate',
                    type=str,
                    dest='gate',
                    choices=['H', 'I', 'X', 'Z'],
                    default='I',
                    help='The quantum gate to apply.')
parser.add_argument('-o', '--output',
                    type=str,
                    dest='output',
                    choices=['github', 'stdout'],
                    default='stdout',
                    help='The output target.')
arguments: Namespace = parser.parse_args()

qubit_state_0: float = arguments.qubit_state_0
qubit_state_1: float = arguments.qubit_state_1
gate: str = arguments.gate
output: str = arguments.output

if not is_valid_qubit_state(qubit_state_0, qubit_state_1, round_digits=ROUND_DIGITS):
    raise ValueError('Invalid qubit state.')

qubit: np.ndarray = create_qubit(qubit_state_0, qubit_state_1)

gate_matrix: np.ndarray = get_gate_matrix(gate)
if gate_matrix is None:
    raise ValueError('Invalid quantum gate.')

result: np.ndarray = apply_quantum_gate(gate_matrix, qubit, round_digits=ROUND_DIGITS)
result_sanitised: list[float] = convert_qubit_to_float(result)

result_output = io.StringIO()
result_output.write(f'final-qubit-state-0={result_sanitised[0]}\n')
result_output.write(f'final-qubit-state-1={result_sanitised[1]}')

if output == 'github':
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as github_output:
        github_output.write(result_output.getvalue())
else:
    print(result_output.getvalue())
