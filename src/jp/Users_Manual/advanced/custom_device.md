# Deviceの自作

Rust版のライブラリではAUTD3以外の`Device`を使用することができる.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.

> NOTE: 実際にはAUTD3以外のデバイスは存在しないので, [Emulator](../Emulator/emulator.md)くらいでしか使用することはできない. ([Simulator](../Simulator/simulator.md)は未対応.)

ここでは, 振動子の間隔を変えられる`CustomDevice`を実際に定義してみることにする.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/custom_device.rs}}
```

`Device`は以下の制約を満たす必要がある.
- 振動子の数は最大で256個
- 振動子はすべて同一方向を向いている (`Device::new`の第2引数がすべての振動子の回転を表す)
