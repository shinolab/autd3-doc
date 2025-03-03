# Greedy
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3-gain-holo/src/combinatorial/greedy.rs)

Greedy Algorithm with Brute-Force Search, 鈴木らの論文[^suzuki2021]に基づく多焦点`Gain`.

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
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.rs}}
```

```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cpp}}
```

```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.cs}}
```

```python
{{#include ../../../../../codes/Users_Manual/gain/holo/greedy.py}}
```
</div>

`phase_div`は位相の離散化深度, デフォルトは上記の通り.
パラメータの詳細は論文[^suzuki2021]を参照されたい.

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
