# GS
[Source](https://github.com/shinolab/autd3-rs/blob/v37.0.1/autd3-gain-holo/src/linear_synthesis/gs.rs)

Gershberg-Saxon, Marzoらの論文[^marzo2019]に基づく多焦点`Gain`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.py}}
```
{{ #endtab }}
{{ #endtabs }}

`repeat`は反復回数, デフォルトは上記の通り.
パラメータの詳細は論文[^marzo2019]を参照されたい.

[^marzo2019]: Marzo, Asier, and Bruce W. Drinkwater. "Holographic acoustic tweezers." Proceedings of the National Academy of Sciences 116.1 (2019): 84-89.
