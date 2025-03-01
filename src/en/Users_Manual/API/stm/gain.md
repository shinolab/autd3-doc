# GainSTM

`GainSTM` is different from `FociSTM` in that it can handle arbitrary `Gain`.
However, the number of `Gain` that can be used is $1024$ (in extended mode $2048$).

The usage of `GainSTM` is as follows.
This is a sample that rotates a focus on the circumference of a circle with a radius of $\SI{30}{mm}$ centered at a point $\SI{150}{mm}$ directly above the center of the array.
The circumference is sampled at 200 points, rotating at $\SI{1}{Hz}$. (That is, the sampling frequency is $\SI{200}{Hz}$.)

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
{{#include ../../../../codes/Users_Manual/stm/gain_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/stm/gain_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/stm/gain_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/stm/gain_0.py}}
```
</div>

## GainSTMMode

`GainSTM` sends all phase/intensity data, resulting in high latency[^fn_gain_seq].
To address this issue, `GainSTM` has a `PhaseFull` mode that sends only the phase, reducing the transmission time by half, and a `PhaseHalf` mode that compresses the phase to 4 bits, reducing the transmission time to a quarter.
In these two modes, the maximum intensity is used regardless of the intensity setting of `Gain`.

The default mode is `PhaseIntensityFull`, which sends both intensity and phase data.

[^fn_gain_seq]: Approximately 75 times the latency of `FociSTM<1>`
