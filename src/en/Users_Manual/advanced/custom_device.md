# Creating Custom Device

In the Rust library, you can use `Device` other than AUTD3.

> NOTE: This feature is not available in the C++, C#, and Python libraries.

> NOTE: In reality, there are no devices other than AUTD3, so it can only be used with [Emulator](../Emulator/emulator.md) (Simulator is not supported).

Here, let's actually define a `CustomDevice` that can change the spacing of the transducers.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/custom_device.rs}}
```

`Device` must meet the following constraints.
- The number of transducers is up to 256
- All transducers face the same direction (the second argument of `Device::new` represents the rotation of all transducers)
