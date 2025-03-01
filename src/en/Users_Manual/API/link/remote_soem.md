# RemoteSOEM

This link is used to separate the server PC running `SOEM` from the client PC running the user program.

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
cargo add autd3-link-soem --features "remote blocking"
```

```cpp,name=CMakeLists.txt
if(WIN32)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v30.0.1/autd3-link-soem-v30.0.1-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v30.0.1/autd3-link-soem-v30.0.1-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v30.0.1/autd3-link-soem-v30.0.1-linux-x64.tar.gz
  )
endif()
FetchContent_MakeAvailable(autd3-link-soem)
target_link_libraries(<TARGET> PRIVATE autd3::link::soem)
```

```cs,name=Shell
dotnet add package AUTD3Sharp.Link.SOEM
```

<div class="tab_content" id="unity_code_content">
  <p>
    Add <code class="hljs">https://github.com/shinolab/AUTD3Sharp.Link.SOEM.git#upm/latest</code> to Unity Package Manager.
  </p>
</div>

```python,name=Shell
pip install pyautd3_link_soem
```
</div>

## Setup

To use `RemoteSOEM`, you need two PCs.
One of these PCs must be able to use [`SOEM`](./soem.md).
Hereby, this PC is referred to as the "server".
The other PC, which is the development PC using the SDK, has no particular restrictions as long as it is connected to the same LAN as the server. 
Hereby, this PC is referred to as the "client".

First, connect the server to the AUTD device.
Then, connect the server and client via a different LAN[^fn_remote_soem].
Next, check the IP addresses of the LAN between the server and client.
For example, let's assume the server's IP is `172.16.99.104` and the client's IP is `172.16.99.62`.

### AUTD Server

When using `RemoteSOEM`, you need to install `AUTD Server` on the server.
The installer is available on [GitHub Releases](https://github.com/shinolab/autd3-server/releases), so download it and follow the instructions to install it.

When you run `AUTD Server`, you will see a screen like the one below. Open the `SOEM` tab.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_remotesoem.jpg"/>
</figure>

Specify an appropriate port number in the port field and press the `Run` button.

If the AUTD3 device is found and a message indicating that it is waiting for a connection from the client is displayed, the setup is successful.

Note that `AUTD Server` allows you to specify options equivalent to those of [`SOEM`](./soem.md).

### APIs

In the constructor of `RemoteSOEM`, specify the <server IP:port>.

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
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/link/remote_soem_0.py}}
```
</div>

## Firewall

If you encounter TCP-related errors, it is possible that the firewall is blocking the connection.
In that case, configure the firewall to allow connections on the specified TCP/UDP port.

[^fn_remote_soem]: Wireless LAN is also acceptable.
