# RemoteTwinCAT

前述の通り, AUTD3とTwinCATを使う場合はWindows OSと特定のネットワークアダプタが必要になる.
Windows以外のPCで開発したい場合は, `RemoteTwinCAT` linkを用いてLinux/macOSから遠隔でTwinCATを操作することができる.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5  for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-link-twincat --features remote
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::twincat)
```

<div class="tab_content" id="cs_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="unity_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="python_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>
</div>

## セットアップ

`RemoteTwinCAT`を使用する場合はPCを2台用意する必要がある.
この時, 片方のPCは[`TwinCAT`](./twincat.md)が使えるPCである必要がある.
このPCをここでは"サーバ"と呼ぶ.
一方, 開発側のPC, 即ちSDKを使用する側は特に制約はなく, サーバと同じLANに繋がっていれば良い, こちらをここでは"クライアント"と呼ぶ.

まず, サーバとAUTDデバイスを接続する.
この時使うLANのアダプタは`TwinCAT`と同じく, TwinCAT対応のアダプタである必要がある.
また, サーバとクライアントを別のLANで繋ぐ.
こちらのLANアダプタはTwinCAT対応である必要はない[^fn_remote_twin].
そして, サーバとクライアント間のLANのIPを確認しておく.
ここでは例えば, サーバ側が`172.16.99.104`, クライアント側が`172.16.99.62`だったとする.
次に, サーバで`AUTD Server`を起動する.
この時, `Client IP address`にクライアントのIPアドレス (この例だと`172.16.99.62`) を指定する.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_remotetwincat.jpg"/>
</figure>

右側の画面に, 「Server AmsNetId」と「Client AmsNetId」が表示されるので, これをメモっておく.

> NOTE: 「Server AmsNetId」の最初の4桁は必ずしもServerのIPアドレスを意味しているわけではないので注意されたい.

## APIs

`RemoteTwinCAT`のコンストラクタには「Server AmsNetId」を指定する.

また, `server_ip`と`client_ams_net_id`でサーバーのIPアドレスとクライアントのNetIdを指定する.
これらは省略することも可能だが, 基本的には指定することを推奨する.

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.py}}
```
</div>

### ファイアウォール

TCP関係のエラーが出る場合は, ファイアウォールでADSプロトコルがブロックされている可能性がある.
その場合は, ファイアウォールの設定でTCP/UDPの48898番ポートの接続を許可する.

[^fn_remote_twin]: 無線LANでも可
