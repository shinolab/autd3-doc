# GainSTM

`GainSTM` can handle arbitrary `Gain`s, unlike `FociSTM`.
However, the number of `Gain`s that can be used is 1024.

The following is an example of how to use `GainSTM`.
This is a sample that rotates the focus on a circle with a radius of $\SI{30}{mm}$ centered on a point $\SI{150}{mm}$ directly above the center of the array.

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm/gain_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm/gain_0.cpp}}

```

```cs
{{#include ../../../codes/Users_Manual/stm/gain_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm/gain_0.py}}
```

## Specify the sampling configuration

You can also specify the sampling frequency instead of frequency.

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm/gain_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm/gain_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm/gain_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm/gain_1.py}}
```

## GainSTMMode

`GainSTM` sends all phase/amplitude data, so it has a large latency[^fn_gain_seq].
To solve this problem, `GainSTM` has `PhaseFull` mode that sends only phase and reduces the transmission time by half[^phase_half].

This mode can be switched with `with_mode`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm/gain_2.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm/gain_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm/gain_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm/gain_2.py}}
```

The default is `PhaseIntensityFull` mode, which sends all information.

[^fn_gain_seq]: About 75 times of `FociSTM<1>`

[^phase_half]: Legacy mode only
