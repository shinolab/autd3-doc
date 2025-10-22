# RemoteTwinCAT

> NOTE: このリンクはRustからのみ使用可能である. 同等の機能が[`Remote`](./remote.md)で提供されている.

前述の通り, AUTD3とTwinCATを使う場合はWindows OSと特定のネットワークアダプタが必要になる.
Windows以外のPCで開発したい場合は, `RemoteTwinCAT` linkを用いてLinux/macOSから遠隔でTwinCATを操作することができる.

## Install

```shell
cargo add autd3-link-twincat --features remote
```

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

`RemoteTwinCAT`のコンストラクタにはServerのIPアドレスとAmsNetIdを指定する.

また, オプションでタイムアウトとソースアドレスを指定できる.

```rust
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.rs}}
```

### ファイアウォール

TCP関係のエラーが出る場合は, ファイアウォールでADSプロトコルがブロックされている可能性がある.
その場合は, ファイアウォールの設定でTCP/UDPの48898番ポートの接続を許可する.

[^fn_remote_twin]: 無線LANでも可
