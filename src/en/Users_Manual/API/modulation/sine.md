# Sine

`Modulation` to transform sound pressure into a sine wave.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/sine_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/sine_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

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

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/sine_2.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/sine_2.py}}
```
{{ #endtab }}
{{ #endtabs }}
