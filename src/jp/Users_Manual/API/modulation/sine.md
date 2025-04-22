# Sine
[Source](https://github.com/shinolab/autd3-rs/blob/v32.1.1/autd3/src/datagram/modulation/sine.rs)

音圧をSin波状に変形するための`Modulation`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/sine_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/sine_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

`Sine`は音圧の波形が
$$
    \left\lfloor\frac{\text{intensity}}{2} \times \sin(2\pi \times \text{freq} \times t + \text{phase}) + \text{offset}\right\rfloor
$$
となるようなAMをかける.
ここで$\lfloor\cdot\rfloor$は床関数を表す.

`clamp`が`false`だと, 上記の式において$[0,255]$の範囲外の値になるような`intensity, offset`が指定された場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `clamp`に`true`を指定する.

これらの値のデフォルトは上記の通りである.

## 周波数制約

`Sine`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

その場合はサンプリング設定を変更するか, `into_nearest`を使用することで, 出力可能な周波数の内で最も近い周波数で変調することができる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/modulation/sine_2.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/sine_2.py}}
```
{{ #endtab }}
{{ #endtabs }}

