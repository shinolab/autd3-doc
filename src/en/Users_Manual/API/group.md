# Group

Using the `Group`, you can group devices by device, and send different data for each group.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/group.rs}}
```
> NOTE: In the Rust version, since the values of `HashMap` must all be of the same type, `BoxedDatagram` is used here to unify the types.
{{ #endtab }}

{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/group.cpp}}
```
> NOTE: In C++, `std::optional` must be used for the keys. Also, to unify the types, `std::shared_ptr<driver::Datagram>` is used.
{{ #endtab }}

{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/group.cs}}
```
{{ #endtab }}

{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/group.py}}
```
{{ #endtab }}
{{ #endtabs }}

Unlike [`GainGroup`](./gain/grouped.md), you can use any data that can be sent with the usual `send`.
However, you can only group by device.

> NOTE:
> In this sample, strings are used as keys, but you can use anything that can be used as a key for `HashMap`.
