# GSPAT

Gershberg-Saxon for Phased Arrays of Transducers, `Gain` for multiple focal points based on the paper by Plasencia et al.[^plasencia2020].

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.py}}
```
{{ #endtab }}
{{ #endtabs }}

`repeat` is the number of iterations, the default is as above.
For details on the parameters, refer to the paper[^plasencia2020].

[^plasencia2020]: Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers." ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.
