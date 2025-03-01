# Square

`Modulation` in the form of a square wave.

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
{{#include ../../../../codes/Users_Manual/modulation/square_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/square_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/square_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/square_0.py}}
```
</div>

## Frequency Constraints

`Square` is strict about frequency by default, and if a frequency that cannot be output due to the sampling frequency is specified, it returns an error.

In that case, you can change the sampling settings or use `into_nearest` to modulate at the nearest frequency that can be output.

<div class="tabs">
<input id="rust_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest" checked>
<label class="tab_item" n=4 for="rust_tab_api_nearest">Rust</label>
<input id="cpp_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="cpp_tab_api_nearest">C++</label>
<input id="cs_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="cs_tab_api_nearest">C#</label>
<input id="python_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="python_tab_api_nearest">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/modulation/square_3.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/square_3.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/square_3.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/square_3.py}}
```
</div>
