# Intensity and Pulse Width

There is a nonlinear relationship between the duty ratio of the PWM signal and the ultrasound output.
To correct this relationship, you can use `PulseWidthEncoder`.

Inside the firmware, there is a table that determines the pulse width ($0$--$511$) of the PWM signal using the value ($0$--$255$) obtained by multiplying the `EmitIntensity` data of `Gain`/`FociSTM`/`GainSTM` by the data of `Modulation` ($0$--$255$) and dividing by $255$.
This table can be modified by `PulseWidthEncoder`.
Note that the period of the PWM signal is 512.

By default, to make the intensity value and ultrasound output (theoretically) linear,
$$
    \text{table}(i) = \left[\sin^{-1}\left(\frac{i}{255}\right) \times \frac{512}{\pi}\right]
$$
is written to the table.
Here, $[\cdot]$ represents the nearest integer.

For example, if you send the following `PulseWidthEncoder`, the relationship between the intensity value and the pulse width will be linear (i.e., the intensity value and ultrasound output will be nonlinear).

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.py}}
```
{{ #endtab }}
{{ #endtabs }}

The constructor argument is a function `Fn(&Device) -> Fn(EmitIntensity) -> PulseWidth` that returns a function that returns the pulse width for each device using the table index as an argument.

## Note for using v10 firmware

When using the v10 firmware from the Rust, use `autd3::prelude::v10::PulseWidthEncoder` instead of `autd3::prelude::PulseWidthEncoder`.
This is not supported other than Rust.
