# Gainの自作

Rust版のライブラリでは自前の`Gain`を作成することができる.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.
> しかし, 同様の目的で, [Custom](../API/gain/custom.md)を使用することができる.

ここでは, `Focus`と同じように単一焦点を生成する`FocalPoint`を実際に定義してみることにする.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.rs}}
```

`Gain::init`は各デバイス毎に, `GainCalculator` (を実装した型) を生成する`GainContextGenerator` (を実装した型) を返す.
実際の位相, 振幅の計算は`GainCalculator::calc`関数内で行う.
