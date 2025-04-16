# Firmware v10 vs v11

This software supports the following firmware versions. 
However, when using firmware v10.0.1, some features are not supported.

Refer to the table below for details.

|                                | v10.0.1                                                         | v11.0.0                                                  | 
| ------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------- | 
| Maximum buffer size of [Modulation](./API/modulation.md)       | 32768                                                           | 65536                                                    | 
| Maximum number of patterns for [FociSTM](./API/stm/focus.md)   | 8192 patterns regardless of the number of foci<br>e.g., $1\times 8192$, $2\times 8192$, ..., $8\times 8192$ | Total number of foci is 65536<br>e.g., $1\times 65536$, $2\times 32768$, ..., $8\times 8192$ | 
| [PulseWidthEncoder](./API/pulse_width_encoder.md)              | Supported (Rust version only)                                                  | Supported                                                | 
| [GPIOOutputType::SysTime](./API/gpio_out.md)                   | Not supported                                                  | Supported                                                | 
| Estimated power consumption of FPGA                            | $\SI{367}{mW}$                                                 | $\SI{456}{mW}$                                           |
