# Changing Ultrasound Frequency

The Rust library allows you to change the ultrasound frequency.

## Installation

### Firmware

To change the ultrasound frequency, you need to use special firmware.

```
git clone https://github.com/shinolab/autd3-firmware
cd autd3-firmware
pwsh autd_firmware_writer.ps1 --version 10.0.1-dynamic_freq
```

### Software

Enable the `dynamic_freq` feature of the `autd3` crate.

## Usage

To change the ultrasound frequency, set the environment variable `AUTD3_ULTRASOUND_FREQ` to the frequency in Hz as an integer.
This frequency must be a multiple of 125Hz.

## Notes

- Since the sampling frequency is divided by the ultrasound frequency, there are sampling frequencies that cannot be set depending on the ultrasound frequency.
- Functions related to the period cannot be used.
- `autd3-emulator` does not support frequency changes.
