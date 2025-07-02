# Segmentの使用

[焦点の移動](./move_focus.md)で説明したように, autd3において, `Gain`等は送信するたびに上書きされ, この書き込みはバッファリングされたりはしない.
そのため, (特に`Gain`→`FociSTM`への切替時などに) 意図しない中間データが出力されてしまうことがある.
これを防ぐために, AUTD3では, `Gain/GainSTM/FociSTM`や`Modulation`は2つのメモリ領域 (`Segment`と呼ぶ) を持っており手動で[ダブルバッファリング](https://en.wikipedia.org/wiki/Multiple_buffering)のような制御を行うことができる.

`WithSegment`でデータを包むことで, 書き込む`Segment`を変更することができる.
(デフォルトでは`Segment::S0`に書き込まれる.)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/segment/segment.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/segment/segment.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/segment/segment.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/segment/segment.py}}
```
{{ #endtab }}
{{ #endtabs }}

ここで, `TransitionMode::Immediate`はデータの書き込み後, 直ちに`Segment`を切り替えることを意味する.

`transition_mode`に`None`を指定すると, データの書き込みだけを行い`Segment`の切り替えは行われない.
この場合は, 後に`SwapSegment`を送信することで, `Segment`を切り替えることができる.
詳細は, [`API/Segment`](../API/segment.md)を参照されたい.

> NOTE: なお, `Gain`, `GainSTM`, `FociSTM`はメモリ領域を共有している. 例えば, `Gain`のデータを書き込んだあと, `GainSTM`のデータを書き込むと, `Gain`のデータは上書きされる.