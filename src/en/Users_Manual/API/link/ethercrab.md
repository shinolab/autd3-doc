# EtherCrab

> NOTE: If TwinCAT is available, we generally recommend using TwinCAT.

This link uses [EtherCrab](https://github.com/ethercrab-rs/ethercrab), an open-source EtherCAT master library.

On Windows, install [npcap](https://nmap.org/npcap/) in "WinPcap API compatible mode".
On Linux/macOS, no additional setup is required.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-ethercrab
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::ethercrab)
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

Pass the error callback function as the first argument, and options as the second argument.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/ethercrab_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

The options available for the `EtherCrab` link are as follows. Default values are as shown above.

- `ifname`: Network interface name. If `None`, the network interface to which the AUTD3 devices are connected is selected automatically.
- `state_check_period`: Interval at which to check for errors.
- `sync0_period`: Period of the SYNC0 signal.
	- When connecting a large number of devices, behavior may become unstable. In that case, increase `sync0_period`. These values should be as small as possible without causing errors. The appropriate values depend on the number of connected units.
- `sync_tolerance`: Synchronization tolerance. During initialization, the system waits until the difference in system time among devices falls below this value. If synchronization is not achieved within the timeout below, an error occurs. Changing this value is NOT recommended.
- `sync_timeout`: Synchronization timeout. Timeout for the system time difference measurement described above.
