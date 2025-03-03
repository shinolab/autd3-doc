# GSPAT

Gershberg-Saxon for Phased Arrays of Transducers, `Gain` for multiple focal points based on the paper by Plasencia et al.[^plasencia2020].

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
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.rs}}
```

```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.cpp}}
```

```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.cs}}
```

```python
{{#include ../../../../../codes/Users_Manual/gain/holo/gspat.py}}
```
</div>

`repeat` is the number of iterations, the default is as above.
For details on the parameters, refer to the paper[^plasencia2020].

[^plasencia2020]: Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers." ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.
