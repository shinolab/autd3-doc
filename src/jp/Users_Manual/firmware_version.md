# Firmware version

本ソフトウェアは以下のファームウェアをサポートしている.

バージョンごとの差は以下の表を参照されたい.

|                                                        | v10.0.0                       | v11.0.0            | v12.0.0          |
|--------------------------------------------------------|-------------------------------|--------------------|------------------|
| [Modulation](./API/modulation.md)の最大バッファサイズ  | 32768                         | 65536              | 65536            |
| [FociSTM](./API/stm/focus.md)の最大パターン数          | 焦点数によらず8192パターン    | 総焦点数が65536    | 総焦点数が65536  |
| [PulseWidthEncoder](./API/pulse_width_encoder.md)      | ✅️ (Rust版のみ)               | ✅️                | ✅️              |
| [GPIOOutputType::SysTime](./API/gpio_out.md)           | ❌️                            | ✅️                | ✅️              |
| [GPIOOutputType::SyncDiff](./API/gpio_out.md)          | ❌️                            | ❌️                | ✅️              |
