# SOEM

[SOEM](https://github.com/OpenEtherCATsociety/SOEM) is an open-source EtherCAT Master library developed by volunteers.
Unlike TwinCAT, real-time performance is not guaranteed.
Therefore, it is generally recommended to use TwinCAT.
Using SOEM should be limited to unavoidable reasons or for development purposes only.
On the other hand, SOEM has the advantage of being cross-platform and simple to install.

For Windows, install [npcap](https://nmap.org/npcap/) in "**WinPcap API compatible mode**".
For Linux/macOS, no special preparation is required.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5 for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-link-soem
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

## APIs

The first argument is a callback function for errors, and the second argument specifies options.

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
{{#include ../../../../codes/Users_Manual/link/soem_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/link/soem_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/link/soem_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/link/soem_0.py}}
```
</div>

The options that can be specified for the SOEM link are as follows.
The default values are as above.

- `buf_size`: Transmission queue buffer size. Usually, there is no need to change this.
- `timer_strategy`: Timer strategy
    - `StdSleep`  : Uses the standard library sleep
    - `SpinSleep` : Uses the [spin_sleep](https://docs.rs/spin_sleep/latest/spin_sleep/) crate. Combines OS native sleep (WaitableTimer on Windows) and spin loop.
    - `SpinWait`  : Uses a spin loop. High resolution but high CPU load.
- `sync_mode`: Synchronization mode
- `ifname`: Network interface name. If empty, the network interface to which the AUTD3 device is connected is automatically selected.
- `state_check_interval`: Interval to check for errors
- `sync0_cycle`: Synchronization signal cycle
- `send_cycle`: Transmission cycle
    - `SOEM` may become unstable when connecting a large number of devices. In this case, increase the values of `sync0_cycle` and `send_cycle`. These values should be as small as possible without causing errors. The appropriate values depend on the number of connected devices. For example, for 9 devices, a value of about $1.5-\SI{2}{ms}$ should work.
- `thread_priority`: Thread priority
- `process_priority`: Process priority (Windows only) 
- `sync_tolerance`: Synchronization tolerance level. During initialization, this link waits until the system time difference of each device is below this value. If synchronization is not completed within the timeout period below, an error occurs. It is not recommended to change this value.
- `sync_timeout`: Synchronization timeout. Timeout period for the system time difference measurement above.
