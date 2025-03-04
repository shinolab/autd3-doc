# Multiple Devices

AUTD3 can connect multiple devices in a daisy-chain to form a large array.
The SDK is designed to be used transparently even when multiple devices are connected.

When using multiple devices with the SDK, specify the `AUTD3` structure for each connected device in order in the first argument of the `Controller::open` function.
Refer to [Getting Started/Hardware](../getting_started/hardware.md) for hardware connection methods.

Below are the steps for connecting two devices.

[[_TOC_]]

## Translation Only

<figure>
  <img src="../../fig/Users_Manual/hor_left_ori_left_1.png"/>
</figure>

For example, if the devices are arranged and connected as shown above, with the device on the left being the first and the device on the right being the second, and the global coordinates are taken to be the same as the local coordinates of the first device, the code is as follows.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

Here, `pos` represents the position of the device in global coordinates.
Note that `AUTD3::DEVICE_WIDTH` is the width of the device (including the outer shape of the board).

## Setting Global Coordinates

The origin and orientation of the global coordinates used by the SDK can be freely set by the user.

<figure>
  <img src="../../fig/Users_Manual/hor_right_ori_left_1.png"/>
</figure>

For example, if the global coordinates are taken to be the same as the local coordinates of the second device, the code is as follows.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.py}}
```
{{ #endtab }}
{{ #endtabs }}

## Translation and Rotation

To specify the rotation of the device, use `rot`.
Rotation can be specified using Euler angles or quaternions.

<figure>
  <img src="../../fig/Users_Manual/vert.png"/>
</figure>

For example, if the devices are arranged as shown above, with the bottom being the first device and the left being the second device, and the global coordinates are taken to be the same as the local coordinates of the first device, the code is as follows.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: Only the Rust version supports all 12 types of Euler angles.
> Other languages support only XYZ and ZYZ.
