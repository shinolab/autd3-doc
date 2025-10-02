# FAQ

[[_TOC_]]

## Frequent link disconnections

- If this frequently occurs when outputting ultrasound, check if the power supply is sufficient.
   - Each device can consume up to 50W.

## Errors when using `RemoteTwinCAT` link

- It may be blocked by the firewall, so either disable the firewall or open TCP/UDP port 48898.
- Disconnect all LAN connections other than the server on the client PC.

## How to access transducer phase/amplitude data?

1. Use [`Controller::inspect`](../API/controller.md#inspect-available-only-in-rust).
1. Create your desired `Gain`. Refer to [Creating Custom Gain](../advanced/custom_gain.md).

## How to access AM modulation data?

1. Use [`Controller::inspect`](../API/controller.md#inspect-available-only-in-rust).
1. Create your desired `Modulation`. Refer to [Creating Custom Modulation](../advanced/custom_modulation.md).

## Others

- Feel free to ask questions or report bugs on [GitHub Issues](https://github.com/shinolab/autd3/issues).
