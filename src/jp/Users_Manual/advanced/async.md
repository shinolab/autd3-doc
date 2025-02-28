# 非同期API

Rust版のライブラリでは非同期処理をサポートしている.

> NOTE: C++, C#, Python版のライブラリでは, この機能は提供されていない.

## Setup

非同期処理を行うには, `autd3` crateの`async` featureを有効にする必要がある.

```shell
cargo add autd3 --features "async"
```

また, 各Linkに対して, `async` featureを有効にする必要がある場合がある.

- SOEM

    ```shell
    cargo add autd3-link-soem --features "async"
    ```
    
- TwinCAT

    ```shell
    cargo add autd3-link-twincat --features "async"
    ```
    
- RemoteTwinCAT

    ```shell
    cargo add autd3-link-twincat --features "remote async"
    ```

- RemoteSOEM, Simulator
  - デフォルトで有効 


非同期APIを使用するには, 通常の`Controller`の代わりに, `autd3::r#async::Controller`を使用すればいい.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/async.rs}}
```
