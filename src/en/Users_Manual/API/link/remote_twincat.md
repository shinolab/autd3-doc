# RemoteTwinCAT

As mentioned earlier, using AUTD3 with TwinCAT requires a Windows OS and a specific network adapter.
If you want to develop on a non-Windows PC, you can use the `RemoteTwinCAT` link to remotely operate TwinCAT from Linux/macOS.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-twincat --features remote
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::twincat)
```
{{ #endtab }}
{{ #tab name=C# }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Unity }}
Included in the main library.
{{ #endtab }}
{{ #tab name=Python }}
Included in the main library.
{{ #endtab }}
{{ #endtabs }}

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

In the constructor of `RemoteTwinCAT`, specify the "Server AmsNetId".

You can also specify the server's IP address and the client's NetId with `server_ip` and `client_ams_net_id`.
These can be omitted, but it is generally recommended to specify them.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

### Firewall

If you encounter TCP-related errors, it is possible that the ADS protocol is being blocked by the firewall.
In that case, configure the firewall to allow connections on TCP/UDP port 48898.

[^fn_remote_twin]: Wireless LAN is also acceptable.
