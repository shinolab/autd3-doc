# Holo

`Holo` is a `Gain` for generating multiple focal points.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5 for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-gain-holo
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::gain::holo)
```

<div class="tab_content" id="cs_code_content">
  <p>
    Included in the main library.
  </p>
</div>

<div class="tab_content" id="unity_code_content">
  <p>
    Included in the main library.
  </p>
</div>

<div class="tab_content" id="python_code_content">
  <p>
    Included in the main library.
  </p>
</div>
</div>

## APIs

Several algorithms for generating multiple focal points have been proposed, and the SDK implements the following algorithms:

* [`Naive`](./holo/naive.md) - Superimposition of single focal point solutions
* [`GS`](./holo/gs.md) - Gershberg-Saxon
* [`GSPAT`](./holo/gspat.md) - Gershberg-Saxon for Phased Arrays of Transducers
* [`LM`](./holo/lm.md) - Levenberg-Marquardt
* [`Greedy`](./holo/greedy.md) - Greedy algorithm and Brute-force search

In addition, each method allows you to choose a computation backend. (except for `Greedy`.)
The SDK provides the following `Backends`:

* `NalgebraBackend` - Uses [Nalgebra](https://nalgebra.org/)
* `CUDABackend` - Uses CUDA, runs on GPU (Rust version only)
* `ArrayFireBackend` - Uses [ArrayFire](https://arrayfire.com/) (Rust version only)

> NOTE: `CUDABackend` and `ArrayFireBackend` are intended for speedup, but in most cases, `NalgebraBackend` is sufficient. Be sure to benchmark when using them.


## Emission Constraints

The intensity of the calculation results of each algorithm must ultimately be limited to the range that the transducers can output.
This can be controlled with the optional `EmissionConstraint`, and one of the following four must be specified:

- Normalize: Normalize all transducer intensities by dividing by the maximum intensity.
- Uniform: Set the intensity of all transducers to the specified value.
- Clamp: Clamp the intensity to the specified range.
- Multiply: Multiply by a specified value after normalization.
