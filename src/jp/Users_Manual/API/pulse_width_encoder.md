# 強度とパルス幅

PWM信号のDuty比と超音波出力の間には非線形な関係がある. 
この関係を補正するために, `PulseWidthEncoder`を使用できる.

ファームウェア内部には, `Gain`/`FociSTM`/`GainSTM`の強度 (`EmitIntensity`) 値 ($0$--$255$) とModulationの振幅データ ($0$--$255$) をかけ合わせたものを$255$で割った強度値 ($0$--$255$) をインデックスにして, PWM信号のパルス幅 ($0$--$511$) を決定するテーブルがある.
`PulseWidthEncoder`を送信することで, このテーブルを変更できる.
なお, PWM信号の周期は512である.

デフォルトでは, 強度値と超音波の出力が (理論上) 線形になるように,
$$
    \text{table}(i) = \left[\sin^{-1}\left(\frac{i}{255}\right) \times \frac{512}{\pi}\right]
$$
となるテーブルが書き込まれている.
ここで$[\cdot]$は最も近い整数を表す.

例えば, 以下のようにすると, 強度値とパルス幅の関係が線形になる (すなわち, 強度値と超音波出力は非線形になる).

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.py}}
```
{{ #endtab }}
{{ #endtabs }}

コンストラクタの引数は各デバイスに対して, テーブルのインデックスを引数にパルス幅を返す関数を返す関数`Fn(&Device) -> Fn(EmitIntensity) -> PulseWidth`である.
