# FAQ

[[_TOC_]]

## "No AUTD3 devices found" is displayed

- When using `link::SOEM` on macOS or Linux, root privileges are required.

   - On Linux, this can be avoided by setting the following permissions with the `setcap` command:
   
      ```shell
      sudo setcap cap_net_raw,cap_net_admin=eip <your executable file>
      ```

   - On macOS, this can be avoided by adding read permissions to the `/dev/bpf*` files:
   
      ```shell
      sudo chmod +r /dev/bpf*
      ```

- (Windows) Use the latest npcap.

- Virtual machines like WSL are not supported.
   - It may work on VirtualBox, but the behavior is unstable.

## "One or more slaves are not responding" or "Slow network was detected" is displayed

- Update the driver.
   - If using Realtek on Windows, install the driver labeled `Win10 Auto Installation Program (NDIS)` from the [official site](https://www.realtek.com/en/component/zoo/category/network-interface-controllers-10-100-1000m-gigabit-ethernet-pci-express-software) (also for Windows 11).

- (Windows) Use the latest npcap.

- Increase the values of `send_cycle` and `sync0_cycle`.

- (Windows) From the properties of the relevant network adapter in Device Manager, uncheck "Allow the computer to turn off this device to save power" in the "Power Management" tab.

## Frequent transmission failures when using `link::SOEM`

- This issue occurs when:
   * `sync_mode` is set to `DC`

   and,

   * The onboard ethernet interface is used

  and, it has been confirmed to occur in the following situations:

   * Using RealSense, Azure Kinect, Web cameras, etc.
      * Generally occurs when the camera is activated.
   * Playing videos or audio
      * Or opening video sites (like YouTube) in an internet browser.
   * Using Unity
      * Occurs just by launching it.
   * Playing animations in Blender
      * Other operations (like modeling) are fine.

- To avoid this issue, try one of the following:
  1. Set `sync_mode` to `FreeRun`.
  1. Use Linux or macOS.
     - However, virtual machines are not acceptable.
  1. Use `TwinCAT`, `RemoteTwinCAT`, or `RemoteSOEM` links.
  1. Use a USB to Ethernet adapter.
     - It has been confirmed to work properly with at least the "ASIX AX88179" chip.
     - Note that this issue can occur with PCIe-connected ethernet adapters as well, not just onboard ones.

- If this issue occurs in situations other than those listed above, or if it does not occur in the listed situations, please actively report it on GitHub Issues.

## Frequent link disconnections

- If this frequently occurs when outputting ultrasound, check if the power supply is sufficient.
   - Each device can consume up to 50W.

## Errors when using `RemoteTwinCAT` link

- It may be blocked by the firewall, so either disable the firewall or open TCP/UDP port 48898.
- Disconnect all LAN connections other than the server on the client PC.

## How to access transducer phase/amplitude data?

1. Create your desired `Gain`. Refer to [Creating Custom Gain](../advanced/custom_gain.md).

## How to access AM modulation data?

1. Create your desired `Modulation`. Refer to [Creating Custom Modulation](../advanced/custom_modulation.md).

## Others

- Feel free to ask questions or report bugs on [GitHub Issues](https://github.com/shinolab/autd3/issues).
