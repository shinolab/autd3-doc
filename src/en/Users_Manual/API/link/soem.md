# SOEM

> NOTE: This link is only available in Rust.

> NOTE: This link is distributed under the GPLv3 license.

[SOEM](https://github.com/OpenEtherCATsociety/SOEM) is an open-source EtherCAT Master library developed by volunteers.
Unlike TwinCAT, real-time performance is not guaranteed.
Therefore, it is generally recommended to use TwinCAT.
Using SOEM should be limited to unavoidable reasons or for development purposes only.
On the other hand, SOEM has the advantage of being cross-platform and simple to install.

For Windows, install [npcap](https://nmap.org/npcap/) in "**WinPcap API compatible mode**".
For Linux/macOS, no special preparation is required.

## Install

```shell
cargo add autd3-link-soem
```

## APIs

The first argument is a callback function for errors, and the second argument specifies options.

```rust
{{#include ../../../../codes/Users_Manual/link/soem_0.rs}}
```

The options that can be specified for the SOEM link are as follows.
The default values are as above.

- `buf_size`: Transmission queue buffer size. Usually, there is no need to change this.
- `ifname`: Network interface name. If empty, the network interface to which the AUTD3 device is connected is automatically selected.
- `state_check_interval`: Interval to check for errors
- `sync0_cycle`: Synchronization signal cycle
- `send_cycle`: Transmission cycle
    - `SOEM` may become unstable when connecting a large number of devices. In this case, increase the values of `sync0_cycle` and `send_cycle`. These values should be as small as possible without causing errors. The appropriate values depend on the number of connected devices. For example, for 9 devices, a value of about $1.5-\SI{2}{ms}$ should work.
- `thread_priority`: Thread priority
- `process_priority`: Process priority (Windows only) 
- `sync_tolerance`: Synchronization tolerance level. During initialization, this link waits until the system time difference of each device is below this value. If synchronization is not completed within the timeout period below, an error occurs. It is not recommended to change this value.
- `sync_timeout`: Synchronization timeout. Timeout period for the system time difference measurement above.
‐ `affinity`: CPU affinity. If `None`, it is left to the OS.