# 位相補正

`PhaseCorrection`により, 位相を補正することができる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/phase_corr.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/phase_corr.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/phase_corr.py}}
```

`PhaseCorrection`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Phase`で, 振動子毎に指定した位相値が`Gain`, `FociSTM`, `GainSTM`の値に加算されるようになる.
