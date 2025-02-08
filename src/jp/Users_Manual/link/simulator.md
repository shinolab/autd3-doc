# Simulator

Simulator linkは[AUTDシミュレータ](../Simulator/simulator.md)を使用する際に使うLinkである.

このlinkの使用の前に, AUTDシミュレータを起動しておく必要がある.

[[_TOC_]]

## Simulatorリンク

### Install

#### Rust

```shell
cargo add autd3-link-simulator@29.0.0-rc.20
```

#### C++ (CMake)

```ignore,filename=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::simulator)
```

#### C#/Unity/Python

メインライブラリに含まれている.

### APIs

`Simulator`のコンストラクタにはAUTDシミュレータのIPアドレスとポート番号を指定する.

```rust,should_panic,edition2021
{{#include ../../../codes/Users_Manual/link/simulator_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/simulator_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/simulator_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/simulator_0.py}}
```
