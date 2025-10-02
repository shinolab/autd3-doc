# Segment/FiniteLoop

## Segment

`Modulation`, `Gain`, `FociSTM`, `GainSTM`のデータ領域にはそれぞれ, `Segment`が2つ用意されている.

特に指定しない限りは, `Segment::S0`が使用される.

データを書き込む`Segment`を変更する場合は, `WithSegment`を送信する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_transition.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/segment_transition.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/segment_transition.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/segment_transition.py}}
```
{{ #endtab }}
{{ #endtabs }}

`transition_mode`には, `Segment`の切り替え条件を指定する.
- 遷移先セグメントが無限ループ時にのみ使用可能
    - `Immediate` : 直ちに切り替える
    - `Ext`       : 直ちに切り替え, 拡張モードにする (各`Segment`のデータを出力後, 自動で`Segment`を切り替えるモード)

- 遷移先セグメントが有限ループ時にのみ使用可能
    - `SyncIdx`               : 遷移先の`Segment`のデータインデックスが$0$になったときに切り替える
    - `SysTime(DcSysTime)`    : 指定した時刻になったときに切り替える
    - `GPIO(GPIOIn)`          : 指定したGPIOピンに信号が入力されたときに切り替える

> NOTE: `Gain`は`Immediate`のみサポートしている.

> 遷移先のループの挙動を指定する場合は, [`FiniteLoop`](#finiteloop)を参照されたい.

データの書き込みのみを行い, `Segment`を切り替えたくない場合は`transition_mode`に`Later`を指定する.

### Segmentの切り替え

`Segment`を切り替えたいだけの場合は, `SwapSegment`を送信する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/segment_change_transition.py}}
```
{{ #endtab }}
{{ #endtabs }}

### FiniteLoop

`Modulation`と`FociSTM`, `GainSTM`は`WithFiniteLoop`を送信することでループの挙動を制御できる.

**ループ挙動の指定は, セグメントを切り替えたときにのみ有効であることに注意.**

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/segment/loop_behavior.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/segment/loop_behavior.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/segment/loop_behavior.py}}
```
{{ #endtab }}
{{ #endtabs }}
