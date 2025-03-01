# Fourier

`Modulation` that generates a waveform by superimposing multiple sine waves of different frequencies.

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
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.py}}
```
</div>

## Scale Factor and Value Clamping

The calculation of `Fourier` is performed using the following formula,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{components}[i]\right\rfloor.
$$
If the scale factor is not specified, $1/\text{number of components}$ is used.

If `clamp` is `false`, it returns an error if `intensity, offset` are specified such that the above formula results in values outside the range of $[0,255]$.
To clamp values outside the range to $[0,255]$ instead of returning an error, specify `true` for `clamp`.

The default values for these are as above.