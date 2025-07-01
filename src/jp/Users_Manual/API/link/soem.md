# SOEM

[SOEM](https://github.com/OpenEtherCATsociety/SOEM)は有志が開発しているオープンソースのEherCAT Masterライブラリである.
TwinCATとは異なりリアルタイム性は保証されない.
そのため, 基本的にTwinCATを使用することを推奨する.
SOEMを使用するのはやむを得ない理由があるか, 開発時のみに限定するべきである.
一方, SOEMはクロスプラットフォームで動作し, インストールも単純という利点がある.

Windowsの場合は, [npcap](https://nmap.org/npcap/)を「**WinPcap API compatible mode**」でインストールしておくこと.
Linux/macOSの場合は, 特に準備は必要ない.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-soem
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
if(WIN32)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v35.0.1/autd3-link-soem-v35.0.1-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v35.0.1/autd3-link-soem-v35.0.1-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v35.0.1/autd3-link-soem-v35.0.1-linux-x64.tar.gz
  )
endif()
FetchContent_MakeAvailable(autd3-link-soem)
target_link_libraries(<TARGET> PRIVATE autd3::link::soem)
```
{{ #endtab }}
{{ #tab name=C# }}
```shell
dotnet add package AUTD3Sharp.Link.SOEM
```
{{ #endtab }}
{{ #tab name=Unity }}
`https://github.com/shinolab/AUTD3Sharp.Link.SOEM.git#upm/latest`をUnity Package Managerで追加する.
{{ #endtab }}
{{ #tab name=Python }}
```shell
pip install pyautd3_link_soem
```
{{ #endtab }}
{{ #endtabs }}

## APIs

第1引数にはエラーが起きたときのコールバック関数を, 第2引数にはオプションを指定する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/soem_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/soem_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/soem_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/soem_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

SOEMリンクで指定できるオプションは以下の通りである.
デフォルト値は上記の通り.

- `buf_size`: 送信キューバッファサイズ. 通常は変更する必要はない.
- `ifname`: ネットワークインタフェース名. 空白の場合はAUTD3デバイスが接続されているネットワークインタフェースを自動的に選択する.
- `state_check_interval`: エラーが出ているかどうかを確認する間隔
- `sync0_cycle`: 同期信号の周期
- `send_cycle`: 送信サイクル
    - `SOEM`も大量のデバイスを接続すると挙動が不安定になる場合がある[^fn_soem]. このときは, `sync0_cycle`と`send_cycle`の値を増やす. これら値はエラーが出ない中で, 可能な限り小さな値が望ましい. どの程度の値にすべきかは接続している台数に依存する. 例えば, 9台の場合は$1.5-\SI{2}{ms}$程度の値にしておけば動作するはずである.
- `thread_priority`: スレッドの優先度
- `process_priority`: (Windowsのみ) プロセスの優先度
- `sync_tolerance`: 同期許容レベル. 初期化時, 各デバイスのシステム時間差がこの値以下になるまで待機する. 以下のタイムアウト時間が経過しても同期が完了しない場合はエラーとなる. この値を変更することは推奨されない.
- `sync_timeout`: 同期タイムアウト. 上記のシステム時間差測定のタイムアウト時間.
- `affinity`: CPUアフィニティ. `None`の場合はOSに任せる.

[^fn_soem]: TwinCATよりは緩く, 普通に動くこともある.
