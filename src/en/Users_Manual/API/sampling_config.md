# About Sampling Configuration

This section explains the sampling configuration for Modulation and FociSTM/GainSTM.

The sampling frequency is $\ufreq/N$, where $N$ is a 16-bit unsigned integer greater than 0.

Additionally, the maximum sampling frequency that can be specified is determined by the Silencer settings.
For more details, refer to [Silencer](./silencer.md#fixed-completion-steps-mode).

The constructor for the sampling configuration can specify the division ratio $N$, the sampling frequency, or the sampling period.

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.py}}
```
</div>

## Relaxation of Sampling Frequency Limits

**Not recommended for use**, but there is a method to use the frequency/period closest to the specified value within the possible output frequencies/periods.

<div class="tabs">
<input id="rust_tab_nearest" type="radio" class="tab" name="tab_nearest" checked>
<label class="tab_item" n=4 for="rust_tab_nearest">Rust</label>
<input id="cpp_tab_nearest" type="radio" class="tab" name="tab_nearest">
<label class="tab_item" n=4 for="cpp_tab_nearest">C++</label>
<input id="cs_tab_nearest" type="radio" class="tab" name="tab_nearest">
<label class="tab_item" n=4 for="cs_tab_nearest">C#</label>
<input id="python_tab_nearest" type="radio" class="tab" name="tab_nearest">
<label class="tab_item" n=4 for="python_tab_nearest">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cs}}
```

```python
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.py}}
```
</div>