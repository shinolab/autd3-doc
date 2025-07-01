# Environment

`Environment`はAUTD3デバイスがおかれている現実世界の環境を表す.

`Environment`には`Controller`の`environment`メンバからアクセスできる.

## EnvironmentのAPI

- `sound_speed`: 音速の取得/設定. 単位はmm/s. **位相計算などに使用されるため, 可能な限り現実に即した値を設定することをおすすめする**. デフォルトの音速は$340\times 10^{3}\,\mathrm{mm/s}$となっており, これは, およそ摂氏15度での空気の音速に相当する.
- `set_sound_speed_from_temp(temp)`: 温度`temp` [℃]から音速を設定.
- `wavelength()`: 超音波の波長
- `wavenumber()`: 超音波の波数

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../codes/Users_Manual/environment.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/environment.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/environment.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/environment.py}}
```
{{ #endtab }}
{{ #endtabs }}
