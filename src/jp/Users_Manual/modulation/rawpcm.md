# RawPCM

## Install

### Rust

```shell
cargo add autd3-modulation-audio-file@29.0.0-rc.19
```

### C++ (CMake)

```ignore,filename=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::modulation::audio_file)
```

### C#/Unity/Python

メインライブラリに含まれている.

## APIs

`RawPCM`はraw pcmファイルをもとに構成される`Modulation`である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.py}}
```

コンストラクタの第2引数で, このデータのサンプリング設定を指定する必要がある.

## リサンプリング

[サンプリング周波数に関する制約](../modulation.md)により, 指定されたサンプリング周波数では出力できない可能性がある.
そのため, リサンプリング機能が提供されている.
詳しくは, [Csv](csv.md##リサンプリング)を参照されたい.
