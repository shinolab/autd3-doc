# Fir

You can apply an FIR filter using `Fir`.

Below is an example of applying an LPF with a sampling frequency of $\SI{20}{kHz}$, 199 taps, and a cutoff frequency of $\SI{200}{Hz}$.

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
