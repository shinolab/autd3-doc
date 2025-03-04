# Fir

You can apply an FIR filter using `Fir`.

Below is an example of applying an LPF with a sampling frequency of $\SI{20}{kHz}$, 199 taps, and a cutoff frequency of $\SI{200}{Hz}$.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/modulation/fir.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/fir.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/fir.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/fir.py}}
```
{{ #endtab }}
{{ #endtabs }}
