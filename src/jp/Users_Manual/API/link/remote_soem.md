# RemoteSOEM

このLinkは`SOEM`を動かすサーバーPCとユーザプログラムを動かすクライアントPCを分離するためのものである.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-soem --features "remote blocking"
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
if(WIN32)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v31.0.1/autd3-link-soem-v31.0.1-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v31.0.1/autd3-link-soem-v31.0.1-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v31.0.1/autd3-link-soem-v31.0.1-linux-x64.tar.gz
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

## セットアップ

`RemoteSOEM`を使用する場合はPCを2台用意する必要がある.
この時, 片方のPCは[`SOEM`](./soem.md)が使えるPCである必要がある.
このPCをここでは"サーバ"と呼ぶ.
一方, 開発側のPC, 即ちSDKを使用する側は特に制約はなく, サーバと同じLANに繋がっていれば良い, こちらをここでは"クライアント"と呼ぶ.

まず, サーバとAUTDデバイスを接続する.
また, サーバとクライアントを別のLANで繋ぐ[^fn_remote_soem].
そして, サーバとクライアント間のLANのIPを確認しておく.
ここでは例えば, サーバ側が`172.16.99.104`, クライアント側が`172.16.99.62`だったとする.

### AUTD Server

`RemoteSOEM`を使用する場合, サーバに`AUTD Server`をインストールする必要がある.
[GitHub Releases](https://github.com/shinolab/autd3-server/releases)にてインストーラを配布しているので, これをダウンロードし, 指示に従ってインストールする.

`AUTD Server`を実行すると, 以下のような画面になるので, `SOEM`タブを開く.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_remotesoem.jpg"/>
</figure>

ポートに適当なポート番号を指定し, `Run`ボタンを押す.

AUTD3デバイスが見つかり, クライアントとの接続待ちである旨のメッセージが表示されれば成功である.

なお, `AUTD Server`では[`SOEM`](./soem.md)と同等のオプションを指定できる.

### APIs

`RemoteSOEM`のコンストラクタでは, <サーバのIP:ポート>を指定する.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

## ファイアウォール

TCP関係のエラーが出る場合は, ファイアウォールでブロックされている可能性がある.
その場合は, ファイアウォールの設定でTCP/UDPの指定したポートの接続を許可する.

[^fn_remote_soem]: 無線LANでも可
