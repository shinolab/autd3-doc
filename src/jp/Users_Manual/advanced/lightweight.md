# Lightweightモード

Rust, 及び, [Dart版](https://github.com/shinolab/autd3-dart)のライブラリではLightweightモードをサポートしている.

> NOTE: Dart版のライブラリはLightweightモードのみサポートしている.

Lightweightモードは, `RemoteTwinCAT`, `RemoteSOEM`, `Simulator` リンクを使用する際に, 通信量を削減するためのモードである.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.
> ただし, Lightweightモードの通信にはProtocol Buffersを使用しているため, [proto定義](https://github.com/shinolab/autd3-rs/tree/main/autd3-protobuf/proto)に従ってデータを送信すれば, 各言語から使用することは可能.

## Setup

lightweightモードのクライアントを使用するには, `autd3-protobuf` crateの`lightweight` featureを有効にする必要がある.

```shell
cargo add autd3-protobuf --features "lightweight"
```

サーバ側は, AUTD3 ServerのオプションでLightweightモードを有効にすればいい.

以下が, Lightweightモードを使用するクライアント側のRustのサンプルコードである.

基本的に通常のAPIと同じであるが, 以下の点に注意.

- `GainSTM`使用時に`autd3_protobuf::lightweight::IntoLightweightGain::into_lightweight()`を使用する必要がある
- 一部機能は使用できない

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/lightweight.rs}}
```

Dartからの使用例は, [autd3-app](https://github.com/shinolab/autd3-app)のリポジトリを参照されたい.
