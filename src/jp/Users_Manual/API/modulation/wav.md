# Wav

`Wav`はWavファイルをもとに構成される`Modulation`である.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5 for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-modulation-audio-file
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::modulation::audio_file)
```

<div class="tab_content" id="cs_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="unity_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="python_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>
</div>

## APIs

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/modulation/wav_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/wav_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/wav_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/wav_0.py}}
```
</div>

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
