# 出力マスク

> NOTE: firmware v12.1.0以降で使用可能

`OutputMask`を送信することで, `Gain`, `FociSTM`, `GainSTM`の`Intensity`値にかかわらず, 振動子毎に出力を止めることができる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/output_mask.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/output_mask.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/output_mask.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/output_mask.py}}
```
{{ #endtab }}
{{ #endtabs }}

`OutputMask`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> bool`で, `false`に設定した振動子の出力は無効化される.

なお, `OutputMask`は`Gain`, `FociSTM`, `GainSTM`の各`Segment`別に作用する.

特に指定しない限りは, `Segment::S0`が使用される.

マスクをかける`Segment`を変更する場合は, `with_segment`を使用する.
