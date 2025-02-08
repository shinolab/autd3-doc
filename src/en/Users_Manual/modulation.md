# Modulation

`Modulation` is a mechanism to control AM modulation.

The modulation is applied to the amplitude of the sound pressure.
For example, if you use `Sine` with $\SI{1}{kHz}$, the sound pressure amplitude is as follows, and the envelope of the positive part (or negative part) of sound pressure follows the $\SI{1}{kHz}$ sine wave.

<figure>
  <img src="../fig/Users_Manual/sine_1k_mod.png"/>
</figure>

Currently, `Modulation` has the following restrictions.

- The buffer size is up to 32768.
- The sampling rate is $\ufreq/N$, where $N$ is a non-zero 16-bit unsigned integer.

The SDK has `Modulation` by default to generate several types of AM.

* [Static](./modulation/static.md)
* [Sine](./modulation/sine.md)
  * [Fourier](./modulation/fourier.md)
* [Square](./modulation/square.md)
* [Wav](./modulation/wav.md)
* [Cache](./modulation/cache.md)
* [RadiationPressure](./modulation/radiation.md)
* [Transform](./modulation/transform.md)

## Modulation common API

### Sampling configuration

You can get the sampling frequency with `sampling_config`.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_prop.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_prop.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_prop.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_prop.py}}
```

Some `Modulation` can set the sampling configuration with `with_sampling_config`.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_0.py}}
```
