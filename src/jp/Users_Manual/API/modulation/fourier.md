# Fourier
[Source](https://github.com/shinolab/autd3-rs/blob/v32.0.1/autd3/src/datagram/modulation/fourier.rs)

複数の周波数の正弦波を重ね合わせた波形を生成する`Modulation`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/fourier_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

## スケールファクタと値のクランプ

`Fourier`の計算は, 以下の式で行われる,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{components}[i]\right\rfloor.
$$
スケールファクタが指定されていない場合, $1/\text{コンポーネント数}$が使用される.

`clamp`が`false`だと, 上記の式において$[0,255]$の範囲外の値になるような`intensity, offset`が指定された場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `clamp`に`true`を指定する.

これらの値のデフォルトは上記の通りである.