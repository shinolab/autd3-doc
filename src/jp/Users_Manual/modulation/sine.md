# Sine

音圧をSin波状に変形するための`Modulation`.

コンストラクタには周波数$f$を指定する.

デフォルトのサンプリング周波数は$\SI{4}{kHz}$である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_0.py}}
```

## 振幅とオフセットの指定

`Sine`は音圧の波形が
$$
    \left\lfloor\frac{\text{intensity}}{2} \times \sin(2\pi ft) + \text{offset}\right\rfloor
$$
となるようなAMをかける.
ここで, intensityとoffsetはそれぞれ, `with_intensity`と`with_offset`で指定できる (デフォルトはそれぞれ$255$, $128$).

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_1.py}}
```

## 周波数制約

`Sine`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

その場合はサンプリング設定を変更するか, `new_nearest`を使用することで, 出力可能な周波数の内で最も近い周波数で変調することができる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_2.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_2.py}}
```

## 値のクランプ

デフォルトだと, 上記の式において$[0,255]$の範囲外の値になるような`intensity, offset`が指定された場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `with_clamp`に`true`を指定する.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_3.py}}
```
