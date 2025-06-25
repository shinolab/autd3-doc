# Gain

AUTD can individually control the phase/amplitude of each transducer, allowing it to generate various sound fields.
`Gain` is the structs that manages this, and the SDK provides several types of `Gain` to generate different sound fields by default.

- [Null](./gain/null.md) ‐ No output
- [Focus](./gain/focus.md) - Single focus
- [Bessel](./gain/bessel.md) - Bessel beam
- [Plane](./gain/plane.md) - Plane wave
- [Uniform](./gain/uniform.md) - Drive all transducers with the same phase/amplitude
- [Custom](./gain/custom.md) - User can freely specify phase/amplitude
- [GainGroup](./gain/grouped.md) - Group transducers and apply different `Gain` to each group
- [Holo](./gain/holo.md) - Multi-focus sound field
