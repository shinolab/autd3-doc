# Controller

This section introduces the APIs available in the `Controller`.

[[_TOC_]]

## fpga_state

Retrieve the state of the FPGA.
Before using this, you need to enable state retrieval with `ReadsFPGAState`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/controller_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/controller_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/controller_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

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

## sender

You can specify settings for sending via `sender`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/sender.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/sender.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/sender.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/sender.py}}
```
{{ #endtab }}
{{ #endtabs }}

Here,
- `send_interval`: Send interval
- `receive_interval`: Receive interval
- `timeout`: Timeout duration. See [About Ack check](#about-ack-check) for details.
- `parallel`: Parallel computation mode. See [About Parallel Computation](#about-parallel-computation) for details.

and the default values are as above.

Note that `Controller::send` is equivalent to `Sender::send` with the `Controller::default_sender_option` (which is configurable).

### About ack check

If the timeout value is
- greater than 0, the `send` function waits until the sent data is processed by the device or the specified timeout duration elapses. If it cannot confirm that the sent data was processed by the device, it returns an error.
- 0, the `send` function does not check whether the sent data was processed by the device.

If you want to ensure that the data is sent, it is recommended to set this to an appropriate value.

If timeout is not specified in `SenderOption`, the default value ($\SI{200}{ms}$) is used.

When sending multiple data at once, the maximum timeout value of each data is used.

### About Parallel Computation

Internal calculations for each data can be executed in parallel on a per-device basis.

Specifying `ParallelMode::On` enables parallel computation, and `ParallelMode::Off` disables it.

In the case of `ParallelMode::Auto`, parallel computation is enabled if the number of devices exceeds the parallel computation threshold value for each data as shown below.

|       | Parallel Computation Threshold Value   | 
| ----- | -------------- | 
| `Clear`/`GPIOOutputs`/<br>`ForceFan`/`PhaseCorrection`/<br>`ReadsFPGAState`/`SwapSegment`/<br>`Silencer`/`Synchronize`/<br>`FociSTM` (less than 4000 foci)/<br>`Modulation` | 18446744073709551615 | 
| `PulseWidthEncoder`/<br>`FociSTM` (4000 foci or more)/<br>/`GainSTM`/`Gain` | 4 |


## `inspect` (available only in Rust)

The calculations for `Gain`, `Modulation`, `GainSTM`, and `FociSTM` are lazy for parallelization and to minimize memory allocation, and the calculation results are constructed directly within the frame.
Therefore, it is not possible to directly check these calculation results before sending.

By using `Controller::inspect`, you can check these calculation results without sending.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_inspect.rs}}
```
{{ #endtab }}
{{ #endtabs }}
