# Wav

`Wav` is a `Modulation` composed based on Wav files.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-modulation-audio-file
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::modulation::audio_file)
```
{{ #endtab }}
{{ #tab name=C# }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Unity }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Python }}
Included in the main library.
{{ #endtab }}
{{ #endtabs }}

## APIs

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/wav_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/wav_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/wav_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/wav_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

Wav data supports mono, 8, 16, 24, 32-bit integers and 32-bit floating point data formats.

Each data value $x$ is converted to 8-bit unsigned integer modulation data through the following formulas.
$$
\text{8bit int}: x + 128
$$
$$
\text{16bit int}: \left[\frac{x + 32768}{257}\right]
$$
$$
\text{24bit int}: \left[\frac{x + 8388608}{65793}\right]
$$
$$
\text{32bit int}: \left[\frac{x + 2147483648}{16843009}\right]
$$
$$
\text{32bit float}: \left[\frac{x + 1}{2} \times 255\right]
$$
Here, $[\cdot]$ represents the nearest integer.
