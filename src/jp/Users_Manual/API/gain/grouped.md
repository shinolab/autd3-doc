# Group
[Source](https://github.com/shinolab/autd3-rs/blob/v32.0.1/autd3/src/datagram/gain/group.rs)

`Group`は振動子ごとに別々の`Gain`を使用するための`Gain`である.

> NOTE: デバイスごとの分割で良いのであれば, [Controller::group_send](../controller.md#group_send)の使用を推奨する.

`Group`では, 振動子に対してキーを割り当て, その各キーに`Gain`を紐付けて使用する.


{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/gain/group_0.rs}}
```
{{ #endtab }}

> NOTE: Rust版は`HashMap`の値がすべて同じ型である必要があるため, ここでは`into_boxed`を使用して, 型を統一している.
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/gain/group_0.cpp}}
```
{{ #endtab }}

> NOTE: C++の場合, キーには`std::optional`を使用する必要がある. また, 型を統一するため, `std::shared_ptr<autd3::Gain>>`を使用している.
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/gain/group_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/gain/group_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

上の場合は, ローカルインデックスが$0$から$100$の振動子は`Null`を, それ以外の振動子は`Focus`を出力する.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, `HashMap`のキーとして使用できるものなら何でも良い.
