# 焦点の移動

autd3において, `Gain`は送信するたびに上書きされる.
したがって, 次のようなコードを実行すると, 約1秒ごとに焦点の位置が移動する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/soft.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/soft.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/soft.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/soft.py}}
```
{{ #endtab }}
{{ #endtabs }}

なお, `Gain`と`Modulation`は独立しているので, どちらの焦点にも$\SI{150}{Hz}$の正弦波AM変調がかかる.

上記のコードだとソフトウェア的にタイミングを制御している.
これの精度はOSや実行環境に依存するため, より精度の高い制御が必要な場合は, [`FociSTM/GainSTM`](./../API/stm.md)を使用することをおすすめする.

`FociSTM`を使用して上記と同等の動作を実現するコードは以下の通りである.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/hard.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/hard.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/hard.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/move_focus/hard.py}}
```
{{ #endtab }}
{{ #endtabs }}

`FociSTM/GainSTM`はAUTD3デバイス内部でループされるため, ソフトウェアループは必要なく, `FociSTM/GainSTM`の送信以降自動的に無限ループする.
また, タイミングはAUTD3デバイス内蔵のタイマーで制御されるため, 精度が高く, 解像度も最高で$\SI{25}{μs}$単位で指定できる
ただし, このタイマーの制約上, [出力不可能な周波数が存在する](./../API/stm/focus.md).

`FociSTM/GainSTM`の切り替えタイミングは, 1ループの周波数, または周期で指定する.
すなわち, この場合は2つの焦点で$\SI{0.5}{Hz}\ (\SI{2}{s})$となるので, 各焦点は$\SI{1}{s}$出力される.
なお, [`SamplingConfig`](./../API/sampling_config.md)を使用することで, 1ループあたりではなく, サンプリング周波数, すなわち1焦点あたりの周波数や周期を指定することもできる.
したがって, 上記のコードのコメントアウト部分はすべて等価である.
