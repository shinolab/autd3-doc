# Fir
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/modulation/fir.rs)

`Fir`では任意の`Modulation`FIRフィルタを適用することができる.

以下は, サンプリング周波数$\SI{20}{kHz}$, タップ数$199$, カットオフ周波数$\SI{200}{Hz}$のLPFを適用する例である. 

<div class="tabs">
<input id="rust_tab_fir" type="radio" class="tab" name="tab_fir" checked>
<label class="tab_item" n=4 for="rust_tab_fir">Rust</label>
<input id="cpp_tab_fir" type="radio" class="tab" name="tab_fir">
<label class="tab_item" n=4 for="cpp_tab_fir">C++</label>
<input id="cs_tab_fir" type="radio" class="tab" name="tab_fir">
<label class="tab_item" n=4 for="cs_tab_fir">C#</label>
<input id="python_tab_fir" type="radio" class="tab" name="tab_fir">
<label class="tab_item" n=4 for="python_tab_fir">Python</label>

```rust,edition2024
{{#include ../../../../codes/Users_Manual/modulation/fir.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/fir.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/fir.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/fir.py}}
```
</div>
