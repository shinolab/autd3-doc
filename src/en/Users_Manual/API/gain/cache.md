# Cache

`Cache` caches the calculation results of another `Gain`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
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

> NOTE: `Cache` is only effective for `Gains` with heavy computation, so there is no point in caching `Null`. Be sure to benchmark when using `Cache`.
