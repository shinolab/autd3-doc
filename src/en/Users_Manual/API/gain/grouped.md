# GainGroup

`GainGroup` is a `Gain` that set different `Gains` for each transducer.

> NOTE: If you only need to group by device, it is recommended to use [`Group`](../group.md).

In `GainGroup`, keys are assigned to transducers, and each key is associated with a `Gain`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/gain/group_0.rs}}
```
> NOTE: In the Rust version, the values of `HashMap` must all be of the same type, so `BoxedGain` is used here to unify the types.
{{ #endtab }}

{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/gain/group_0.cpp}}
```
> NOTE: In C++, `std::optional` must be used for the keys. Also, to unify the types, `std::shared_ptr<autd3::Gain>` is used.
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

In the above example, transducers with local indices from 0 to 100 output `Null`, and the rest output `Focus`.

> NOTE:
> In this sample, `&str` are used as keys, but any type that can be used as a key in `HashMap` is acceptable.
