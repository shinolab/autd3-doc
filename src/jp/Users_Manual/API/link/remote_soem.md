# RemoteSOEM


このLinkは`SOEM`を動かすサーバーPCとユーザプログラムを動かすクライアントPCを分離するためのものである.

### Install

#### Rust

```shell
cargo add autd3-link-soem --features "remote blocking"
```

#### C++/C#/Unity/Python

[SOEM](#install)と同じ.

### Usage

`RemoteSOEM`を使用する場合はPCを2台用意する必要がある.
この時, 片方のPCは`SOEM` linkが使えるである必要がある.
このPCをここでは"サーバ"と呼ぶ.
一方, 開発側のPC, 即ちSDKを使用する側は特に制約はなく, サーバと同じLANに繋がっていれば良い, こちらをここでは"クライアント"と呼ぶ.

まず, サーバとAUTDデバイスを接続する.
また, サーバとクライアントを別のLANで繋ぐ[^fn_remote_soem].
そして, サーバとクライアント間のLANのIPを確認しておく.
ここでは例えば, サーバ側が`172.16.99.104`, クライアント側が`172.16.99.62`だったとする.

#### AUTD Server

`RemoteSOEM`を使用する場合, サーバに`AUTD Server`をインストールする必要がある.
[GitHub Releases](https://github.com/shinolab/autd3-server/releases)にてインストーラを配布しているので, これをダウンロードし, 指示に従ってインストールする.

`AUTD Server`を実行すると, 以下のような画面になるので, `SOEM`タブを開く.

<figure>
  <img src="../../fig/Users_Manual/autdserver_remotesoem.jpg"/>
</figure>

ポートに適当なポート番号を指定し, `Run`ボタンを押す.

AUTD3デバイスが見つかり, クライアントとの接続待ちである旨のメッセージが表示されれば成功である.

なお, `AUTD Server`では`SOEM`と同等のオプションを指定できる.

### APIs

`RemoteSOEM`のコンストラクタでは, <サーバのIP:ポート>を指定する.

```rust,should_panic,edition2024
{{#include ../../../codes/Users_Manual/link/remote_soem_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/remote_soem_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/remote_soem_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/remote_soem_0.py}}
```

### ファイアウォール

TCP関係のエラーが出る場合は, ファイアウォールでブロックされている可能性がある.
その場合は, ファイアウォールの設定でTCP/UDPの指定したポートの接続を許可する.

[^fn_soem]: TwinCATよりは緩く, 普通に動くこともある.

[^fn_remote_soem]: 無線LANでも可
