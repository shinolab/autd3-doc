# Fan Control
  
AUTD3 devices have fans with three modes: Auto, Off, and On.

In Auto mode, the temperature monitoring IC monitors the temperature of the IC and automatically activates the fan when it exceeds a certain temperature.
In Off mode, the fan is always off, and in On mode, the fan is always on.

The mode can be switched using the jumper switch next to the fan. It is a bit difficult to understand, but as shown in the figure below, shorting the fan side sets it to Auto, the middle to Off, and the right side to On.

<figure>
    <img src="../../fig/Users_Manual/fan.jpg"/>
    <figcaption>Jumper switch for AUTD fan control</figcaption>
</figure>

In Auto mode, the fan automatically activates when the temperature rises.

In Auto mode, the fan can be forcibly activated with `ForceFan`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/fan.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/fan.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/fan.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/fan.py}}
```
{{ #endtab }}
{{ #endtabs }}

The argument of the `ForceFan` constructor is `Fn(&Device) -> bool`, which specifies whether to forcibly drive the fan for each device.

> NOTE: You cannot forcibly turn off the fan in Auto mode.
