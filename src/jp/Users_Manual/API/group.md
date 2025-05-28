# Group

`Group`を使用すると, デバイスをグループ分けし, 各グループごとに異なるデータを送信することができる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/group.rs}}
```
{{ #endtab }}

> NOTE: Rust版は`HashMap`の値がすべて同じ型である必要があるため, ここでは`into_boxed`を使用して, 型を統一している.

{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/group.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/group.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/group.py}}
```
{{ #endtab }}
{{ #endtabs }}

[`gain::Group`](./gain/grouped.md)とは異なり, 通常の`send`で送信できるデータなら何でも使用できる.
ただし, デバイス単位でしかグルーピングできない.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, `HashMap`のキーとして使用できるものなら何でも良い.
