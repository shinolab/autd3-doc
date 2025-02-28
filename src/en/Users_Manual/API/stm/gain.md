# GainSTM

`GainSTM`は`FociSTM`とは異なり, 任意の`Gain`を扱える. ただし, 使用できる`Gain`の個数は$1024$ (拡張モードの場合$2048$) となる.

`GainSTM`の使用方法は以下のようになる.
これは, アレイの中心から直上$\SI{150}{mm}$の点を中心とした半径$\SI{30}{mm}$の円周上で焦点を回すサンプルである.
円周上を200点サンプリングし, 一周を$\SI{1}{Hz}$で回るようにしている. (すなわち, サンプリング周波数は$\SI{200}{Hz}$である.)

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../../codes/Users_Manual/stm/gain_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/stm/gain_0.cpp}}

```

```cs
{{#include ../../../../codes/Users_Manual/stm/gain_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/stm/gain_0.py}}
```
</div>

## GainSTMMode

`GainSTM`は位相/振幅データをすべて送信するため, レイテンシが大きい[^fn_gain_seq].
この問題に対処するため, `GainSTM`には位相のみを送信して送信にかかる時間を半分にする`PhaseFull`モードと, 位相を4bitに圧縮して送信時間を4分の1にする`PhaseHalf`モードが用意されている.
この2つのモードでは振幅は最大値が使用される.

デフォルトは振幅/位相データを送る`PhaseIntensityFull`モードである.

[^fn_gain_seq]: `FociSTM<1>`のおよそ75倍のレイテンシ
