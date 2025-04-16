# Greedy
[Source](https://github.com/shinolab/autd3-rs/blob/v32.1.0/autd3-gain-holo/src/combinatorial/greedy.rs)

Greedy Algorithm with Brute-Force Search, 鈴木らの論文[^suzuki2021]に基づく多焦点`Gain`.


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

`phase_div`は位相の離散化深度, デフォルトは上記の通り.
パラメータの詳細は論文[^suzuki2021]を参照されたい.

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
