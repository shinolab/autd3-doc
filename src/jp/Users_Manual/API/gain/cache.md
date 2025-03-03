# Cache
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/gain/cache.rs)

`Cache`によって`Gain`の計算結果をキャッシュする`Gain`を生成できる.

<div class="tabs">
<input id="rust_tab_cache" type="radio" class="tab" name="tab_cache" checked>
<label class="tab_item" n=4 for="rust_tab_cache">Rust</label>
<input id="cpp_tab_cache" type="radio" class="tab" name="tab_cache">
<label class="tab_item" n=4 for="cpp_tab_cache">C++</label>
<input id="cs_tab_cache" type="radio" class="tab" name="tab_cache">
<label class="tab_item" n=4 for="cs_tab_cache">C#</label>
<input id="python_tab_cache" type="radio" class="tab" name="tab_cache">
<label class="tab_item" n=4 for="python_tab_cache">Python</label>

```rust,edition2024
{{#include ../../../../codes/Users_Manual/gain/cache_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/cache_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/cache_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/cache_0.py}}
```
</div>

> NOTE: 当然ながら, `Cache`は計算処理が重い`Gain`に対してのみ有効なため, 実際には`Null`をキャッシュする意味はない. 使用時は必ずベンチマークを取ること.
