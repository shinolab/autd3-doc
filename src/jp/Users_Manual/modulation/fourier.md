# Fourier

複数の周波数の正弦波を重ね合わせた波形を生成する`Modulation`.

```rust,edition2021
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

## 位相パラメータ

`Fourier`のために, `Sine`には位相パラメータを指定する機能がある.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/fourier_2.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/fourier_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/fourier_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/fourier_2.py}}
```

## スケールファクタと値のクランプ

`Fourier`の計算は, 以下の式で行われる,
$$
    \left\lfloor\text{offset} + \text{scale\_factor} \times \sum_i \text{Sine}[i]\right\rfloor.
$$
スケールファクタはデフォルトでは$1/\text{コンポーネント数}$に設定されている.
また, offsetはデフォルトでは$0$に設定されている.
これらを変更する場合は, それぞれ, `with_scale_factor`, `with_offset`を使用する.

また, デフォルトだと, 上記の式において$[0,255]$の範囲外の値になる場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `with_clamp`に`true`を指定する.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/fourier_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/fourier_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/fourier_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/fourier_3.py}}
```

