# リモートサーバの構築

リモートサーバを構築することで, AUTDとの通信処理をサーバに委譲することができる.

## セットアップ

リモートサーバを走らせるには, [Rust](https://rust-lang.org/ja/)をインストールする必要がある.

次に, 以下のコマンドでRustのプロジェクトを新規作成する.

```shell
cargo new autd_remote_server
cd autd_remote_server
```

次に`autd3-link-remote` crateと非同期ランタイムとして[`tokio`](https://crates.io/crates/tokio)を追加する.

```shell
cargo add autd3-link-remote --features server
cargo add tokio --features full
```

次に, 適当なLinkを追加する. ここでは説明のため, `autd3` crateにあるダミーの`Nop`リンクを使用する.

```shell
cargo add autd3 --features link-nop
```

次に, `src/main.rs`を以下のように編集する.

`RemoteServer::new`の第1引数には使用するポート番号を, 第2引数には使用するLinkを生成する関数を指定する.

```rust,no_run
{{#include ../../../codes/Users_Manual/advanced/remote_server.rs}}
```

あとは, クライアント側で[`Remote`](../API/link/remote.md)リンクを使用して, サーバに接続すれば良い.
