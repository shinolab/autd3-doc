# Bessel

`Bessel` generates a Bessel beam.
This `Gain` is based on the paper by Hasegawa et al. [^hasegawa2017].

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/gain/bessel_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/gain/bessel_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/gain/bessel_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/gain/bessel_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

Here, `apex` is the apex of the virtual cone (dotted line in the figure below) that generates the beam, `dir` is the direction of the beam, and `theta` is the angle between the plane perpendicular to the beam and the side of the virtual cone that generates the beam ($\theta_z$ in the figure below).

<figure>
  <img src="../../../fig/Users_Manual/1.4985159.figures.online.f1.jpg"/>
  <figcaption>Bessel beam (cited from the paper by Hasegawa et al.)</figcaption>
</figure>

Optionally, you can specify the output intensity and phase offset.
The default values are as above.

[^hasegawa2017]: Hasegawa, Keisuke, et al. "Electronically steerable ultrasound-driven long narrow air stream." Applied Physics Letters 111.6 (2017): 064104.
