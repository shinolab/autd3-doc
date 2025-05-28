# Greedy

Greedy Algorithm with Brute-Force Search, `Gain` for multiple focal points based on the paper by Suzuki et al.[^suzuki2021].

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.py}}
```
{{ #endtab }}
{{ #endtabs }}

`phase_quantization_levels` is the discretization depth of the phase, the default is as above.
For details on the parameters, refer to the paper[^suzuki2021].

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
