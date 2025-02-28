# サンプリング設定について

Modulation, FociSTM/GainSTMのサンプリング設定について説明する.

サンプリング周波数は$\ufreq/N$で, $N$は$0$より大きい16-bit符号なし整数である.

また, Silencerの設定によって指定できるサンプリング周波数の最大値が決まる.
詳しくは[Silencer](./silencer.md#fixed-completion-steps-mode)を参照.

サンプリング設定のコンストラクタには, 分周比$N$, または, サンプリング周波数, サンプリング周期を指定する.

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

## サンプリング周波数制限の緩和

**使用は推奨されないが**, 出力可能な周波数/周期の内で最も指定した値に近い周波数/周期を使用する方法もある.

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