# Holo

`Holo` is a `Gain` for generating multiple focal points.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-gain-holo
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::gain::holo)
```
{{ #endtab }}
{{ #tab name=C# }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Unity }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Python }}
Included in the main library.
{{ #endtab }}
{{ #endtabs }}

## APIs

Several algorithms for generating multiple focal points have been proposed, and the SDK implements the following algorithms:

* [`Naive`](./holo/naive.md) - Superimposition of single focal point solutions
* [`GS`](./holo/gs.md) - Gershberg-Saxon
* [`GSPAT`](./holo/gspat.md) - Gershberg-Saxon for Phased Arrays of Transducers
* [`Greedy`](./holo/greedy.md) - Greedy algorithm and Brute-force search

## Emission Constraints

The intensity of the calculation results of each algorithm must ultimately be limited to the range that the transducers can output.
This can be controlled with the optional `EmissionConstraint`, and one of the following four must be specified:

- Normalize: Normalize all transducer intensities by dividing by the maximum intensity.
- Uniform: Set the intensity of all transducers to the specified value.
- Clamp: Clamp the intensity to the specified range.
- Multiply: Multiply by a specified value after normalization.
