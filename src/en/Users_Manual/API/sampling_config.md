# About Sampling Configuration

This section explains the sampling configuration for Modulation and FociSTM/GainSTM.

The sampling frequency is $\ufreq/N$, where $N$ is a 16-bit unsigned integer greater than 0.

Additionally, the maximum sampling frequency that can be specified is determined by the Silencer settings.
For more details, refer to [Silencer](./silencer.md#fixed-completion-steps-mode).

The constructor for the sampling configuration can specify the division ratio $N$, the sampling frequency, or the sampling period.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/sampling_config/modulation_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

## Relaxation of Sampling Frequency Limits

**Not recommended for use**, but there is a method to use the frequency/period closest to the specified value within the possible output frequencies/periods.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.py}}
```
{{ #endtab }}
{{ #endtabs }}