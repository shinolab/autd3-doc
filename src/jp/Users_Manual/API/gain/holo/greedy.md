# Greedy
[Source](https://github.com/shinolab/autd3-rs/blob/v38.0.1/autd3-gain-holo/src/combinatorial/greedy.rs)

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

`phase_quantization_levels`は位相の離散化深度, デフォルトは上記の通り.
パラメータの詳細は論文[^suzuki2021]を参照されたい.

Rust版のみ, 目的関数を変更できる.
デフォルトは目標音圧との絶対誤差を使用する.

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
