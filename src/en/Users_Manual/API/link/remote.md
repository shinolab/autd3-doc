# Remote

Remote link is used to connect to a [remote server](../../advanced/remote_server.md) or an [AUTD simulator](../../Simulator/simulator.md).

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-remote
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::remote)
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

## APIs

In the constructor of `Remote`, specify the ip address and port number of the server.
You can also specify the timeout as an option.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/remote_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/remote_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/remote_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/remote_0.py}}
```
{{ #endtab }}
{{ #endtabs }}
