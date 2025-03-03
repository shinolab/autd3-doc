# Bessel
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/gain/bessel.rs)

`Bessel`ではBessel beamを生成する.
この`Gain`は長谷川らの論文[^hasegawa2017]に基づく.

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

ここで, `pos`はビームを生成する仮想円錐 (下図の点線) の頂点であり, `dir`はビームの方向, `theta`はビームに垂直な面とビームを生成する仮想円錐の側面となす角度である (下図の$\theta_z$).

<figure>
  <img src="../../../fig/Users_Manual/1.4985159.figures.online.f1.jpg"/>
  <figcaption>Bessel beam (長谷川らの論文より引用)</figcaption>
</figure>

オプションにて, 出力振幅と位相オフセットを指定できる.
デフォルト値は上記の通り.

[^hasegawa2017]: Hasegawa, Keisuke, et al. "Electronically steerable ultrasound-driven long narrow air stream." Applied Physics Letters 111.6 (2017): 064104.
