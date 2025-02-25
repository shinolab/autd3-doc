# Fourier

複数の周波数の正弦波を重ね合わせた波形を生成する`Modulation`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/modulation/fourier_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/fourier_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/fourier_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/fourier_0.py}}
```

## スケールファクタと値のクランプ

`Fourier`の計算は, 以下の式で行われる,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{components}[i]\right\rfloor.
$$
スケールファクタが指定されていない場合, $1/\text{コンポーネント数}$が使用される.

また, デフォルトだと, 上記の式において$[0,255]$の範囲外の値になる場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `clamp`に`true`を指定する.
