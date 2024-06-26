# Custom

`Custom`は指定された符号なし8bitデータ列を出力する`Modulation`である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/custom.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/custom.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/custom.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/custom.py}}
```

コンストラクタの第2引数で, このデータのサンプリング設定を指定する必要がある.

> NOTE: AUTD3のサンプリング周波数に関する制約により, 出力できない可能性があるので注意されたい.
> Modulationのサンプリング周波数の設定と制約は[Modulation](../modulation.md)を参照されたい.
