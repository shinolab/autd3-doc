# Single Device

This section explains how to drive a single device.

## Installing Dependencies

This tutorial uses [SOEM](https://github.com/OpenEtherCATsociety/SOEM).
If you are using Windows, install [Npcap](https://npcap.com/) in "**WinPcap API-compatible Mode**".

Note that if the firmware is outdated, proper operation is not guaranteed.
The firmware version assumed in this document is v11.0.0 or v10.0.1[^1].
Refer to [Getting Started/Firmware](../getting_started/firmware.md) for firmware updates.

## Sample Programs

{{ #tabs }}
{{ #tab name=Rust }}
{{#include rust.md}}
{{ #endtab }}
{{ #tab name=C++ }}
{{#include cpp.md}}
{{ #endtab }}
{{ #tab name=C# }}
{{#include cs.md}}
{{ #endtab }}
{{ #tab name=Python }}
{{#include python.md}}
{{ #endtab }}
{{ #endtabs }}

[^1]: Some features are not supported. See [Firmware v10 vs v11](./../firmware_v10_vs_v11.md) for details.
