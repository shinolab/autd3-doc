# Geometry

Geometry manages how AUTD3 devices are arranged in the real world.

[[_TOC_]]

## Device/Transducer Index

Devices are assigned an index starting from 0 in the order they are connected.

Each device has 249 transducers arranged, and they are assigned local indices (refer to "AUTD Surface Photo" in [Getting Started/Hardware](../getting_started/hardware.md)).

## Geometry API

- `num_devices()`: Get the number of enabled devices
- `num_transducers()`: Get the number of all enabled transducers
- `center()`: Get the center of all enabled transducers

Note that `Geometry` can be accessed directly from `Controller`.

<div class="tabs">
<input id="rust_tab_geometry" type="radio" class="tab" name="tab_geometry" checked>
<label class="tab_item" n=4 for="rust_tab_geometry">Rust</label>
<input id="cpp_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="cpp_tab_geometry">C++</label>
<input id="cs_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="cs_tab_geometry">C#</label>
<input id="python_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="python_tab_geometry">Python</label>

```rust
{{#include ../../../codes/Users_Manual/geometry_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/geometry_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/geometry_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/geometry_3.py}}
```
</div>

### Getting a Device

`Geometry` is a container of `Device`, and `Device` is a container of `Transducer`.

To get a `Device`, use an indexer.
Alternatively, you can use an iterator.

<div class="tabs">
<input id="rust_tab_device" type="radio" class="tab" name="tab_device" checked>
<label class="tab_item" n=4 for="rust_tab_device">Rust</label>
<input id="cpp_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="cpp_tab_device">C++</label>
<input id="cs_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="cs_tab_device">C#</label>
<input id="python_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="python_tab_device">Python</label>

```rust
{{#include ../../../codes/Users_Manual/geometry_4.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/geometry_4.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/geometry_4.cs}}
```

```python
{{#include ../../../codes/Users_Manual/geometry_4.py}}
```
</div>

## Device API

- `idx()`: Device index
- `enable`: Enable flag. When disabled, the data of the device will not be updated.
  - Note that it does not stop the output, it just stops updating the data.
- `sound_speed`: Get/set the speed of sound. The unit is mm/s. **It is recommended to set a value as close to reality as possible because it is used for phase calculation, etc.** The default speed of sound is $340\times 10^{3}\,\mathrm{mm/s}$, which corresponds to the speed of sound in air at approximately 15 degrees Celsius.
- `set_sound_speed_from_temp(temp)`: Set the speed of sound from the temperature `temp` [℃]. Note that `Geometry` also has a function with the same name, and using it will set the speed of sound from the temperature for all enabled devices.
- `translate(t)`: Translate by `t`
- `rotate(r)`: Rotate by `r`
- `affine(t, r)`: Affine transformation (translation by `t` and rotation by `r`)
- `wavelength()`: Wavelength of the ultrasound emitted by the device
- `wavenumber()`: Wavenumber of the ultrasound emitted by the device
- `rotation()`: Rotation of the device
- `x_direction()`: X-direction vector of the device
- `y_direction()`: Y-direction vector of the device
- `axial_direction()`: Axial direction vector of the device (direction the transducers face)

<div class="tabs">
<input id="rust_tab_device_api" type="radio" class="tab" name="tab_device_api" checked>
<label class="tab_item" n=4 for="rust_tab_device_api">Rust</label>
<input id="cpp_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="cpp_tab_device_api">C++</label>
<input id="cs_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="cs_tab_device_api">C#</label>
<input id="python_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="python_tab_device_api">Python</label>

```rust
{{#include ../../../codes/Users_Manual/device_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/device_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/device_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/device_0.py}}
```
</div>

### Getting a Transducer

`Device` is a container of `Transducer`, and `Transducer` stores information about each transducer.

To get a `Transducer`, use an indexer.
Alternatively, you can use an iterator.

<div class="tabs">
<input id="rust_tab_transducer" type="radio" class="tab" name="tab_transducer" checked>
<label class="tab_item" n=4 for="rust_tab_transducer">Rust</label>
<input id="cpp_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="cpp_tab_transducer">C++</label>
<input id="cs_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="cs_tab_transducer">C#</label>
<input id="python_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="python_tab_transducer">Python</label>

```rust
{{#include ../../../codes/Users_Manual/device_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/device_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/device_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/device_1.py}}
```
</div>

## Transducer API

The following information can be obtained.

- `idx()`: (Local) index of the transducer
- `dev_idx()`: Index of the device to which the transducer belongs
- `position()`: Position of the transducer

<div class="tabs">
<input id="rust_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api" checked>
<label class="tab_item" n=4 for="rust_tab_transducer_api">Rust</label>
<input id="cpp_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="cpp_tab_transducer_api">C++</label>
<input id="cs_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="cs_tab_transducer_api">C#</label>
<input id="python_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="python_tab_transducer_api">Python</label>

```rust
{{#include ../../../codes/Users_Manual/transducer_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/transducer_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/transducer_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/transducer_0.py}}
```
</div>

