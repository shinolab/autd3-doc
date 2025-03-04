# Phase Correction

`PhaseCorrection` allows you to correct the phase.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/phase_corr.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/phase_corr.py}}
```
{{ #endtab }}
{{ #endtabs }}

The constructor argument for `PhaseCorrection` is `Fn(&Device) -> Fn(&Transducer) -> Phase`, which specifies the phase value for each transducer to be added to the values of `Gain`, `FociSTM`, and `GainSTM`.
