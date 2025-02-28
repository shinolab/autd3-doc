# Spatio-Temporal Modulation/時空間変調

SDKでは, 音場を周期的に切り替えるための機能 (Spatio-Temporal Modulation, STM) が用意されている.
SDKには単一焦点音場から8焦点音場までをサポートする`FociSTM`と, 任意の`Gain`をサポートする`GainSTM`が用意されている.
`FociSTM`と`GainSTM`はAUTD3ハードウェア上のタイマを使用するので時間精度が高いが, 制約も多い.

- [FociSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## FociSTM/GainSTMの共通API

### サンプリング設定の取得

`sampling_config`でサンプリング設定を取得できる.

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_prop.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm_prop.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm_prop.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm_prop.py}}
```
</div>

### LoopBehavior

`FociSTM`/`GainSTM`では, ループの挙動を制御できる.
デフォルトは無限ループである.

詳細は[Segment/LoopBehavior](./segment.md)を参照.

### ユーティリティ

Rust版のみ直線と円の軌跡を生成するユーティリティが用意されている.


<div class="tabs">
<input id="rust_tab_util" type="radio" class="tab" name="tab_util" checked>
<label class="tab_item" n=1 for="rust_tab_util">Rust</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/stm_utils.rs}}
```
</div>
