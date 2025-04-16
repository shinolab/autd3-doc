# Cache
[Source](https://github.com/shinolab/autd3-rs/blob/v32.1.0/autd3/src/datagram/gain/cache.rs)

`Cache`によって`Gain`の計算結果をキャッシュする`Gain`を生成できる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/gain/cache_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/gain/cache_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/gain/cache_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/gain/cache_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: 当然ながら, `Cache`は計算処理が重い`Gain`に対してのみ有効なため, 実際には`Null`をキャッシュする意味はない. 使用時は必ずベンチマークを取ること.
