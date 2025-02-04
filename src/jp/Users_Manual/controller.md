# Controller

ここでは, `Controller`クラスに存在するAPIを紹介する.

[[_TOC_]]

## send

デバイスにデータを送信する.

データは単体か2つのみ同時に送信することができる.

送受信の間隔は, [Controllerの設定](##Controllerの設定)で変更可能.

### タイムアウト

各データにはタイムアウトの値が設定されている.

タイムアウトの値が
- 0より大きい場合, 送信データがデバイスで処理されるか, 指定したタイムアウト時間が経過するまで待機する. 送信データがデバイスで処理されたのが確認できなかった場合にエラーを返す.
- 0の場合, `send`関数は送信データがデバイスで処理されたかどうかのチェックを行わない.

確実にデータを送信したい場合はこれを適当な値に設定しておくことをおすすめする.

各データに設定されている値は以下の通りである.

|       | タイムアウト値   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`PulseWidthEncoder`/`ReadsFPGAState`/<br>`SwapSegment`/`Silencer`/<br>`Synchronize`/`FociSTM`/<br>`GainSTM`/`Modulation` | $\SI{200}{ms}$ | 
| `Gain`  | `None` | 
| (`a`, `b`) | `a`と`b`で大きい方, 片方が`None`の場合はもう片方, 両方`None`の場合は`None` | 

タイムアウトは`with_timeout`で上書きできる.

### 並列計算

各データの内部での計算は, デバイスの数が並列計算スレッショルドより大きい場合に, デバイス単位で並列に実行される.

各データに設定されている値は以下の通りである.


|       | 並列計算スレッショルド値   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`ReadsFPGAState`/`SwapSegment`/<br>`Silencer`/`Synchronize`/<br>`FociSTM` (焦点数が4000未満)/<br>`Modulation` | 18446744073709551615 | 
| `PulseWidthEncoder`/<br>`FociSTM` (焦点数が4000以上)/<br>/`GainSTM`/`Gain` | `None` | 
| (`a`, `b`) | `a`と`b`で小さい方, 片方が`None`の場合はもう片方, 両方`None`の場合は`None` | 

この値は`with_parallel_threshold`で上書きできる.

## fpga_state

FPGAの状態を取得する.
これを使用する前に, `ReadsFPGAState`で状態取得を有効化しておく必要がある.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_0.py}}
```

`ReadsFPGAState`コンストラクタの引数は`Fn(&Device) -> bool`で, デバイス毎に状態取得を有効化するかどうかを指定する.

有効化していないデバイスに対して`fpga_state`は`None`を返す.

FPGAの状態としては, 現在以下の情報が取得できる.

- `is_thermal_assert`: ファン制御用の温度センサがアサートされているかどうか
- `current_mod_segment`: 現在のModulation Segment
- `current_stm_segment`: 現在のFociSTM/GainSTM Segment
- `current_gain_segment`: 現在のGain Segment
- `is_gain_mode`: 現在Gainが使用されているかどうか
- `is_stm_mode`: 現在FociSTM/GainSTMが使用されているかどうか

## group

`group`関数を使用すると, デバイスをグルーピングすることができる.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_2.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_2.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_2.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_2.py}}
```

`gain::Group`とは異なり, 通常の`send`で送信できるデータなら何でも使用できる.
ただし, デバイス単位でしかグルーピングできない.

なお, タイムアウトは`set`したものの中で最大のもの, 並列計算スレッショルドは`set`したものの中で最小のものが使用される. 
すべて`None`の場合は, [Controllerの設定](#Controllerの設定)で設定したデフォルト値が使用される.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, HashMapのキーとして使用できるものなら何でも良い.
