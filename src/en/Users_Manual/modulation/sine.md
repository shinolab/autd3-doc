# Sine

`Modulation` to transform the square of the sound pressure to a sine wave.

Specify the frequency $f$ as an integer in the constructor.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_0.py}}
```

## Set intensity and offset

`Sine` applies AM so that the waveform of the sound pressure is
$$
    \frac{intensity}{2} \times \sin(2\pi ft) + \frac{offset}{2}
$$
Here, $intensity$ and $offset$ can be specified by `with_intensity` and `with_offset`, respectively (defaults are `0xFF`).

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_1.py}}
```
