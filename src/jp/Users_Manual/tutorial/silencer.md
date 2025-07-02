# 静音化

焦点を高速に動かしたり, AM変調をかけたりすると可聴音ノイズが発生する.
AUTD3にはこれを抑制する[Silencer](./../API/silencer.md)という機能がある.
Silencerは, 振幅/位相データの急峻な変化を抑える, つまり, 位相/振幅変化を補間することで可聴音ノイズを抑制する.

Silencerはデフォルトで有効になっており, これを無効化するには以下の様に`Silencer::disable()`を送信すれば良い.

> NOTE: 以下のコードを実行すると大きな騒音が発生するので, 実行する際は注意すること.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/silencer/disable.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/silencer/disable.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/silencer/disable.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/silencer/disable.py}}
```
{{ #endtab }}
{{ #endtabs }}

`Silencer::disable()`を送信する部分をコメントアウトして, ノイズの差を確認してみると良いだろう.

詳細は[Silencer](./../API/silencer.md)を参照されたいが, `Silencer`によってノイズは抑制されるものの, `Silencer`によって, ユーザが指定していない位相や振幅を出力する, あるいは, ユーザが指定した位相や振幅が出力されない可能性がある.
前者は本質的に避けられないが, 後者は避けられる場合もある.
具体的には, `FociSTM/GainSTM`や`Modulation`など, 位相/振幅が変化する間隔がわかっている場合, `Silencer`による位相/振幅補間がその間隔よりも短くあれば後者の問題は起こらない.

デフォルトでは, 上記のようなユーザが指定した位相や振幅が出力されない問題を回避するように設定されている.
`Silencer`は振幅に対して$\SI{0.25}{ms}$, 位相に対して$\SI{1}{ms}$の時間をかけて補間を行い, これを超えるサンプリングレートに対してはエラーを返す.
つまり,  `FociSTM/GainSTM`のサンプリング周期は$\SI{1}{ms}$以上, `Modulation`のサンプリング周期は$\SI{0.25}{ms}$以上である必要がある.

したがって, 例えば以下のコードは, サンプリング周期が$1/\SI{50}{Hz}/40=\SI{0.5}{ms}$となるので実行時エラーとなる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/silencer/err.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/silencer/err.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/silencer/err.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/silencer/err.py}}
```
{{ #endtab }}
{{ #endtabs }}

このエラーを回避する方法は以下の通りである.

1. サンプリングレートを下げる.
    - 最初の例のように, `point_num = 20`とすれば, サンプリング周期が$1/\SI{50}{Hz}/20=\SI{1}{ms}$となるので, エラーは発生しない.
1. `Silencer`の補間周期を短くする.
    - `Silencer`のデフォルトの補間間隔は振幅に対して$\SI{0.25}{ms}$, 位相に対して$\SI{1}{ms}$であるが, これは[変更できる](./../API/silencer.md#fixed-completion-time-mode). 例えば, 以下の例だと$\SI{0.5}{ms}$に設定すればエラーにならなくなる.
    - ただし, 補間間隔を短くするとその分ノイズが大きくなるので注意.
    - なお, `Silencer::disable()`は補間間隔を$\SI{25}{μs}$に設定するのと等価である.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/silencer/workaround_2.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/silencer/workaround_2.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/silencer/workaround_2.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/silencer/workaround_2.py}}
```
{{ #endtab }}
{{ #endtabs }}

3. [FixedUpdateRate](./../API/silencer.md#fixed-update-rate-mode)を使用する.
    - これを使用する場合, ユーザが指定した位相や振幅が出力されない (補間が完了する前に次のデータに移行してしまう) 可能性があるので注意.
4. `FixedCompletionTime::strict`を`false`に設定する.
    - これは単にエラーを無視するだけなので, 使用は推奨されない.
