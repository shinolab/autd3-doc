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

Several algorithms have been proposed for generating foci (multiple focal points), and the SDK implements the following algorithms:

* `Naive` - Superposition of single focal point solutions
* `GS` - Gershberg-Saxon, based on the paper by Marzo et al. [^marzo2019]
* `GSPAT` - Gershberg-Saxon for Phased Arrays of Transducers, based on the paper by Plasencia et al. [^plasencia2020]
* `LM` - Levenberg-Marquardt, an optimization method for nonlinear least squares problems proposed by Levenberg [^levenberg1944] and Marquardt [^marquardt1963], implemented based on Madsen's text [^madsen2004].
* `Greedy` - Greedy algorithm and Brute-force search, based on the paper by Suzuki et al. [^suzuki2021]

Each method can choose a computation backend (except for `Greedy`).
The SDK provides the following `Backends`:

* `NalgebraBackend` - Uses [Nalgebra](https://nalgebra.org/)
* `CUDABackend` - Uses CUDA, runs on GPU (Rust version only)
* `ArrayFireBackend` - Uses [ArrayFire](https://arrayfire.com/) (Rust version only)

> NOTE: `CUDABackend` and `ArrayFireBackend` are intended for speedup, but in most cases, `NalgebraBackend` is sufficient. Be sure to benchmark when using them.

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/gain/holo_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/holo_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/holo_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/holo_0.py}}
```
</div>

## Emission Constraints and Optimization Parameters

The intensity of the calculation results of each algorithm must ultimately be limited to the range that the transducers can output.
This can be controlled with the optional `EmissionConstraint`, and one of the following four must be specified:

- Normalize: Normalize all transducer intensities by dividing by the maximum intensity.
- Uniform: Set the intensity of all transducers to the specified value.
- Clamp: Clamp the intensity to the specified range.
- Multiply: Multiply by a specified value after normalization.

Additionally, each algorithm has optimization parameters.

Refer to the respective papers for details on each parameter.

[^marzo2019]: Marzo, Asier, and Bruce W. Drinkwater. "Holographic acoustic tweezers." Proceedings of the National Academy of Sciences 116.1 (2019): 84-89.

[^plasencia2020]: Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers." ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.

[^levenberg1944]: Levenberg, Kenneth. "A method for the solution of certain non-linear problems in least squares." Quarterly of applied mathematics 2.2 (1944): 164-168.

[^marquardt1963]: Marquardt, Donald W. "An algorithm for least-squares estimation of nonlinear parameters." Journal of the society for Industrial and Applied Mathematics 11.2 (1963): 431-441.

[^madsen2004]: Madsen, Kaj, Hans Bruun Nielsen, and Ole Tingleff. "Methods for non-linear least squares problems." (2004).

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
