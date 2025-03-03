# Fourier
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/modulation/fourier.rs)

複数の周波数の正弦波を重ね合わせた波形を生成する`Modulation`.

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
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.py}}
```
</div>

## スケールファクタと値のクランプ

`Fourier`の計算は, 以下の式で行われる,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{components}[i]\right\rfloor.
$$
スケールファクタが指定されていない場合, $1/\text{コンポーネント数}$が使用される.

`clamp`が`false`だと, 上記の式において$[0,255]$の範囲外の値になるような`intensity, offset`が指定された場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `clamp`に`true`を指定する.

これらの値のデフォルトは上記の通りである.