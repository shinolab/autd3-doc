# RadiationPressure
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/modulation/radiation_pressure.rs)

`RadiationPressure`は`Modulation`を音圧ではなく, 放射圧 (音圧の二乗に比例) に印加するための`Modulation`である.

例えば, $\SI{1}{kHz}$の`Sine`変調に`RadiationPressure`を適用した場合の音圧振幅の放射圧は以下のようになり, 放射圧の包絡線が$\SI{1}{kHz}$のsin波に従う.

<figure>
  <img src="../../../fig/Users_Manual/sine_1k_mod_rad.png"/>
</figure>

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/radiation_0.py}}
```
</div>
