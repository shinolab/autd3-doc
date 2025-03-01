# RadiationPressure

`RadiationPressure` is a `Modulation` that applies modulation to radiation pressure (proportional to the square of sound pressure) instead of sound pressure.

For example, when `RadiationPressure` is applied to a $\SI{1}{kHz}$ `Sine` modulation, the radiation pressure of the sound pressure amplitude will be as follows, and the envelope of the radiation pressure will follow a $\SI{1}{kHz}$ sine wave.

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
