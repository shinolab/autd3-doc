# DebugSettings

`DebugSettings` allows you to set the output of GPIO output pins for each device.

<figure>
    <img src="../../fig/Users_Manual/gpio_pin.jpg"/>
    <figcaption>GPIO pins</figcaption>
</figure>

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/debug_setting.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/debug_setting.py}}
```
{{ #endtab }}
{{ #endtabs }}

The following data can be output.
- `None`: No output
- `BaseSignal`: Reference signal (50% duty cycle square wave with the same frequency as ultrasound)
- `Thermo`: Whether the temperature sensor is asserted
- `ForceFan`: Whether the ForceFan flag is asserted
- `Sync`: EtherCAT synchronization signal
- `ModSegment`: Modulation segment (High if segment is 1)
- `ModIdx(u16)`: High when the modulation index is the specified value
- `StmSegment`: STM segment (High if segment is 1)
- `StmIdx(u16)`: High when the STM index is the specified value
- `IsStmMode`: Whether FociSTM/GainSTM is being used
- `PwmOut(&Transducer)`: PWM output of the specified transducer
- `SysTimeEq(DcSysTime)`: High during the specified system time
- `Direct(bool)`: Output the specified value (if `true`, High; if `false`, Low)
