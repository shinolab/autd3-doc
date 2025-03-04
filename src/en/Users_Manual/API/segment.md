# Segment/LoopBehavior

## Segment

The data areas of `Modulation`, `Gain`, `FociSTM`, and `GainSTM` each have two `Segments`.

Unless otherwise specified, `Segment::S0` is used.

The `Segment` to which data is written is specified with `WithSegment`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_transition.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/segment_transition.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/segment_transition.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/segment_transition.py}}
```
{{ #endtab }}
{{ #endtabs }}

The `transition_mode` specifies the conditions for switching `Segments`.
- Only available when the destination segment is in an infinite loop
    - `Immediate`: Switch immediately
    - `Ext`: Switch immediately and enter extended mode (automatically switch segments after outputting data from each `Segment`)

- Only available when the destination segment is in a finite loop
    - `SyncIdx`: Switch when the data index of the destination `Segment` becomes $0$
    - `SysTime(DcSysTime)`: Switch at the specified time
    - `GPIO(GPIOIn)`: Switch when a signal is input to the specified GPIO pin

> NOTE: `Gain` only supports `Immediate`.

> To specify the loop behavior of the destination loop, refer to [`LoopBehavior`](#loopbehavior).

To write data without switching `Segments`, specify `None` for `transition_mode`.

### Switching Segments

To switch `Segments` only, use `SwapSegment`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.py}}
```
{{ #endtab }}
{{ #endtabs }}

### LoopBehavior

`Modulation`, `FociSTM`, and `GainSTM` can control loop behavior with `WithLoopBehavior`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/loop_behavior.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/loop_behavior.py}}
```
{{ #endtab }}
{{ #endtabs }}
