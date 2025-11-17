# Custom
[Source](https://github.com/shinolab/autd3-rs/blob/v38.0.0/autd3/src/datagram/gain/custom.rs)

`Custom`はユーザーが自由に音場を生成するための`Gain`である.

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

`Custom`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Drive`である.
