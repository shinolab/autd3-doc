# Spatio-Temporal Modulation/時空間変調

SDKでは, 音場を周期的に切り替えるための機能 (Spatio-Temporal Modulation, STM) が用意されている.
SDKには単一焦点音場から8焦点音場までをサポートする`FociSTM`と, 任意の`Gain`をサポートする`GainSTM`が用意されている.
`FociSTM`と`GainSTM`はAUTD3ハードウェア上のタイマを使用するので時間精度が高いが, 制約も多い.

- [FociSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## FociSTM/GainSTMの共通API

### 周波数/周期/サンプリング設定の取得

`freq`, `period`, `sampling_config`でそれぞれ周波数, 周期, サンプリング設定を取得できる.

```rust,edition2021
{{#include ../../codes/Users_Manual/stm_prop.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/stm_prop.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/stm_prop.cs}}
```

```python
{{#include ../../codes/Users_Manual/stm_prop.py}}
```

### LoopBehavior

ループの挙動を, [Modulation](./modulation.md#loopbehavior)と同様に`with_loop_behavior`で制御できる.
有限回ループするか, 無限ループするかを指定できる.

デフォルトは無限ループである.

無限ループの場合, どのインデックスデータから再生されるかは制御できない.
有限回ループの場合, 0番目のデータから再生が始まり, 指定回数のループの後, 最終インデックスデータが出力され続ける.

**この設定は, Segmentを切り替えたときにしか効果がない. 詳しくは[Segment](./segment.md)を参照.**

### ユーティリティ

Rust版のみ直線と円の軌跡を生成するユーティリティが用意されている.

```rust,edition2021
{{#include ../../codes/Users_Manual/stm_utils.rs}}
```