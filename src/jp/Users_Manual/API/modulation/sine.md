# Sine

音圧をSin波状に変形するための`Modulation`.

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
{{#include ../../../../codes/Users_Manual/modulation/sine_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/sine_0.py}}
```
</div>

`Sine`は音圧の波形が
$$
    \left\lfloor\frac{\text{intensity}}{2} \times \sin(2\pi ft + \text{phase}) + \text{offset}\right\rfloor
$$
となるようなAMをかける.

`clamp`が`false`だと, 上記の式において$[0,255]$の範囲外の値になるような`intensity, offset`が指定された場合にエラーを返す.
エラーを返すのではなく, 範囲外の値を$[0,255]$にクランプする場合は, `clamp`に`true`を指定する.

これらの値のデフォルトは上記の通りである.

## 周波数制約

`Sine`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

その場合はサンプリング設定を変更するか, `into_nearest`を使用することで, 出力可能な周波数の内で最も近い周波数で変調することができる.

<div class="tabs">
<input id="rust_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest" checked>
<label class="tab_item" n=4 for="rust_tab_api_nearest">Rust</label>
<input id="cpp_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="cpp_tab_api_nearest">C++</label>
<input id="cs_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="cs_tab_api_nearest">C#</label>
<input id="python_tab_api_nearest" type="radio" class="tab" name="tab_api_nearest">
<label class="tab_item" n=4 for="python_tab_api_nearest">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/modulation/sine_2.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/sine_2.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/sine_2.py}}
```
</div>
