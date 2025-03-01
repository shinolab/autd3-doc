# Phase Correction

`PhaseCorrection` allows you to correct the phase.

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/phase_corr.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/phase_corr.py}}
```
</div>

The constructor argument for `PhaseCorrection` is `Fn(&Device) -> Fn(&Transducer) -> Phase`, which specifies the phase value for each transducer to be added to the values of `Gain`, `FociSTM`, and `GainSTM`.
