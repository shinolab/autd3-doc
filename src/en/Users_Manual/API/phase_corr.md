# 位相補正

`PhaseCorrection`により, 位相を補正することができる.

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

`PhaseCorrection`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Phase`で, 振動子毎に指定した位相値が`Gain`, `FociSTM`, `GainSTM`の値に加算されるようになる.
