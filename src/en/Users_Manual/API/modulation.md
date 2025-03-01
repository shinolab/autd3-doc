# Modulation

`Modulation` is a mechanism to control amplitude modulation.

Modulation data is multiplied by the sound pressure amplitude.
For example, when applying `Sine` modulation of $\SI{1}{kHz}$, the sound pressure amplitude will be as follows, and the envelope of the positive (or negative) part of the sound pressure amplitude will follow a $\SI{1}{kHz}$ sine wave.

<figure>
  <img src="../../fig/Users_Manual/sine_1k_mod.png"/>
</figure>

Currently, `Modulation` has the following limitations.

* The buffer size is up to 32768
  * 65536 when using extended mode
* The sampling rate is $\ufreq/N$. Here, $N$ is a 16-bit unsigned integer greater than 0.

The SDK provides several types of `Modulation` to generate AM by default.

* [Static](./modulation/static.md) - Without modulation
* [Sine](./modulation/sine.md) - Sine wave
  * [Fourier](./modulation/fourier.md) - Superposition of sine waves
* [Square](./modulation/square.md) - Square wave
* [Wav](./modulation/wav.md) - Modulation based on Wav file
* [Csv](./modulation/csv.md) - Modulation based on Csv file
* [Custom](./modulation/custom.md) - User-defined modulation
* [Cache](./modulation/cache.md) - Cache the calculation result of other `Modulation`
* [RadiationPressure](./modulation/radiation.md) - Apply modulation to radiation pressure instead of sound pressure
* [Fir](./modulation/fir.md) - Apply Fir filter

## Common API for Modulation

### Sampling Configuration

The sampling configuration of `Modulation` can be obtained with `sampling_config`.

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/modulation_prop.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation_prop.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation_prop.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation_prop.py}}
```
</div>

Additionally, some `Modulation` can optionally change the sampling configuration.

For more details on sampling configuration, refer to [About Sampling Configuration](./sampling_config.md).

### LoopBehavior

`Modulation` can control the behavior of loops.
The default is an infinite loop.

For more details, refer to [Segment/LoopBehavior](./segment.md).
