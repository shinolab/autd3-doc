# Fourier

`Modulation` that generates a waveform by superimposing multiple sine waves of different frequencies.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

## Scale Factor and Value Clamping

The calculation of `Fourier` is performed using the following formula,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{components}[i]\right\rfloor.
$$
If the scale factor is not specified, $1/\text{number of components}$ is used.

If `clamp` is `false`, it returns an error if `intensity, offset` are specified such that the above formula results in values outside the range of $[0,255]$.
To clamp values outside the range to $[0,255]$ instead of returning an error, specify `true` for `clamp`.

The default values for these are as above.