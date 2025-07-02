# FociSTM

- 使用可能な最大焦点数は$65536$
  - 拡張モードの場合は$131072$
- サンプリングレートは$\ufreq/N$で, $N$は0より大きい16-bit符号なし整数である

`FociSTM`の使用方法は以下のようになる.
これは, アレイの中心から直上$\SI{150}{mm}$の点を中心とした半径$\SI{30}{mm}$の円周上で焦点を回すサンプルである.
円周上を200点サンプリングし, 一周を$\SI{1}{Hz}$で回るようにしている. (すなわち, サンプリング周波数は$\SI{200}{Hz}$である.)


{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/focus_stm.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/stm/focus_stm.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/stm/focus_stm.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/stm/focus_stm.py}}
```
{{ #endtab }}
{{ #endtabs }}

`config`には周波数のほか, 周期やサンプリング設定を指定することができる.

サンプリング点数とサンプリング周期に関する制約によって, 指定した周波数で出力できない可能性がある.
例えば, 上記の例は200点を$\SI{1}{Hz}$で回すため, サンプリング周波数は$\SI{200}{Hz}=\ufreq/200$とすれば良い.
しかし, 例えば`point_num=199`にすると, サンプリング周波数を$\SI{199}{Hz}$にしなければならないが, $\SI{199}{Hz}=\ufreq/N$を満たすような整数$N$は存在せずエラーになる.

`FociSTM::into_nearest`を使用すると, 最も近い$N$が選択されるようになるが, 指定した周波数と実際の周波数がずれる可能性があるため注意が必要である.

## 多焦点

`FociSTM`では最大8焦点を同時に出すことができる.

以下は2焦点の例である.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/foci_1.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/stm/foci_1.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/stm/foci_1.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/stm/foci_1.py}}
```
{{ #endtab }}
{{ #endtabs }}

`FociSTM`の多焦点音場は単純な単焦点音場の重ね合わせである.
すなわち, 振動子の位置$x_\text{t}$, 各焦点位置$x_i$, 超音波周波数$f$, 音速$c$に対して, 以下の計算により位相$\theta$を求めている.
$$
\theta = \angle \sum_i \mathrm{e}^{2\pi\mathrm{j}\frac{f}{c}\|x_i-x_\text{t}\| + \mathrm{j}\phi_i}
$$
ここで, $\phi_i$は各焦点の位相オフセットである.
振幅に関しては, $\displaystyle \left\|\sum_i\mathrm{e}^{2\pi\mathrm{j}\frac{f}{c}\|x_i-x_\text{t}\| + \mathrm{j}\phi_i}\right\|$ **ではなく**, ソフトウェアからの指定値を使用する.

## 制約

データ量を削減するため, `FociSTM`では, 焦点位置座標を$\SI{0.025}{mm}$を単位とする$\SI{18}{bit}$符号あり固定小数点数にエンコードして使用する.
そのため, 各軸方向に対して, すべての振動子から$[\SI{-3276.8}{mm}, \SI{3276.775}{mm}]$の範囲にある焦点しか出力できない.

また, 内部計算も固定小数点数で行っているため, `gain::Focus`などとは異なる位相になる可能性がある.
詳しくは, [ファームウェアのドキュメント](./../../../Developer_Manual/fpga/stm.md)を参照.
