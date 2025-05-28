# Lightweight Mode

The Rust and [Dart](https://github.com/shinolab/autd3-dart) libraries support Lightweight mode.

> NOTE: The Dart library only supports Lightweight mode.

Lightweight mode is a mode to reduce transmission data when using `RemoteTwinCAT`, `RemoteSOEM`, or `Simulator` links.

> NOTE: This feature is not available in the C++, C#, and Python libraries.
> However, since Lightweight mode communication uses Protocol Buffers, it is possible to use it from each language by sending data according to the [proto definition](https://github.com/shinolab/autd3-rs/tree/main/autd3-protobuf/proto).

## Setup

To use the lightweight mode client, you need to enable the `lightweight` feature of the `autd3-protobuf` crate.

```shell
cargo add autd3-protobuf --features "lightweight"
```

On the server side, you can enable Lightweight mode with the AUTD3 Server options.

Below is a sample code for the client side in Rust using Lightweight mode.

Basically, it is the same as the normal API, but note the following points:

- When using `GainSTM`, you need to use `autd3_protobuf::lightweight::IntoLightweightGain::into_lightweight()`
- Some data is not supported

```rust,edition2024
{{#include ../../../codes/Users_Manual/advanced/lightweight.rs}}
```

For usage examples from Dart, refer to the [autd3-app](https://github.com/shinolab/autd3-app) repository.
