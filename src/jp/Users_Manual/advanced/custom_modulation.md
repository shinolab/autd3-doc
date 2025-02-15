# Modulationの自作

Rust版では`Modulation`も独自のものを作成することができる.
ここでは, 周期中のある一瞬だけ出力する`Burst`を作ってみる[^fn_burst].

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.
> しかし, 同様の目的で, [Custom](../modulation/custom.md)を使用することができる.

以下が, この`Burst`のサンプルである.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/custom_modulation_0.rs}}
```

[^fn_burst]: SDKにはない.
