# Cache

`Cache`で計算結果をキャッシュしておくための`Modulation`を生成できる.

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
{{#include ../../../../codes/Users_Manual/modulation/cache_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/modulation/cache_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/modulation/cache_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/modulation/cache_0.py}}
```
</div>

> NOTE: ほとんどの`Modulation`に対して, キャッシュするより都度計算し直したほうが速い. 使用時は必ずベンチマークを取ること.
