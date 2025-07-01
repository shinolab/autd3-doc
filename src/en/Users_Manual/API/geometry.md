# Geometry

Geometry manages how AUTD3 devices are arranged in the real world.

[[_TOC_]]

## Device/Transducer Index

Devices are assigned an index starting from 0 in the order they are connected.

Each device has 249 transducers arranged, and they are assigned local indices (refer to "AUTD Surface Photo" in [Getting Started/Hardware](../getting_started/hardware.md)).

## Geometry API

- `num_devices()`: Get the number of devices
- `num_transducers()`: Get the number of all transducers
- `center()`: Get the center of all transducers

Note that `Geometry` can be accessed directly from `Controller`.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/geometry_3.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/geometry_3.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/geometry_3.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/geometry_3.py}}
```
{{ #endtab }}
{{ #endtabs }}

### Getting a Device

`Geometry` is a container of `Device`, and `Device` is a container of `Transducer`.

To get a `Device`, use an indexer.
Alternatively, you can use an iterator.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/geometry_4.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/geometry_4.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/geometry_4.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/geometry_4.py}}
```
{{ #endtab }}
{{ #endtabs }}

## Device API

- `idx()`: Device index
- `rotation()`: Rotation of the device
- `x_direction()`: X-direction vector of the device
- `y_direction()`: Y-direction vector of the device
- `axial_direction()`: Axial direction vector of the device (direction the transducers face)

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/device_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/device_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/device_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/device_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

### Getting a Transducer

`Device` is a container of `Transducer`, and `Transducer` stores information about each transducer.

To get a `Transducer`, use an indexer.
Alternatively, you can use an iterator.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/device_1.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/device_1.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/device_1.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/device_1.py}}
```
{{ #endtab }}
{{ #endtabs }}

## Transducer API

The following information can be obtained.

- `idx()`: (Local) index of the transducer
- `dev_idx()`: Index of the device to which the transducer belongs
- `position()`: Position of the transducer

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/transducer_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/transducer_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/transducer_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/transducer_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

