# 出力音圧の制御

AUTD3では, 出力する音圧を[PWM](./../../Theory/pwm.md)を使用して制御している.
具体的には, Duty比$D$と出力音圧$P$の関係は理論上以下のように表される.
$$
P \propto \sin\left(D\pi\right).
$$

`Focus`などの`Gain`には出力強度を$\SI{8}{bit}$で制御する`intensity`パラメータがある.
例えば, 以下のコードでは, この強度を最大値の約半分に設定している.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/intensity/focus.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/intensity/focus.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/intensity/focus.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/intensity/focus.py}}
```
{{ #endtab }}
{{ #endtabs }}

デフォルトでは, この`intensity`パラメータと出力音圧$P$が理論上は線形に比例するように設定されている.
具体的には, 強度パラメータ$I$ ($\SI{8}{bit}$) からDuty比$D$が以下のように計算されるように設定されている.
$$
D = \frac{\arcsin\left(\frac{I}{255}\right)}{\pi}.\\
\left(\therefore P \propto \sin\left(\arcsin\left(\frac{I}{255}\right)\right) = \frac{I}{255}\right)
$$

しかし, 実際には振動子の個体差や理論値とのズレによって, 必ずしも線形に比例するとは限らないことに注意が必要である.
(ただし, その場合でも強度パラメータと音圧の関係が単調増加であることは仮定して良い.)
[AUTD3ではそのため, この強度パラメータとDuty比$D$の変換式を変更し, ユーザが補正することができるようにしている](../API/pulse_width_encoder.md).

> NOTE: なお, 実際の強度パラメータとしては, `Gain`等で指定する強度パラメータに`Modulation`による変調データ($\SI{8}{bit}$)をかけ合わせ$255$で割った値が使用される.
