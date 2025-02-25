# Square

矩形波状の`Modulation`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/modulation/square_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_0.py}}
```

## 周波数制約

`Square`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

その場合はサンプリング設定を変更するか, `into_nearest`を使用することで, 出力可能な周波数の内で最も近い周波数で変調することができる.

```rust,edition2024
{{#include ../../../codes/Users_Manual/modulation/square_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_3.py}}
```
