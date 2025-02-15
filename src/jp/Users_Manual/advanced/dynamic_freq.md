# 超音波周波数の変更

Rust版のライブラリでは, 超音波周波数を変更することができる.

## インストール

### Firmware

超音波周波数を変更する場合, 特殊なファームウェアを使用する必要がある.

```
git clone https://github.com/shinolab/autd3-firmware
cd autd3-firmware
pwsh autd_firmware_writer.ps1 --version 10.0.1-dynamic_freq
```

### Software

`autd3` crateの`dynamic_freq` featureを有効にする.

## 使い方

超音波周波数を変更する場合は, 環境変数`AUTD3_ULTRASOUND_FREQ`にHz単位の周波数を整数で設定すれば良い.
この周波数は125Hzの倍数である必要がある.

## 注意点

- サンプリング周波数等は超音波の周波数を分周しているため, 超音波の周波数によっては設定できないサンプリング周波数が存在する.
- 周期に関連する関数は使用できない.
- `autd3-emulator`は周波数の変更をサポートしていない.
