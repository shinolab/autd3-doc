# Group

`Group` is a `Gain` that set different `Gains` for each transducer.

> NOTE: If you only need to group by device, it is recommended to use [Controller::group_send](../controller.md#group_send).

In `Group`, keys are assigned to transducers, and each key is associated with a `Gain`.

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/gain/group_0.rs}}
```

> NOTE: In the Rust version, the values of `HashMap` must all be of the same type, so `into_boxed` is used here to unify the types.

```cpp
{{#include ../../../../codes/Users_Manual/gain/group_0.cpp}}
```

> NOTE: In C++, `std::optional` must be used for the keys. Also, to unify the types, `std::shared_ptr<autd3::Gain>` is used.

```cs
{{#include ../../../../codes/Users_Manual/gain/group_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/group_0.py}}
```
</div>

In the above example, transducers with local indices from 0 to 100 output `Null`, and the rest output `Focus`.

> NOTE:
> In this sample, `&str` are used as keys, but any type that can be used as a key in `HashMap` is acceptable.
