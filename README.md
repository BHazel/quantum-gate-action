# Quantum Gate Action

This action simulates applying a quantum logic gate on a qubit and returns the resulting state vector.

## Inputs

### `qubit-state-0`

**Required**

The initial value of the qubit 0 component.

Valid value can be between 0 and 1.

**Default:** `1.0`

### `qubit-state-1`

**Required**

The initial value of the qubit 1 component.

Valid value can be between 0 and 1.

**Default:** `0.0`

### `gate`

**Required**

The quantum gate to apply to the qubit.

Possible Values: H, I, X, Z

**Default:** `I`

## Outputs

### `final-qubit-state-0`

The final value of the qubit 0 component.

### `final-qubit-state-1`

The final value of the qubit 1 component.

## Example Usage

```yml
uses: bhazel/quantum-gate-action@master
with:
    qubit-state-0: 0.0
    qubit-state-1: 1.0
    gate: H
```