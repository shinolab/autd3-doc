# Greedy

Greedy Algorithm with Brute-Force Search, `Gain` for multiple focal points based on the paper by Suzuki et al.[^suzuki2021].

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
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.rs}}
```

```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cpp}}
```

```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cs}}
```

```python
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.py}}
```
</div>

`phase_div` is the discretization depth of the phase, the default is as above.
For details on the parameters, refer to the paper[^suzuki2021].

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
