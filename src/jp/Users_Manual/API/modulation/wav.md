# Wav
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3-modulation-audio-file/src/wav.rs)

`Wav`はWavファイルをもとに構成される`Modulation`である.

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
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Unity }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Python }}
メインライブラリに含まれている.
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

Wavデータとして, モノラル, かつ, 8,16,24,32bit整数, 及び, 32bit浮動小数点数のデータ形式に対応している.

それぞれのデータ値$x$は以下の式を通して, 8bit符号なし整数の変調データに変換される.
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
ここで$[\cdot]$は最も近い整数を表す.
