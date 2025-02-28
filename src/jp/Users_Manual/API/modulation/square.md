# Square

矩形波状の`Modulation`.

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
{{#include ../../../../codes/Users_Manual/modulation/square_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/square_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/square_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/square_0.py}}
```
</div>

## 周波数制約

`Square`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

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
{{#include ../../../../codes/Users_Manual/modulation/square_3.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/square_3.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/square_3.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/square_3.py}}
```
</div>
