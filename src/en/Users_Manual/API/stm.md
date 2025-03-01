# Spatio-Temporal Modulation

The SDK provides a feature for periodically switching sound fields called Spatio-Temporal Modulation (STM).
The SDK supports `FociSTM` for single to eight focal points and `GainSTM` for arbitrary `Gain`.
`FociSTM` and `GainSTM` use the timer on the AUTD3 hardware, providing high time precision but with some constraints.

- [FociSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## Common API for FociSTM/GainSTM

### Getting Sampling Configuration

You can get the sampling configuration with `sampling_config`.

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_prop.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm_prop.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm_prop.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm_prop.py}}
```
</div>

### LoopBehavior

In `FociSTM`/`GainSTM`, you can control the loop behavior.
The default is an infinite loop.

For details, refer to [Segment/LoopBehavior](./segment.md).

### Utilities

Only the Rust version provides utilities for generating linear and circular trajectories.

<div class="tabs">
<input id="rust_tab_util" type="radio" class="tab" name="tab_util" checked>
<label class="tab_item" n=1 for="rust_tab_util">Rust</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_utils.rs}}
```
</div>
