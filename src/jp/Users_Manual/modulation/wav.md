# Wav

`Wav`はWavファイルをもとに構成される`Modulation`である.

## Install

### Rust

```shell
cargo add autd3-modulation-audio-file
```

### C++ (CMake)

```ignore,filename=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::modulation::audio_file)
```

### C#/Unity/Python

メインライブラリに含まれている.

## APIs

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/wav_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/wav_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/wav_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/wav_0.py}}
```

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
