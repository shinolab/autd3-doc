# Simulator

The Simulator link is used when using the [AUTD Simulator](../../Simulator/simulator.md).

Before using this link, you need to start the AUTD Simulator.

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
cargo add autd3-link-simulator --features blocking
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::simulator)
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

## APIs

In the constructor of `Simulator`, specify the IP address and port number of the AUTD Simulator.

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
{{#include ../../../../codes/Users_Manual/link/simulator_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/link/simulator_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/link/simulator_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/link/simulator_0.py}}
```
</div>
