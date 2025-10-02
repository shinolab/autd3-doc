# Asynchronous API

The Rust library supports asynchronous processing.

> NOTE: This feature is not available in the C++, C#, and Python libraries.

## Setup

To perform asynchronous processing, you need to enable the `async` feature of the `autd3` crate.

```shell
cargo add autd3 --features "async"
```

Also, you may need to enable the `async` feature for each Link.

- `TwinCAT`

    ```shell
    cargo add autd3-link-twincat --features "async"
    ```
    
- `RemoteTwinCAT`

    ```shell
    cargo add autd3-link-twincat --features "remote async"
    ```

- `EtherCrab`, `Simulator`
  - Enabled by default 


To use the asynchronous API, use `autd3::r#async::Controller` instead of the `Controller`.

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/async.rs}}
```
