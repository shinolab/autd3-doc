# Segment/LoopBehavior

## Segment

The data areas of `Modulation`, `Gain`, `FociSTM`, and `GainSTM` each have two `Segments`.

Unless otherwise specified, `Segment::S0` is used.

The `Segment` to which data is written is specified with `WithSegment`.

<div class="tabs">
<input id="rust_tab_segment" type="radio" class="tab" name="tab_segment" checked>
<label class="tab_item" n=4 for="rust_tab_segment">Rust</label>
<input id="cpp_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="cpp_tab_segment">C++</label>
<input id="cs_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="cs_tab_segment">C#</label>
<input id="python_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="python_tab_segment">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_transition.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/segment_transition.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/segment_transition.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/segment_transition.py}}
```
</div>

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

<div class="tabs">
<input id="rust_tab_swap" type="radio" class="tab" name="tab_swap" checked>
<label class="tab_item" n=4 for="rust_tab_swap">Rust</label>
<input id="cpp_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="cpp_tab_swap">C++</label>
<input id="cs_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="cs_tab_swap">C#</label>
<input id="python_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="python_tab_swap">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.py}}
```
</div>

### LoopBehavior

`Modulation`, `FociSTM`, and `GainSTM` can control loop behavior with `WithLoopBehavior`.

<div class="tabs">
<input id="rust_tab_loop" type="radio" class="tab" name="tab_loop" checked>
<label class="tab_item" n=4 for="rust_tab_loop">Rust</label>
<input id="cpp_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="cpp_tab_loop">C++</label>
<input id="cs_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="cs_tab_loop">C#</label>
<input id="python_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="python_tab_loop">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/loop_behavior.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/loop_behavior.py}}
```
</div>
