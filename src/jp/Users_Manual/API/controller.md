# Controller

ここでは, `Controller`クラスに存在するAPIを紹介する.

[[_TOC_]]

## fpga_state

FPGAの状態を取得する.
これを使用する前に, `ReadsFPGAState`で状態取得を有効化しておく必要がある.

<div class="tabs">
<input id="rust_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state" checked>
<label class="tab_item" n=4 for="rust_tab_fpga_state">Rust</label>
<input id="cpp_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="cpp_tab_fpga_state">C++</label>
<input id="cs_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="cs_tab_fpga_state">C#</label>
<input id="python_tab_fpga_state" type="radio" class="tab" name="tab_fpga_state">
<label class="tab_item" n=4 for="python_tab_fpga_state">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/controller_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/controller_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/controller_0.py}}
```
</div>

`ReadsFPGAState`コンストラクタの引数は`Fn(&Device) -> bool`で, デバイス毎に状態取得を有効化するかどうかを指定する.

有効化していないデバイスに対して`fpga_state`は`None`を返す.

FPGAの状態としては, 現在以下の情報が取得できる.

- `is_thermal_assert`: ファン制御用の温度センサがアサートされているかどうか
- `current_mod_segment`: 現在のModulation Segment
- `current_stm_segment`: 現在のFociSTM/GainSTM Segment
- `current_gain_segment`: 現在のGain Segment
- `is_gain_mode`: 現在Gainが使用されているかどうか
- `is_stm_mode`: 現在FociSTM/GainSTMが使用されているかどうか

## send

デバイスにデータを送信する.

データは単体か2つのみ同時に送信することができる.

## group_send

`group_send`関数を使用すると, デバイスをグルーピングすることができる.

<div class="tabs">
<input id="rust_tab_group" type="radio" class="tab" name="tab_group" checked>
<label class="tab_item" n=4 for="rust_tab_group">Rust</label>
<input id="cpp_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="cpp_tab_group">C++</label>
<input id="cs_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="cs_tab_group">C#</label>
<input id="python_tab_group" type="radio" class="tab" name="tab_group">
<label class="tab_item" n=4 for="python_tab_group">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/controller_2.rs}}
```

> NOTE: Rust版は`HashMap`の値がすべて同じ型である必要があるため, ここでは`into_boxed`を使用して, 型を統一している.

```cpp
{{#include ../../../codes/Users_Manual/controller_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/controller_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/controller_2.py}}
```
</div>

`gain::Group`とは異なり, 通常の`send`で送信できるデータなら何でも使用できる.
ただし, デバイス単位でしかグルーピングできない.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, `HashMap`のキーとして使用できるものなら何でも良い.

## sender

送信時の設定を`sender`経由で指定できる.

<div class="tabs">
<input id="rust_tab_sender" type="radio" class="tab" name="tab_sender" checked>
<label class="tab_item" n=4 for="rust_tab_sender">Rust</label>
<input id="cpp_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="cpp_tab_sender">C++</label>
<input id="cs_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="cs_tab_sender">C#</label>
<input id="python_tab_sender" type="radio" class="tab" name="tab_sender">
<label class="tab_item" n=4 for="python_tab_sender">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/sender.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/sender.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/sender.cs}}
```

```python
{{#include ../../../codes/Users_Manual/sender.py}}
```
</div>

ここで,
- `send_interval`: 送信間隔
- `receive_interval`: 受信間隔
- `timeout`: タイムアウト時間. 詳細は[タイムアウトについて](#タイムアウトについて)を参照
- `parallel`: 並列計算モード. 詳細は[並列計算について](#並列計算について)を参照
- `sleeper`: 送受信間隔を調整する構造体
    - `SpinSleeper`: [`spin_sleep`](https://crates.io/crates/spin_sleep)を使用
    - `StdSleeper`: `std::thread::sleep`を使用
    - `WaitableSleeper`: (Windowsのみ) [`Waitable Timer`](https://learn.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects)を使用
であり, デフォルト値は上記の通り.

なお, `Controller::send`, `Controller::group_send`はデフォルトの`SenderOption`を使用した場合と等価である.

### タイムアウトについて

タイムアウトの値が
- 0より大きい場合, 送信データがデバイスで処理されるか, 指定したタイムアウト時間が経過するまで待機する. 送信データがデバイスで処理されたのが確認できなかった場合にエラーを返す.
- 0の場合, `send`関数は送信データがデバイスで処理されたかどうかのチェックを行わない.

確実にデータを送信したい場合はこれを適当な値に設定しておくことをおすすめする.

`SenderOption`で指定しない場合, 以下に示す各データのデフォルト値が使用される.

|       | タイムアウト値   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`PulseWidthEncoder`/`ReadsFPGAState`/<br>`SwapSegment`/`Silencer`/<br>`Synchronize`/`FociSTM`/<br>`GainSTM`/`Modulation` | $\SI{200}{ms}$ | 
| `Gain`  | $\SI{20}{ms}$ | 

複数をまとめて送信する場合は, それぞれのデータのタイムアウト値の最大値が使用される.

### 並列計算について

各データの内部での計算は, デバイス単位で並列に実行することができる.

`ParallelMode::On`を指定すると並列計算を有効化, `ParallelMode::Off`を指定すると無効化する.

`ParallelMode::Auto`の場合, 有効なデバイスの数が以下に示す各データの並列計算スレッショルド値を超える場合に並列計算が有効化される.

|       | 並列計算スレッショルド値   | 
| ----- | -------------- | 
| `Clear`/`DebugSettings`/<br>`ForceFan`/`PhaseCorrection`/<br>`ReadsFPGAState`/`SwapSegment`/<br>`Silencer`/`Synchronize`/<br>`FociSTM` (焦点数が4000未満)/<br>`Modulation` | 18446744073709551615 | 
| `PulseWidthEncoder`/<br>`FociSTM` (焦点数が4000以上)/<br>/`GainSTM`/`Gain` | 4 | 
