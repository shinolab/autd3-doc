# Firmware v10 vs v11

本ソフトウェアは以下のファームウェアをサポートしている.
ただし, ファームウェアv10.0.1を使用する場合, 一部機能は未サポートである.

詳細は以下の表を参照されたい.

|                                | v10.0.1                                                         | v11.0.0                                                  | 
| ------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------- | 
| [Modulation](./API/modulation.md)の最大バッファサイズ | 32768[^1]                                                           | 65536                                                    | 
| [FociSTM](./API/stm/focus.md)の最大パターン数        | 焦点数によらず8192パターン[^1]<br>e.g., $1\times 8192$, $2\times 8192$, ..., $8\times 8192$ | 総焦点数が65536点<br>e.g., $1\times 65536$, $2\times 32768$, ..., $8\times 8192$ | 
| [PulseWidthEncoder](./API/pulse_width_encoder.md)              | サポートしている (Rust版のみ)                                              | サポートしている                                         | 
| [GPIOOutputType::SysTime](./API/gpio_out.md)        | サポートしていない[^2]                                              | サポートしている                                         | 
| FPGAの推定消費電力             | $\SI{367}{mW}$                                                           | $\SI{456}{mW}$                                                    | 

[^1]: 範囲外のデータを使用した場合は, エラーにはならず単に上書きされるような動作になることに注意.
[^2]: エラーにはならないが, 正常に動作しない.
