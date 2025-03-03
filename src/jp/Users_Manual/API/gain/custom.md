# Custom
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3/src/datagram/gain/custom.rs)

`Custom`はユーザーが自由に音場を生成するための`Gain`である.

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
{{#include ../../../../codes/Users_Manual/gain/custom_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/custom_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/custom_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/custom_0.py}}
```
</div>

`Custom`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Drive`である.
