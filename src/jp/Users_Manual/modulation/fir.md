# Fir

`with_fir`にて, FIRフィルタを適用することができる.

以下は, サンプリング周波数$\SI{20}{kHz}$, タップ数$199$, カットオフ周波数$\SI{200}{Hz}$のFIRフィルタを適用する例である. 

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/fir.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/fir.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/fir.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/fir.py}}
```
