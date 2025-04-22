# GSPAT
[Source](https://github.com/shinolab/autd3-rs/blob/v32.1.1/autd3-gain-holo/src/linear_synthesis/gspat.rs)

Gershberg-Saxon for Phased Arrays of Transducers, Plasenciaらの論文[^plasencia2020]に基づく多焦点`Gain`.

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

`repeat`は反復回数, デフォルトは上記の通り.
パタメータの詳細は論文[^plasencia2020]を参照されたい.

[^plasencia2020]: Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers." ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.
