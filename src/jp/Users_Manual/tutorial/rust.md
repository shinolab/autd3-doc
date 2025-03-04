まずは適当なプロジェクトを作成し, `autd3`ライブラリを依存関係に追加する.
また, デバイスとの通信を行う`autd3-link-soem`ライブラリも依存関係に追加する.

```shell
cargo new --bin autd3-sample
cd autd3-sample
cargo add autd3
cargo add autd3-link-soem
```

次に, `src/main.rs`ファイルを編集し, 以下のようにする.
これは単一焦点に$\SI{150}{Hz}$のAM変調をかける場合のソースコードである.

```rust,should_panic,name=main.rs,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/single/main.rs}}
```

そして, これを実行する.

```shell
cargo run --release
```

### Linux,macOS使用時の注意

Linux, macOSでは, SOEMを使用するのに管理者権限が必要になる.
その場合は, 
```shell
cargo build --release && sudo ./target/release/autd3_sample
```
とすること.
