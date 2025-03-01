# RemoteTwinCAT

As mentioned earlier, using AUTD3 with TwinCAT requires a Windows OS and a specific network adapter.
If you want to develop on a non-Windows PC, you can use the `RemoteTwinCAT` link to remotely operate TwinCAT from Linux/macOS.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5  for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5  for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-link-twincat --features remote
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::twincat)
```

<div class="tab_content" id="cs_code_content">
  <p>
    Included in the main library.
  </p>
</div>

<div class="tab_content" id="unity_code_content">
  <p>
    Included in the main library.
  </p>
</div>

<div class="tab_content" id="python_code_content">
  <p>
    Included in the main library.
  </p>
</div>
</div>

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

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/link/remote_twincat_0.py}}
```
</div>

### Firewall

If you encounter TCP-related errors, it is possible that the ADS protocol is being blocked by the firewall.
In that case, configure the firewall to allow connections on TCP/UDP port 48898.

[^fn_remote_twin]: Wireless LAN is also acceptable.
