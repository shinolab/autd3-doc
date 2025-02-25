# Lightweightモード

Rust, 及び, Dart版のライブラリではLightweightモードをサポートしている.

> NOTE: Dart版のライブラリはLightweightモードのみサポートしている.

Lightweightモードは, `RemoteTwinCAT`, `RemoteSOEM`, `Simulator` リンクを使用する際に, 通信量を削減するためのモードである.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.

## Setup

lightweightモードのクライアントを使用するには, `autd3-protobuf` crateの`lightweight` featureを有効にする必要がある.

```shell
cargo add autd3-protobuf --features "lightweight"
```

サーバ側は, AUTD3 ServerのオプションでLightweightモードを有効にすればいい.


以下が, Lightweightモードをを使用するクライアント側のRustのサンプルコードである.

データの送信が一つずつしか行えないこと以外は, 通常のAPIと同じである.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/lightweight.rs}}
```
