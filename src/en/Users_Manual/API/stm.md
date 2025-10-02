# Spatio-Temporal Modulation

The SDK provides a feature for periodically switching sound fields called Spatio-Temporal Modulation (STM).
The SDK supports `FociSTM` for single to eight focal points and `GainSTM` for arbitrary `Gain`.
`FociSTM` and `GainSTM` use the timer on the AUTD3 hardware, providing high time precision but with some constraints.

- [FociSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## Common API for FociSTM/GainSTM

### Getting Sampling Configuration

You can get the sampling configuration with `sampling_config`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_prop.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/stm_prop.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/stm_prop.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/stm_prop.py}}
```
{{ #endtab }}
{{ #endtabs }}

### FiniteLoop

In `FociSTM`/`GainSTM`, you can control the loop behavior.
The default is an infinite loop.

For details, refer to [Segment/FiniteLoop](./segment.md).

### Utilities

Only the Rust version provides utilities for generating linear and circular trajectories.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_utils.rs}}
```
{{ #endtab }}
{{ #endtabs }}
