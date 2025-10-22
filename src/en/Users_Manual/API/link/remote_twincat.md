# RemoteTwinCAT

> NOTE: This link is only available from Rust. Equivalent functionality is provided by [`Remote`](./remote.md).

As mentioned earlier, using AUTD3 with TwinCAT requires a Windows OS and a specific network adapter.
If you want to develop on a non-Windows PC, you can use the `RemoteTwinCAT` link to remotely operate TwinCAT from Linux/macOS.

## Install

```shell
cargo add autd3-link-twincat --features remote
```

## Setup

To use `RemoteTwinCAT`, you need two PCs.
One of these PCs must be able to use [`TwinCAT`](./twincat.md).
Hereby, this PC is referred to as the "server".
The other PC, which is the development PC using the SDK, has no particular restrictions as long as it is connected to the same LAN as the server. H
ereby, this PC is referred to as the "client".

First, connect the server to the AUTD device.
The LAN adapter used for this connection must be a TwinCAT-compatible adapter.
Then, connect the server and client via a different LAN.
This LAN adapter does not need to be TwinCAT-compatible[^fn_remote_twin].
Next, check the IP addresses of the LAN between the server and client.
For example, let's assume the server's IP is `172.16.99.104` and the client's IP is `172.16.99.62`.
Next, start the `AUTD Server` on the server.
Specify the client's IP address (in this example, `172.16.99.62`) in the `Client IP address` field.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_remotetwincat.jpg"/>
</figure>

The "Server AmsNetId" and "Client AmsNetId" will be displayed on the right side of the screen, so make a note of them.

> NOTE: The first four digits of the "Server AmsNetId" do not necessarily represent the server's IP address.

## APIs

In the constructor of `RemoteTwinCAT`, specify the ip address and AmsNetId of the server.

You can also specify the timeout and source address as options.

```rust
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.rs}}
```

### Firewall

If you encounter TCP-related errors, it is possible that the ADS protocol is being blocked by the firewall.
In that case, configure the firewall to allow connections on TCP/UDP port 48898.

[^fn_remote_twin]: Wireless LAN is also acceptable.
