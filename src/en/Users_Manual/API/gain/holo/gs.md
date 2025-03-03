# GS

Gershberg-Saxon, `Gain` for multiple focal points based on the paper by Marzo et al.[^marzo2019].

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
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.rs}}
```

```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.cpp}}
```

```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.cs}}
```

```python
{{#include ../../../../../codes/Users_Manual/gain/holo/gs.py}}
```
</div>

`repeat` is the number of iterations, the default is as above.
For details on the parameters, refer to the paper[^marzo2019].

[^marzo2019]: Marzo, Asier, and Bruce W. Drinkwater. "Holographic acoustic tweezers." Proceedings of the National Academy of Sciences 116.1 (2019): 84-89.
