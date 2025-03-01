# Sine

`Modulation` to transform sound pressure into a sine wave.

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
{{#include ../../../../codes/Users_Manual/modulation/sine_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/sine_0.py}}
```
</div>

`Sine` applies AM so that the waveform of the sound pressure becomes
$$
    \left\lfloor\frac{\text{intensity}}{2} \times \sin(2\pi ft + \text{phase}) + \text{offset}\right\rfloor
$$

If `clamp` is `false`, it returns an error if `intensity, offset` are specified such that the above formula results in values outside the range of $[0,255]$.
To clamp values outside the range to $[0,255]$ instead of returning an error, specify `true` for `clamp`.

The default values for these are as above.

## Frequency Constraints

`Sine` is strict about frequency by default, and if a frequency that cannot be output due to the sampling frequency is specified, it returns an error.

In that case, you have to change the sampling settings or use `into_nearest` to modulate at the nearest frequency that can be output.

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
{{#include ../../../../codes/Users_Manual/modulation/sine_2.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/sine_2.py}}
```
</div>
