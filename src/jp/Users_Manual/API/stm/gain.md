# GainSTM

`GainSTM`は`FociSTM`とは異なり, 任意の`Gain`を扱える. ただし, 使用できる`Gain`の個数は$1024$ (拡張モードの場合$2048$) となる.

`GainSTM`の使用方法は以下のようになる.
これは, アレイの中心から直上$\SI{150}{mm}$の点を中心とした半径$\SI{30}{mm}$の円周上で焦点を回すサンプルである.
円周上を200点サンプリングし, 一周を$\SI{1}{Hz}$で回るようにしている. (すなわち, サンプリング周波数は$\SI{200}{Hz}$である.)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/gain_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/stm/gain_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/stm/gain_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/stm/gain_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

## GainSTMMode

`GainSTM`は位相/振幅データをすべて送信するため, レイテンシが大きい[^fn_gain_seq].
この問題に対処するため, `GainSTM`には位相のみを送信して送信にかかる時間を半分にする`PhaseFull`モードと, 位相を4bitに圧縮して送信時間を4分の1にする`PhaseHalf`モードが用意されている.
この2つのモードでは振幅は最大値が使用される.

デフォルトは振幅/位相データを送る`PhaseIntensityFull`モードである.

[^fn_gain_seq]: `FociSTM<1>`のおよそ75倍のレイテンシ
