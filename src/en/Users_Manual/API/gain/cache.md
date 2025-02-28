# Cache

`Cache` caches the calculation results of another `Gain`.

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

> NOTE: `Cache` is only effective for `Gains` with heavy computation, so there is no point in caching `Null`. Be sure to benchmark when using `Cache`.
