# Output mask

> NOTE: Available since firmware v12.1.0

`OutputMask` can be sent to stop the output of each transducer regardless of the `Intensity` values of `Gain`, `FociSTM`, and `GainSTM`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/output_mask.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/output_mask.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/output_mask.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/output_mask.py}}
```
{{ #endtab }}
{{ #endtabs }}

The constructor argument for `OutputMask` is `Fn(&Device) -> Fn(&Transducer) -> bool` and the output of transducers set to `false` will be disabled.
