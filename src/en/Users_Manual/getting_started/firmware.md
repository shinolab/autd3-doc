# Firmware

To update the firmware, you need a Windows 10/11 64bit PC with [Vivado](https://www.xilinx.com/products/design-tools/vivado.html) and [J-Link Software](https://www.segger.com/downloads/jlink/) installed.
We tested with Vivado 2025.1 and J-Link Software v8.10.

> NOTE: If the sole purpose is to update the firmware, it is strongly recommended to use "**Vivado Lab Edition**".
> ML Edition requires more than 60 GB of disk space for installation. Lab Edition requires about 6 GB of disk space.

> NOTE: When using an old J-Link device, check "**Install legacy USB Driver for J-Link**".
> For example, J-Link Plus V10 and earlier require a legacy USB Driver. (The version is written on the back of the J-Link Plus device.)
> For more details, refer to the [Segger Wiki](https://wiki.segger.com/J-Link_Model_Overview). If the device you are using has the WinUSB feature, the legacy USB Driver is not required.

First, connect the AUTD3 device and the PC with a [XILINX Platform Cable](https://www.xilinx.com/products/boards-and-kits/hw-usb-ii-g.html) and a [J-Link 9-Pin Cortex-M Adapter](https://www.segger-pocjapan.com/j-link-9-pin-cortex-m-adapter) attached to a [J-Link Plus](https://www.segger.com/products/debug-probes/j-link/models/j-link-plus/), and turn on the power of the AUTD3.
Next, execute `autd_firmware_writer.ps1` in the [autd3-firmware](https://github.com/shinolab/autd3-firmware) from PowerShell and follow the instructions. The update takes a few minutes.

```shell
git clone https://github.com/shinolab/autd3-firmware
cd autd3-firmware
pwsh autd_firmware_writer.ps1
```

<figure>
    <img src="../../fig/Users_Manual/cable.jpg"/>
    <figcaption>Firmware update cable connection</figcaption>
</figure>
