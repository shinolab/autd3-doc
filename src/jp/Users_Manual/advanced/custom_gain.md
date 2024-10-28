# Gainの自作

Rust版のライブラリでは自前の`Gain`を作成することができる.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.
> しかし, 同様の目的で, [Custom](../gain/custom.md)を使用することができる.

ここでは, `Focus`と同じように単一焦点を生成する`FocalPoint`を実際に定義してみることにする.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.rs}}
```

`Controller::send`関数は`Gain`型を継承したクラスを引数に取ることができる.
`Gain`型は`Geometry`とfilter (後述) を引数に取り, 各デバイス毎に`GainContext`を生成する`GainContextGenerator`を返す.
実際の位相, 振幅の計算は`GainContext::calc`関数内で行う.

なお, filterは[Group](../gain/grouped.md)で使用される, 各デバイス毎に各振動子が有効か否かを表すデータである.
