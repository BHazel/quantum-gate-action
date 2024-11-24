# Quantum Gate Action

This GitHub Action simulates applying a quantum logic gate on a qubit.  It returns the resulting state vector and optionally the measurement of the qubit for a specified number of shots.

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

### `shots`

The number of times to apply the quantum gate and measure the qubit in its final state.

If 0 no measurement will be performed.

**Default:** `0`

## Outputs

### `final-qubit-state-0`

The final value of the qubit 0 component.

### `final-qubit-state-1`

The final value of the qubit 1 component.

### `measurement-0-count`

The number of times the qubit measurement was 0 (if measurement is requested).

### `measurement-1-count`

The number of times the qubit measurement was 1 (if measurement is requested).

## Example Usage

```yml
uses: bhazel/quantum-gate-action@master
with:
    qubit-state-0: 0.0
    qubit-state-1: 1.0
    gate: H
    shots: 100
```