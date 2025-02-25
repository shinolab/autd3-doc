# 振幅とパルス幅

PWM信号のDuty比と超音波出力の間には非線形な関係がある. 
この関係を補正するために, `PulseWidthEncoder`を使用できる.

ファームウェア内部には, `Gain`/`FociSTM`/`GainSTM`の強度データの値 ($0$--$255$) とModulationの振幅データ ($0$--$255$) をかけ合わせたものを$255$で割った値 ($0$--$255$) をインデックスにして, PWM信号のパルス幅 ($0$--$255$) を決定するテーブルがある.
`PulseWidthEncoder`によってこのテーブルを変更できる.
なお, PWM信号の周期は256である.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.py}}
```

コンストラクタの引数は各デバイスに対して, テーブルのインデックスを引数にパルス幅を返す関数を返す関数`Fn(&Device) -> Fn(EmitIntensity) -> u8`である.

デフォルトでは,
$$
    \text{table}(i) = \left[\sin^{-1}\left(\frac{i}{255}\right) \times \frac{256}{\pi}\right]
$$
となるテーブルが書き込まれている.
ここで$[\cdot]$は最も近い整数を表す.
