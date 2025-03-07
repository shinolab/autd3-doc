# Cache
[Source](https://github.com/shinolab/autd3-rs/blob/v31.0.1/autd3/src/datagram/modulation/cache.rs)

`Cache`で計算結果をキャッシュしておくための`Modulation`を生成できる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/modulation/cache_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/modulation/cache_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/modulation/cache_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/modulation/cache_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: ほとんどの`Modulation`に対して, キャッシュするより都度計算し直したほうが速い. 使用時は必ずベンチマークを取ること.
