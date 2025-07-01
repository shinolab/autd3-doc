# Firmware v10 vs v11

This software supports the following firmware versions. 

Refer to the table below for differences between versions.

|                                                              | v10.0.0                                        | v11.0.0                       | v12.0.0                       | v12.1.0                       |
|--------------------------------------------------------------|------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|
| Maximum buffer size of [Modulation](./API/modulation.md)     | 32768                                          | 65536                         | 65536                         | 65536                         |
| Maximum number of patterns for [FociSTM](./API/stm/focus.md) | 8192 patterns regardless of the number of foci | Total number of foci is 65536 | Total number of foci is 65536 | Total number of foci is 65536 |
| [PulseWidthEncoder](./API/pulse_width_encoder.md)            | Supported (Rust version only)                  | Supported                     | Supported                     | Supported                     |
| [GPIOOutputType::SysTime](./API/gpio_out.md)                 | Not supported                                  | Supported                     | Supported                     | Supported                     |
| [GPIOOutputType::SyncDiff](./API/gpio_out.md)                | Not supported                                  | Not supported                 | Supported                     | Supported                     |
| [OutputMask](./API/output_mask.md)                           | Not supported                                  | Not supported                 | Supported                     | Supported                     |
