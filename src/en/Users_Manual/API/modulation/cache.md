# Cache

You can generate a `Modulation` to cache the calculation results using `Cache`.

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

> NOTE: For most `Modulation`, it is faster to recalculate each time rather than cache. Always benchmark when using.
