# サンプリング設定について

Modulation, FociSTM/GainSTMのサンプリング設定について説明する.

サンプリング周波数は$\ufreq/N$で, $N$は$0$より大きい16-bit符号なし整数である.

また, Silencerの設定によって指定できるサンプリング周波数の最大値が決まる.
詳しくは[Silencer](./silencer.md#fixed-completion-steps-mode)を参照.

サンプリング設定のコンストラクタには, 分周比$N$, または, サンプリング周波数, サンプリング周期を指定する.

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

## サンプリング周波数制限の緩和

**使用は推奨されないが**, 出力可能な周波数/周期の内で最も指定した値に近い周波数/周期を使用する方法もある.

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