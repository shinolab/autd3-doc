# FociSTM

- The maximum number of sound field patterns is $8192$
  - In extended mode, it is $16384$
- The sampling rate is $\ufreq/N$, where $N$ is a 16-bit unsigned integer greater than 0

The usage of `FociSTM` is as follows.
This is a sample that rotates a focus on the circumference of a circle with a radius of $\SI{30}{mm}$ centered at a point $\SI{150}{mm}$ directly above the center of the array.
The circumference is sampled at 200 points, rotating at $\SI{1}{Hz}$. (That is, the sampling frequency is $\SI{200}{Hz}$.)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/focus_stm.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/stm/focus_stm.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/stm/focus_stm.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/stm/focus_stm.py}}
```
{{ #endtab }}
{{ #endtabs }}

In `config`, you can specify the frequency, period, and sampling settings.

Due to constraints on the number of sampling points and the sampling period, it may not be possible to output at the specified frequency.
For example, in the above example, to rotate 200 points at $\SI{1}{Hz}$, the sampling frequency should be $\SI{200}{Hz}=\ufreq/200$.
However, if `point_num=199`, the sampling frequency must be $\SI{199}{Hz}$, but there is no integer $N$ that satisfies $\SI{199}{Hz}=\ufreq/N$, resulting in an error.

Using `FociSTM::into_nearest`, the nearest $N$ is selected, but note that the actual frequency may differ from the specified frequency.

## Multiple Foci

`FociSTM` can output up to 8 foci simultaneously.

Below is an example with 2 foci.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/foci_1.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/stm/foci_1.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/stm/foci_1.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/stm/foci_1.py}}
```
{{ #endtab }}
{{ #endtabs }}

The multi-focus sound field of `FociSTM` is a simple superposition of single-focus sound fields.
That is, for the position of the transducer $x_\text{t}$, each focus position $x_i$, ultrasonic frequency $f$, and speed of sound $c$, the phase $\theta$ is calculated as follows.
$$
\theta = \angle \sum_i \mathrm{e}^{2\pi\mathrm{j}\frac{f}{c}\|x_i-x_\text{t}\| + \mathrm{j}\phi_i}
$$
Here, $\phi_i$ is the phase offset of each focus.
For amplitude, the specified value from the software is used **instead of** $\displaystyle \left\|\sum_i\mathrm{e}^{2\pi\mathrm{j}\frac{f}{c}\|x_i-x_\text{t}\| + \mathrm{j}\phi_i}\right\|$.

## Constraints

To reduce data volume, `FociSTM` encodes the focus position coordinates as $\SI{18}{bit}$ signed fixed-point numbers with a unit of $\SI{0.025}{mm}$.
Therefore, for each axis direction, only foci within the range of $[\SI{-3276.8}{mm}, \SI{3276.775}{mm}]$ from all transducers can be output.

Also, since internal calculations are performed with fixed-point numbers, the phase may differ from that of `gain::Focus`.
