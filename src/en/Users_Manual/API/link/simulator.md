# Simulator

The Simulator link is used when using the [AUTD Simulator](../../Simulator/simulator.md).

Before using this link, you need to start the AUTD Simulator.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-simulator --features blocking
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::simulator)
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

In the constructor of `Simulator`, specify the IP address and port number of the AUTD Simulator.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/simulator_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/simulator_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/simulator_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/simulator_0.py}}
```
{{ #endtab }}
{{ #endtabs }}
