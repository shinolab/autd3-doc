# DebugSettings

`DebugSettings` allows you to set the output of GPIO output pins for each device.

<figure>
    <img src="../../fig/Users_Manual/gpio_pin.jpg"/>
    <figcaption>GPIO pins</figcaption>
</figure>

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
{{#include ../../../codes/Users_Manual/advanced/debug_setting.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/debug_setting.py}}
```
</div>

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
