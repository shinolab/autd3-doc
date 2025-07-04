# GPIOOutputs

`GPIOOutputs`を送信することで, GPIOピンの出力を各デバイス・ピン毎に設定できる.

<figure>
    <img src="../../fig/Users_Manual/gpio_pin.jpg"/>
    <figcaption>GPIOピン</figcaption>
</figure>

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/gpio_out.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/advanced/gpio_out.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/advanced/gpio_out.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/advanced/gpio_out.py}}
```
{{ #endtab }}
{{ #endtabs }}

出力可能なデータは以下の通り.
- `BaseSignal`: 基準信号 (超音波と同じ周波数のDuty比50%矩形波)
- `Thermo`: 温度センサーがアサートされているかどうか
- `ForceFan`: ForceFanフラグがアサートされているかどうか
- `Sync`: EtherCAT同期信号
- `ModSegment`: Modulationのセグメント
- `ModIdx(u16)`: Modulationのインデックスが指定した値のときにHighになる
- `StmSegment`: STMのセグメント
- `StmIdx(u16)`: STMのインデックスが指定した値のときにHighになる
- `IsStmMode`: FociSTM/GainSTMが使用されているかどうか
- `PwmOut(&Transducer)`: 指定した振動子のPWM出力
- `SysTimeEq(DcSysTime)`: 指定したシステム時間の間Highになる
- `SyncDiff`: システム時間の補正中にHighになる
- `Direct(bool)`: 指定した値を出力する
