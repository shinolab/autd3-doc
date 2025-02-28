# Group

`Group`は振動子ごとに別々の`Gain`を使用するための`Gain`である.

> NOTE: デバイスごとの分割で良いのであれば, [Controller::group_send](../controller.md#group_send)の使用を推奨する.

`Group`では, 振動子に対してキーを割り当て, その各キーに`Gain`を紐付けて使用する.

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
{{#include ../../../../codes/Users_Manual/gain/group_0.rs}}
```

> NOTE: Rust版は`HashMap`の値がすべて同じ型である必要があるため, ここでは`into_boxed`を使用して, 型を統一している.

```cpp
{{#include ../../../../codes/Users_Manual/gain/group_0.cpp}}
```

> NOTE: C++の場合, キーには`std::optional`を使用する必要がある. また, 型を統一するため, `std::shared_ptr<autd3::Gain>>`を使用している.

```cs
{{#include ../../../../codes/Users_Manual/gain/group_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/group_0.py}}
```
</div>

上の場合は, ローカルインデックスが$0$から$100$の振動子は`Null`を, それ以外の振動子は`Focus`を出力する.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, `HashMap`のキーとして使用できるものなら何でも良い.
