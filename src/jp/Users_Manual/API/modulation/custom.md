# Custom
[Source](https://github.com/shinolab/autd3-rs/blob/v37.0.1/autd3/src/datagram/modulation/custom.rs)

`Custom`は指定された符号なし8bitデータ列を出力する`Modulation`である.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/modulation/custom.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/custom.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/custom.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/custom.py}}
```
{{ #endtab }}
{{ #endtabs }}

上記の例だと, `0xFF`と`0x00`が$\SI{4}{kHz}$でサンプルされる, すなわち, 2kHzのDuty比$\SI{50}{\%}$の矩形波変調がかかる.
