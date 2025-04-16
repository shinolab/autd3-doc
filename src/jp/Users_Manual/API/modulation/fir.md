# Fir
[Source](https://github.com/shinolab/autd3-rs/blob/v32.1.0/autd3/src/datagram/modulation/fir.rs)

`Fir`では任意の`Modulation`FIRフィルタを適用することができる.

以下は, サンプリング周波数$\SI{20}{kHz}$, タップ数$199$, カットオフ周波数$\SI{200}{Hz}$のLPFを適用する例である. 

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
