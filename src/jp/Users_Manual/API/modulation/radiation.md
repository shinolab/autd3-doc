# RadiationPressure
[Source](https://github.com/shinolab/autd3-rs/blob/v37.0.1/autd3/src/datagram/modulation/radiation_pressure.rs)

`RadiationPressure`は`Modulation`を音圧ではなく, 放射圧 (音圧の二乗に比例) に印加するための`Modulation`である.

例えば, $\SI{1}{kHz}$の`Sine`変調に`RadiationPressure`を適用した場合の音圧振幅の放射圧は以下のようになり, 放射圧の包絡線が$\SI{1}{kHz}$のsin波に従う.

<figure>
  <img src="../../../fig/Users_Manual/sine_1k_mod_rad.png"/>
</figure>

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.py}}
```
{{ #endtab }}
{{ #endtabs }}
