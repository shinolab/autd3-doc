# Remote

Remote linkは[リモートサーバ](../../advanced/remote_server.md), あるいは, [AUTDシミュレータ](../../Simulator/simulator.md)に接続する際に使うLinkである.

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
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Unity }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Python }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #endtabs }}

## APIs

`Remote`のコンストラクタにはサーバのIPアドレスとポート番号を指定する.
オプションでタイムアウトを指定できる.

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
