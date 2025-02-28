# Custom

`Custom` is a `Gain` that allows the user to freely generate sound fields.

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
{{#include ../../../../codes/Users_Manual/gain/custom_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/custom_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/custom_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/custom_0.py}}
```
</div>

The argument of the `Custom` constructor is `Fn(&Device) -> Fn(&Transducer) -> Drive`.
