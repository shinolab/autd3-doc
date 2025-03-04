# GS

Gershberg-Saxon, `Gain` for multiple focal points based on the paper by Marzo et al.[^marzo2019].

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

`repeat` is the number of iterations, the default is as above.
For details on the parameters, refer to the paper[^marzo2019].

[^marzo2019]: Marzo, Asier, and Bruce W. Drinkwater. "Holographic acoustic tweezers." Proceedings of the National Academy of Sciences 116.1 (2019): 84-89.
