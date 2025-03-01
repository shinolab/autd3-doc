# Controller

This section introduces the APIs available in the `Controller` class.

[[_TOC_]]

## fpga_state

Retrieve the state of the FPGA.
Before using this, you need to enable state retrieval with `ReadsFPGAState`.

<div class="tabs">
<input id="rust_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state" checked>
<label class="tab_item" n=4 for="rust_tab_fpga_state">Rust</label>
<input id="cpp_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="cpp_tab_fpga_state">C++</label>
<input id="cs_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="cs_tab_fpga_state">C#</label>
<input id="python_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="python_tab_fpga_state">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/controller_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/controller_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/controller_0.py}}
```
</div>

The argument of the `ReadsFPGAState` constructor is `Fn(&Device) -> bool`, which specifies whether to enable state retrieval for each device.

`fpga_state` returns `None` for devices that are not enabled.

The following information can currently be obtained as the state of the FPGA:

- `is_thermal_assert`: Whether the temperature sensor for fan control is asserted
- `current_mod_segment`: Current Modulation Segment
- `current_stm_segment`: Current FociSTM/GainSTM Segment
- `current_gain_segment`: Current Gain Segment
- `is_gain_mode`: Whether Gain is currently being used
- `is_stm_mode`: Whether FociSTM/GainSTM is currently being used

## send

Send data to the device.

Data can be sent either individually or two at a time.

## group_send

Using the `group_send` function, you can group devices.

<div class="tabs">
<input id="rust_tab_group" type="radio" class="tab" name="tab_group" checked>
<label class="tab_item" n=4 for="rust_tab_group">Rust</label>
<input id="cpp_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="cpp_tab_group">C++</label>
<input id="cs_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="cs_tab_group">C#</label>
<input id="python_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="python_tab_group">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_2.rs}}
```

> NOTE: In the Rust version, since the values of `HashMap` must all be of the same type, `into_boxed` is used here to unify the types.

```cpp
{{#include ../../../codes/Users_Manual/controller_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/controller_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/controller_2.py}}
```
</div>

Unlike `gain::Group`, you can use any data that can be sent with the usual `send`.
However, you can only group by device.

> NOTE:
> In this sample, strings are used as keys, but you can use anything that can be used as a key for `HashMap`.

## sender

You can specify settings for sending via `sender`.

<div class="tabs">
<input id="rust_tab_sender" type="radio" class="tab" name="tab_sender" checked>
<label class="tab_item" n=4 for="rust_tab_sender">Rust</label>
<input id="cpp_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="cpp_tab_sender">C++</label>
<input id="cs_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="cs_tab_sender">C#</label>
<input id="python_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="python_tab_sender">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/sender.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/sender.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/sender.cs}}
```

```python
{{#include ../../../codes/Users_Manual/sender.py}}
```
</div>

Here,
- `send_interval`: Send interval
- `receive_interval`: Receive interval
- `timeout`: Timeout duration. See [About Timeout](#about-timeout) for details
- `parallel`: Parallel computation mode. See [About Parallel Computation](#about-parallel-computation) for details
- `sleeper`: Structure to adjust send/receive intervals
    - `SpinSleeper`: Uses [`spin_sleep`](https://crates.io/crates/spin_sleep)
    - `StdSleeper`: Uses `std::thread::sleep`
    - `WaitableSleeper`: (Windows only) Uses [`Waitable Timer`](https://learn.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects)
and the default values are as above.

Note that `Controller::send` and `Controller::group_send` are equivalent to `Sender::send` and `Sender::group_send` with the default `SenderOption`.

### About Timeout

If the timeout value is
- greater than 0, the `send` function waits until the sent data is processed by the device or the specified timeout duration elapses. If it cannot confirm that the sent data was processed by the device, it returns an error.
- 0, the `send` function does not check whether the sent data was processed by the device.

If you want to ensure that the data is sent, it is recommended to set this to an appropriate value.

If timeout is not specified in `SenderOption`, the default values for each data are used as shown below.

|       | Timeout Value   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`PulseWidthEncoder`/`ReadsFPGAState`/<br>`SwapSegment`/`Silencer`/<br>`Synchronize`/`FociSTM`/<br>`GainSTM`/`Modulation` | $\SI{200}{ms}$ | 
| `Gain`  | $\SI{20}{ms}$ | 

When sending multiple data at once, the maximum timeout value of each data is used.

### About Parallel Computation

Internal calculations for each data can be executed in parallel on a per-device basis.

Specifying `ParallelMode::On` enables parallel computation, and `ParallelMode::Off` disables it.

In the case of `ParallelMode::Auto`, parallel computation is enabled if the number of enabled devices exceeds the parallel computation threshold value for each data as shown below.

|       | Parallel Computation Threshold Value   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`ReadsFPGAState`/`SwapSegment`/<br>`Silencer`/`Synchronize`/<br>`FociSTM` (less than 4000 foci)/<br>`Modulation` | 18446744073709551615 | 
| `PulseWidthEncoder`/<br>`FociSTM` (4000 foci or more)/<br>/`GainSTM`/`Gain` | 4 |
