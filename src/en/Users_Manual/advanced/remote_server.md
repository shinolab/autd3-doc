# Building a Remote Server

By building a remote server, you can delegate the communication process with AUTD to the server.

## Setup

To run a remote server, you need to install [Rust](https://rust-lang.org/).

Next, create a new Rust project with the following commands:

```shell
cargo new autd_remote_server
cd autd_remote_server
```

Next, add the `autd3-link-remote` crate and [`tokio`](https://crates.io/crates/tokio) as an asynchronous runtime.

```shell
cargo add autd3-link-remote --features server
cargo add tokio --features full
```

Next, add an appropriate Link. Here, for the sake of explanation, we use the dummy `Nop` link from the `autd3` crate.

```shell
cargo add autd3 --features link-nop
```

Next, edit `src/main.rs` as follows.

In the first argument of `RemoteServer::new`, specify the port number to use, and in the second argument, specify the Link factory to use.

```rust,no_run
{{#include ../../../codes/Users_Manual/advanced/remote_server.rs}}
```

After that, you just need to connect to the server using the [`Remote`](../API/link/remote.md) link on the client side.
