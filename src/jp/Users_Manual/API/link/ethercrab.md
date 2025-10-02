# EtherCrab

> NOTE: TwinCATが使用可能な環境では, 基本的にTwinCATを使用することを推奨する.

このリンクはオープンソースのEtherCAT Masterライブラリである[EtherCrab](https://github.com/ethercrab-rs/ethercrab)を利用したリンクである.

Windowsの場合は, [npcap](https://nmap.org/npcap/)を「**WinPcap API compatible mode**」でインストールしておくこと.
Linux/macOSの場合は, 特に準備は必要ない.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-ethercrab
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::ethercrab)
```
{{ #endtab }}
{{ #tab name=C# }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Unity }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Python }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #endtabs }}

## APIs

第1引数にはエラーが起きたときのコールバック関数を, 第2引数にはオプションを指定する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.py}}
```
{{ #endtab }}
{{ #endtabs }}


`EtherCrab`リンクで指定できるオプションは以下の通りである.
デフォルト値は上記の通り.

- `ifname`: ネットワークインタフェース名. `None`の場合はAUTD3デバイスが接続されているネットワークインタフェースを自動的に選択する.
- `state_check_period`: エラーが出ているかどうかを確認する間隔
- `sync0_period`: 同期信号の周期
    - 大量のデバイスを接続すると挙動が不安定になる場合がある. このときは, `sync0_period`の値を増やす. これら値はエラーが出ない中で, 可能な限り小さな値が望ましい. どの程度の値にすべきかは接続している台数に依存する.
- `sync_tolerance`: 同期許容レベル. 初期化時, 各デバイスのシステム時間差がこの値以下になるまで待機する. 以下のタイムアウト時間が経過しても同期が完了しない場合はエラーとなる. この値を変更することは推奨されない.
- `sync_timeout`: 同期タイムアウト. 上記のシステム時間差測定のタイムアウト時間.
