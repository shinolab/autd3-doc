# Custom

`Custom` is a `Gain` that allows the user to freely generate sound fields.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/gain/custom_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/gain/custom_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/gain/custom_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/gain/custom_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

The argument of the `Custom` constructor is `Fn(&Device) -> Fn(&Transducer) -> Drive`.
