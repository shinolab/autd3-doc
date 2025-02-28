# Bessel

`Bessel` generates a Bessel beam.
This `Gain` is based on the paper by Hasegawa et al. [^hasegawa2017].

<div class="tabs">
<input id="rust_tab_bessel" type="radio" class="tab" name="tab_bessel" checked>
<label class="tab_item" n=4 for="rust_tab_bessel">Rust</label>
<input id="cpp_tab_bessel" type="radio" class="tab" name="tab_bessel">
<label class="tab_item" n=4 for="cpp_tab_bessel">C++</label>
<input id="cs_tab_bessel" type="radio" class="tab" name="tab_bessel">
<label class="tab_item" n=4 for="cs_tab_bessel">C#</label>
<input id="python_tab_bessel" type="radio" class="tab" name="tab_bessel">
<label class="tab_item" n=4 for="python_tab_bessel">Python</label>

```rust,edition2024
{{#include ../../../../codes/Users_Manual/gain/bessel_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/bessel_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/bessel_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/bessel_0.py}}
```
</div>

Here, `pos` is the apex of the virtual cone (dotted line in the figure below) that generates the beam, `dir` is the direction of the beam, and `theta` is the angle between the plane perpendicular to the beam and the side of the virtual cone that generates the beam ($\theta_z$ in the figure below).

<figure>
  <img src="../../../fig/Users_Manual/1.4985159.figures.online.f1.jpg"/>
  <figcaption>Bessel beam (cited from the paper by Hasegawa et al.)</figcaption>
</figure>

Optionally, you can specify the output intensity and phase offset.
The default values are as above.

[^hasegawa2017]: Hasegawa, Keisuke, et al. "Electronically steerable ultrasound-driven long narrow air stream." Applied Physics Letters 111.6 (2017): 064104.
