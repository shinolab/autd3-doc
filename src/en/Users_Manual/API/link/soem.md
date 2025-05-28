# SOEM

[SOEM](https://github.com/OpenEtherCATsociety/SOEM) is an open-source EtherCAT Master library developed by volunteers.
Unlike TwinCAT, real-time performance is not guaranteed.
Therefore, it is generally recommended to use TwinCAT.
Using SOEM should be limited to unavoidable reasons or for development purposes only.
On the other hand, SOEM has the advantage of being cross-platform and simple to install.

For Windows, install [npcap](https://nmap.org/npcap/) in "**WinPcap API compatible mode**".
For Linux/macOS, no special preparation is required.

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-soem
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
if(WIN32)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v33.0.0/autd3-link-soem-v33.0.0-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v33.0.0/autd3-link-soem-v33.0.0-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3-link-soem
    URL https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v33.0.0/autd3-link-soem-v33.0.0-linux-x64.tar.gz
  )
endif()
FetchContent_MakeAvailable(autd3-link-soem)
target_link_libraries(<TARGET> PRIVATE autd3::link::soem)
```
{{ #endtab }}
{{ #tab name=C# }}
```shell
dotnet add package AUTD3Sharp.Link.SOEM
```
{{ #endtab }}
{{ #tab name=Unity }}
Add `https://github.com/shinolab/AUTD3Sharp.Link.SOEM.git#upm/latest` to Unity Package Manager.
{{ #endtab }}
{{ #tab name=Python }}
```shell
pip install pyautd3_link_soem
```
{{ #endtab }}
{{ #endtabs }}

## APIs

The first argument is a callback function for errors, and the second argument specifies options.

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/soem_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/soem_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/soem_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/soem_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

The options that can be specified for the SOEM link are as follows.
The default values are as above.

- `buf_size`: Transmission queue buffer size. Usually, there is no need to change this.
- `timer_strategy`: Timer strategy
    - `StdSleep`  : Uses the standard library sleep
    - `SpinSleep` : Uses the [spin_sleep](https://docs.rs/spin_sleep/latest/spin_sleep/) crate. Combines OS native sleep (WaitableTimer on Windows) and spin loop.
    - `SpinWait`  : Uses a spin loop. High resolution but high CPU load.
- `ifname`: Network interface name. If empty, the network interface to which the AUTD3 device is connected is automatically selected.
- `state_check_interval`: Interval to check for errors
- `sync0_cycle`: Synchronization signal cycle
- `send_cycle`: Transmission cycle
    - `SOEM` may become unstable when connecting a large number of devices. In this case, increase the values of `sync0_cycle` and `send_cycle`. These values should be as small as possible without causing errors. The appropriate values depend on the number of connected devices. For example, for 9 devices, a value of about $1.5-\SI{2}{ms}$ should work.
- `thread_priority`: Thread priority
- `process_priority`: Process priority (Windows only) 
- `sync_tolerance`: Synchronization tolerance level. During initialization, this link waits until the system time difference of each device is below this value. If synchronization is not completed within the timeout period below, an error occurs. It is not recommended to change this value.
- `sync_timeout`: Synchronization timeout. Timeout period for the system time difference measurement above.
