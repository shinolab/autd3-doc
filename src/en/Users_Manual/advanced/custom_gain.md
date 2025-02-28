# Creating Custom Gain

In the Rust library, you can create your own `Gain`.

> NOTE: This feature is not available in the C++, C#, and Python libraries.
> However, you can use [Custom](../gain/custom.md) for the same purpose.

Here, let's actually define a `FocalPoint` that generates a single focal point like `Focus`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.rs}}
```

`Gain::init` returns a (struct that implements) `GainContextGenerator` that generates a (struct that implements) `GainCalculator` for each device.
The actual phase and intensity calculations are performed in the `GainCalculator::calc` function.
