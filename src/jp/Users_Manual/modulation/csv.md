# Csv

`Csv`はCsvファイルをもとに構成される`Modulation`である.

## Install

### Rust

```shell
cargo add autd3-modulation-audio-file@29.0.0-rc.12
```

### C++ (CMake)

```ignore,filename=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::modulation::audio_file)
```

### C#/Unity/Python

メインライブラリに含まれている.

## APIs

第1引数にデータファイルへのパスを指定する.
データファイルはdeliminator (デフォルトはカンマ",". `with_deliminator`で変更可.) で区切られた行データか, 列データであり, データ値は符号なし8bit整数である必要がある.
また, 第2引数には, サンプリング周波数を指定する.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/csv_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/csv_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/csv_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/csv_0.py}}
```

## リサンプリング

[サンプリング周波数に関する制約](../modulation.md)により, 指定されたサンプリング周波数では出力できない可能性がある.
そのため, リサンプリング機能が提供されている.
リサンプリングする場合は, 以下のようにする.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/csv_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/csv_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/csv_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/csv_1.py}}
```

第2引数にもとのサンプリング設定を指定する.
第3引数に目標サンプリング設定を指定する.
第4引数には, リサンプリングの方法を指定する.
現在は, `SincInterpolation`のみが実装されている.
`SincInterpolation`では, 窓関数を指定できる.
現在は, 窓関数として, `Rectangular`と`BlackMan`のみが用意されている.
窓関数では, 窓関数の幅を指定できる.
