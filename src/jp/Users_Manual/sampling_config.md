# サンプリング設定について

Modulation, FociSTM/GainSTMのサンプリング設定について説明する.

サンプリング周波数は$\ufreq/N$で, $N$は$0$より大きい16-bit符号なし整数である.

また, Silencerの設定によって指定できるサンプリング周波数の最大値が決まる.
詳しくは[Silencer](./silencer.md#fixed-completion-steps-mode)を参照.

## サンプリング周波数/周期の設定

サンプリング周波数, または, サンプリング周期を設定する場合は, 周波数, 周期をそのまま指定すれば良い.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.py}}
```

## サンプリング周波数分周比の設定

サンプリング周波数分周比$N$を設定する場合は以下のようにする.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.py}}
```

## サンプリング周波数制限の緩和

**使用は推奨されないが**, 出力可能な周波数/周期の内で最も指定した値に近い周波数/周期を使用する方法もある.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.py}}
```
