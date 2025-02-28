# Segment/LoopBehavior

## Segment

`Modulation`, `Gain`, `FociSTM`, `GainSTM`のデータ領域にはそれぞれ, `Segment`が2つ用意されている.

特に指定しない限りは, `Segment::S0`が使用される.

データを書き込む`Segment`は, `WithSegment`で指定する.

<div class="tabs">
<input id="rust_tab_segment" type="radio" class="tab" name="tab_segment" checked>
<label class="tab_item" n=4 for="rust_tab_segment">Rust</label>
<input id="cpp_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="cpp_tab_segment">C++</label>
<input id="cs_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="cs_tab_segment">C#</label>
<input id="python_tab_segment" type="radio" class="tab" name="tab_segment">
<label class="tab_item" n=4 for="python_tab_segment">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_transition.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/segment_transition.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/segment_transition.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/segment_transition.py}}
```
</div>

`transition_mode`には, `Segment`の切り替え条件を指定する.
- 遷移先セグメントが無限ループ時にのみ使用可能
    - `Immediate` : 直ちに切り替える
    - `Ext`       : 直ちに切り替え, 拡張モードにする (各`Segment`のデータを出力後, 自動で`Segment`を切り替えるモード)

- 遷移先セグメントが有限ループ時にのみ使用可能
    - `SyncIdx`               : 遷移先の`Segment`のデータインデックスが$0$になったときに切り替える
    - `SysTime(DcSysTime)`    : 指定した時刻になったときに切り替える
    - `GPIO(GPIOIn)`          : 指定したGPIOピンに信号が入力されたときに切り替える

> NOTE: `Gain`は`Immediate`のみサポートしている.

> 遷移先のループの挙動を指定する場合は, [`LoopBehavior`](#loopbehavior)を参照されたい.

データの書き込みのみを行い, `Segment`を切り替えたくない場合は`transition_mode`に`None`を指定する.

### Segmentの切り替え

`Segment`を切り替えたいだけの場合は, `SwapSegment`を使用する.

<div class="tabs">
<input id="rust_tab_swap" type="radio" class="tab" name="tab_swap" checked>
<label class="tab_item" n=4 for="rust_tab_swap">Rust</label>
<input id="cpp_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="cpp_tab_swap">C++</label>
<input id="cs_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="cs_tab_swap">C#</label>
<input id="python_tab_swap" type="radio" class="tab" name="tab_swap">
<label class="tab_item" n=4 for="python_tab_swap">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.py}}
```
</div>

### LoopBehavior

`Modulation`と`FociSTM`, `GainSTM`は`WithLoopBehavior`でループの挙動を制御できる.

<div class="tabs">
<input id="rust_tab_loop" type="radio" class="tab" name="tab_loop" checked>
<label class="tab_item" n=4 for="rust_tab_loop">Rust</label>
<input id="cpp_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="cpp_tab_loop">C++</label>
<input id="cs_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="cs_tab_loop">C#</label>
<input id="python_tab_loop" type="radio" class="tab" name="tab_loop">
<label class="tab_item" n=4 for="python_tab_loop">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/loop_behavior.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cs}}
```

```python
{{#include ../../../codes/Users_Manual/segment/loop_behavior.py}}
```
</div>
