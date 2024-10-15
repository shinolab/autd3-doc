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

## リサンプリング

[サンプリング周波数に関する制約](../modulation.md)により, 指定されたサンプリング周波数では出力できない可能性がある.
そのため, リサンプリング機能が提供されている.
詳しくは, [Csv](csv.md##リサンプリング)を参照されたい.
