# 位相補正

`PhaseCorrection`により, 位相を補正することができる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/phase_corr.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/phase_corr.py}}
```
{{ #endtab }}
{{ #endtabs }}

`PhaseCorrection`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Phase`で, 振動子毎に指定した位相値が`Gain`, `FociSTM`, `GainSTM`の値に加算されるようになる.
