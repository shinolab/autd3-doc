# Creating Custom Modulation

In the Rust version, you can create your own `Modulation`.
Here, let's create a `Burst` that outputs only at a certain moment during the period[^fn_burst].

> NOTE: This feature is not available in the C++, C#, and Python libraries.
> However, you can use [Custom](../API/modulation/custom.md) for the same purpose.

Below is a sample of this `Burst`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/custom_modulation_0.rs}}
```

[^fn_burst]: Not included in the SDK.
