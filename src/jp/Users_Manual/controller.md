# Controller

ここでは, `Controller`クラスに存在するAPIを紹介する.

[[_TOC_]]

## Controllerの設定

Controllerには以下の設定が存在する.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_config.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_config.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_config.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_config.py}}
```
- `parallel_threshold`: 並列化スレッショルドの値. デフォルトは4. 詳しくは[以下](#並列計算)を参照.
- `send_interval`: 送信間隔. デフォルトは$\SI{1}{ms}$.
- `receive_interval`: 受信間隔. デフォルトは$\SI{1}{ms}$.
- `timer_resolution`: (Windowsのみ) タイマー分解能. デフォルトは1. 無効化したい場合は`None`を指定する.

## send

デバイスにデータを送信する.

データは単体か2つのみ同時に送信することができる.

送受信の間隔は, [Controllerの設定](##Controllerの設定)で変更可能.

### タイムアウト

`with_timeout`でタイムアウト時間を指定できる.
これを省略した場合は各データに設定されているデフォルト値があれば使用される.
各データにデフォルト値が設定されていない場合は, [Link](./link.md)で設定したタイムアウト時間が使用される.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_1.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_1.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_1.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_1.py}}
```

タイムアウトの値が0より大きい場合, 送信データがデバイスで処理されるか, 指定したタイムアウト時間が経過するまで待機する.
送信データがデバイスで処理されたのが確認できなかった場合にエラーを返す.

タイムアウトの値が0の場合, `send`関数は送信データがデバイスで処理されたかどうかのチェックを行わない.

確実にデータを送信したい場合はこれを適当な値に設定しておくことをおすすめする.


### 並列計算

各データの内部での計算は, デバイスの数が並列計算スレッショルドより大きい場合に, デバイス単位で並列に実行される.

`with_parallel_threshold`でこの並列計算スレッショルドを設定できる.
これを省略した場合は各データに設定されているデフォルト値があれば使用される.
各データにデフォルト値が設定されていない場合は, [Controllerの設定](#Controllerの設定)で設定した値が使用される.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_with_parallel.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_with_parallel.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_with_parallel.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_with_parallel.py}}
```

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

なお, タイムアウトは, `set`したものの中で最大のものが使用される.
`set`したものの中にタイムアウトを指定したものがなければ, 各データのデフォルト値が使用される.
それもなければ, [Link](./link.md)で設定したタイムアウト時間が使用される.
また, 並列計算スレッショルドは, `set`したものの中で最小のものが使用される.
`set`したものの中に並列計算スレッショルドを指定したものがなければ, 各データのデフォルト値が使用される.
それもなければ, [Controllerの設定](#Controllerの設定)で設定した値が使用される.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, HashMapのキーとして使用できるものなら何でも良い.
