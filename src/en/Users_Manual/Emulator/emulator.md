# Emulator

By using the `Emulator`, you can perform more detailed calculations of output phase/pulse width, output voltage, output sound wave, and sound field compared to the `Simulator`.

> NOTE: Currently, the `Emulator` is only available in Rust and Python.
> There are no plans to port it to C++ or C#.

[[_TOC_]]

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```rust,name=shell
cargo add autd3-emulator
```
{{ #endtab }}
{{ #tab name=Python }}
```python,name=shell
pip install pyautd3_emulator
```
{{ #endtab }}
{{ #endtabs }}

## APIs
The data output by the `Emulator` is a Polars DataFrame.
For more details, please refer to the [Polars documentation](https://pola.rs/).

### Transducer Table

Displays a list of transducers.

Each column contains the device index, the (local) index of the transducer, position, and axial direction.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_trans_table.rs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_trans_table.py}}
```
{{ #endtab }}
{{ #endtabs }}

```
┌─────────┬────────┬────────────┬────────────┬───────┬─────┬─────┬─────┐
│ dev_idx ┆ tr_idx ┆ x[mm]      ┆ y[mm]      ┆ z[mm] ┆ nx  ┆ ny  ┆ nz  │
│ ---     ┆ ---    ┆ ---        ┆ ---        ┆ ---   ┆ --- ┆ --- ┆ --- │
│ u16     ┆ u8     ┆ f32        ┆ f32        ┆ f32   ┆ f32 ┆ f32 ┆ f32 │
╞═════════╪════════╪════════════╪════════════╪═══════╪═════╪═════╪═════╡
│ 0       ┆ 0      ┆ 0.0        ┆ 0.0        ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 1      ┆ 10.16      ┆ 0.0        ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 2      ┆ 20.32      ┆ 0.0        ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 3      ┆ 30.48      ┆ 0.0        ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 4      ┆ 40.639999  ┆ 0.0        ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ …       ┆ …      ┆ …          ┆ …          ┆ …     ┆ …   ┆ …   ┆ …   │
│ 0       ┆ 244    ┆ 132.080002 ┆ 132.080002 ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 245    ┆ 142.23999  ┆ 132.080002 ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 246    ┆ 152.399994 ┆ 132.080002 ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 247    ┆ 162.559998 ┆ 132.080002 ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
│ 0       ┆ 248    ┆ 172.720001 ┆ 132.080002 ┆ 0.0   ┆ 0.0 ┆ 0.0 ┆ 1.0 │
└─────────┴────────┴────────────┴────────────┴───────┴─────┴─────┴─────┘
```

### Calculation of Output Phase/Pulse Width

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_drive.rs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_drive.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: The time interval specified by `tick` must be a multiple of $\SI{25}{us}$.

At each time ($\SI{25}{us}$ unit), the phase/pulse width is stored in each column.
Each column name is `<phase/pulse_width>@<time>[ns]`.

Each row corresponds to the rows in the [Transducer Table](#transducer-table).

```
┌─────────────┬────────────────┬────────────────┬────────────────┬───┬────────────────┬───────────────┬───────────────┬───────────────┐
│ phase@0[ns] ┆ phase@25000[ns ┆ phase@50000[ns ┆ phase@75000[ns ┆ … ┆ phase@9900000[ ┆ phase@9925000 ┆ phase@9950000 ┆ phase@9975000 │
│ ---         ┆ ]              ┆ ]              ┆ ]              ┆   ┆ ns]            ┆ [ns]          ┆ [ns]          ┆ [ns]          │
│ u8          ┆ ---            ┆ ---            ┆ ---            ┆   ┆ ---            ┆ ---           ┆ ---           ┆ ---           │
│             ┆ u8             ┆ u8             ┆ u8             ┆   ┆ u8             ┆ u8            ┆ u8            ┆ u8            │
╞═════════════╪════════════════╪════════════════╪════════════════╪═══╪════════════════╪═══════════════╪═══════════════╪═══════════════╡
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ …           ┆ …              ┆ …              ┆ …              ┆ … ┆ …              ┆ …             ┆ …             ┆ …             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
│ 0           ┆ 0              ┆ 0              ┆ 0              ┆ … ┆ 0              ┆ 0             ┆ 0             ┆ 0             │
└─────────────┴────────────────┴────────────────┴────────────────┴───┴────────────────┴───────────────┴───────────────┴───────────────┘
```


```
┌───────────────────┬───────────────────────┬───────────────────────┬───────────────────────┬───┬─────────────────────────┬─────────────────────────┬────────────────────────┬────────────────────────┐
│ pulse_width@0[ns] ┆ pulse_width@25000[ns] ┆ pulse_width@50000[ns] ┆ pulse_width@75000[ns] ┆ … ┆ pulse_width@9900000[ns] ┆ pulse_width@9925000[ns] ┆ pulse_width@9950000[ns ┆ pulse_width@9975000[ns │
│ ---               ┆ ---                   ┆ ---                   ┆ ---                   ┆   ┆ ---                     ┆ ---                     ┆ ]                      ┆ ]                      │
│ u16               ┆ u16                   ┆ u16                   ┆ u16                   ┆   ┆ u16                     ┆ u16                     ┆ ---                    ┆ ---                    │
│                   ┆                       ┆                       ┆                       ┆   ┆                         ┆                         ┆ u16                    ┆ u16                    │
╞═══════════════════╪═══════════════════════╪═══════════════════════╪═══════════════════════╪═══╪═════════════════════════╪═════════════════════════╪════════════════════════╪════════════════════════╡
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ …                 ┆ …                     ┆ …                     ┆ …                     ┆ … ┆ …                       ┆ …                       ┆ …                      ┆ …                      │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
│ 8                 ┆ 16                    ┆ 24                    ┆ 33                    ┆ … ┆ 50                      ┆ 53                      ┆ 55                     ┆ 57                     │
└───────────────────┴───────────────────────┴───────────────────────┴───────────────────────┴───┴─────────────────────────┴─────────────────────────┴────────────────────────┴────────────────────────┘
```
### Output Voltage

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_voltage.rs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_voltage.py}}
```
{{ #endtab }}
{{ #endtabs }}

The output voltage at each time ($\SI{25}{us}/512$ unit) is stored in each column.
Each column name is `voltage[V]@<time>[25us/512]`.

Each row corresponds to the rows in the [Transducer Table](#transducer-table).

```
┌────────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┬───┬────────────────────────────┬────────────────────────────┬────────────────────────────┬────────────────────────────┐
│ voltage[V]@0[25us/512] ┆ voltage[V]@1[25us/512] ┆ voltage[V]@2[25us/512] ┆ voltage[V]@3[25us/512] ┆ … ┆ voltage[V]@20476[25us/512] ┆ voltage[V]@20477[25us/512] ┆ voltage[V]@20478[25us/512] ┆ voltage[V]@20479[25us/512] │
│ ---                    ┆ ---                    ┆ ---                    ┆ ---                    ┆   ┆ ---                        ┆ ---                        ┆ ---                        ┆ ---                        │
│ f32                    ┆ f32                    ┆ f32                    ┆ f32                    ┆   ┆ f32                        ┆ f32                        ┆ f32                        ┆ f32                        │
╞════════════════════════╪════════════════════════╪════════════════════════╪════════════════════════╪═══╪════════════════════════════╪════════════════════════════╪════════════════════════════╪════════════════════════════╡
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ …                      ┆ …                      ┆ …                      ┆ …                      ┆ … ┆ …                          ┆ …                          ┆ …                          ┆ …                          │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
│ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ 12.0                   ┆ … ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      ┆ -12.0                      │
└────────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┴───┴────────────────────────────┴────────────────────────────┴────────────────────────────┴────────────────────────────┘
```
### Output Sound Pressure

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_ultrasound.rs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_ultrasound.py}}
```
{{ #endtab }}
{{ #endtabs }}

The normalized output sound pressure at each time ($\SI{25}{us}/512$ unit) is stored in each column.
Each column name is `p[a.u.]@<time>[25us/512]`.

Each row corresponds to the rows in the [Transducer Table](#transducer-table).

```
┌─────────────────────┬─────────────────────┬─────────────────────┬─────────────────────┬───┬─────────────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ p[a.u.]@0[25us/512] ┆ p[a.u.]@1[25us/512] ┆ p[a.u.]@2[25us/512] ┆ p[a.u.]@3[25us/512] ┆ … ┆ p[a.u.]@20476[25us/512] ┆ p[a.u.]@20477[25us/512] ┆ p[a.u.]@20478[25us/512] ┆ p[a.u.]@20479[25us/512] │
│ ---                 ┆ ---                 ┆ ---                 ┆ ---                 ┆   ┆ ---                     ┆ ---                     ┆ ---                     ┆ ---                     │
│ f32                 ┆ f32                 ┆ f32                 ┆ f32                 ┆   ┆ f32                     ┆ f32                     ┆ f32                     ┆ f32                     │
╞═════════════════════╪═════════════════════╪═════════════════════╪═════════════════════╪═══╪═════════════════════════╪═════════════════════════╪═════════════════════════╪═════════════════════════╡
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ …                   ┆ …                   ┆ …                   ┆ …                   ┆ … ┆ …                       ┆ …                       ┆ …                       ┆ …                       │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
│ 0.0                 ┆ -0.000272           ┆ -0.000481           ┆ -0.000618           ┆ … ┆ -0.36185                ┆ -0.350698               ┆ -0.339501               ┆ -0.328258               │
└─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┴───┴─────────────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Calculation of Sound Field (Instantaneous Value)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_field.rs}}
```
>NOTE: The `gpu` option is only available if the `gpu` feature is enabled.</p>
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_field.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: In Rust, besides `RangeXYZ`, you can use `RangeZXY`, `RangeXY` for 2D, `RangeX` for 1D and so on, or `Vec<Vector3>` to specify arbitrary points.
> In Python, only `RangeXYZ` is available.

Enabling the `print_progress` option will display the calculation progress.
Enabling the `gpu` option will execute the calculation on the GPU.

Due to the potential for high memory consumption, the `next` function is used to retrieve only specific times.
The `skip` function can be used to skip a specified amount of time.

The output sound pressure at each observation point is stored in each column in chronological order (unit specified by `time_step`).
Each column name is `p[Pa]@<time>[ns]`.
Each row corresponds to the observation points obtained with `observe_points`.

```
┌────────────┬───────────┬───────┐
│ x[mm]      ┆ y[mm]     ┆ z[mm] │
│ ---        ┆ ---       ┆ ---   │
│ f32        ┆ f32       ┆ f32   │
╞════════════╪═══════════╪═══════╡
│ 66.625267  ┆ 46.713196 ┆ 150.0 │
│ 67.625267  ┆ 46.713196 ┆ 150.0 │
│ 68.625267  ┆ 46.713196 ┆ 150.0 │
│ 69.625267  ┆ 46.713196 ┆ 150.0 │
│ 70.625267  ┆ 46.713196 ┆ 150.0 │
│ …          ┆ …         ┆ …     │
│ 102.625267 ┆ 86.713196 ┆ 150.0 │
│ 103.625267 ┆ 86.713196 ┆ 150.0 │
│ 104.625267 ┆ 86.713196 ┆ 150.0 │
│ 105.625267 ┆ 86.713196 ┆ 150.0 │
│ 106.625267 ┆ 86.713196 ┆ 150.0 │
└────────────┴───────────┴───────┘
```

```
┌──────────────────┬──────────────────┬──────────────────┬──────────────────┬───┬──────────────────┬──────────────────┬──────────────────┬──────────────────┐
│ p[Pa]@500000[ns] ┆ p[Pa]@501000[ns] ┆ p[Pa]@502000[ns] ┆ p[Pa]@503000[ns] ┆ … ┆ p[Pa]@996000[ns] ┆ p[Pa]@997000[ns] ┆ p[Pa]@998000[ns] ┆ p[Pa]@999000[ns] │
│ ---              ┆ ---              ┆ ---              ┆ ---              ┆   ┆ ---              ┆ ---              ┆ ---              ┆ ---              │
│ f32              ┆ f32              ┆ f32              ┆ f32              ┆   ┆ f32              ┆ f32              ┆ f32              ┆ f32              │
╞══════════════════╪══════════════════╪══════════════════╪══════════════════╪═══╪══════════════════╪══════════════════╪══════════════════╪══════════════════╡
│ 22.249609        ┆ 14.994699        ┆ 11.20509         ┆ 3.416157         ┆ … ┆ 167.468948       ┆ 143.434677       ┆ 115.029839       ┆ 78.702179        │
│ 22.973528        ┆ 17.704706        ┆ 14.598668        ┆ 6.462077         ┆ … ┆ 128.688828       ┆ 102.245392       ┆ 73.068733        ┆ 39.29715         │
│ 23.043713        ┆ 20.534163        ┆ 15.762163        ┆ 9.015405         ┆ … ┆ 72.13736         ┆ 50.06559         ┆ 25.516897        ┆ -1.414132        │
│ 21.61729         ┆ 19.986338        ┆ 16.669203        ┆ 11.957072        ┆ … ┆ 6.599095         ┆ -8.152014        ┆ -22.183277       ┆ -34.678905       │
│ 17.479811        ┆ 18.30769         ┆ 16.697689        ┆ 12.929367        ┆ … ┆ -61.525105       ┆ -64.023788       ┆ -62.711498       ┆ -56.925694       │
│ …                ┆ …                ┆ …                ┆ …                ┆ … ┆ …                ┆ …                ┆ …                ┆ …                │
│ 14.888723        ┆ 14.758762        ┆ 13.289121        ┆ 9.737269         ┆ … ┆ -73.181961       ┆ -85.114655       ┆ -92.114983       ┆ -93.623962       │
│ 17.559294        ┆ 15.889968        ┆ 12.346513        ┆ 7.979947         ┆ … ┆ -28.419638       ┆ -61.184322       ┆ -90.326851       ┆ -113.895905      │
│ 18.171673        ┆ 15.26449         ┆ 10.946121        ┆ 5.410897         ┆ … ┆ 19.804182        ┆ -28.594215       ┆ -73.595749       ┆ -115.230705      │
│ 18.815191        ┆ 12.321008        ┆ 7.800498         ┆ 3.680776         ┆ … ┆ 65.869225        ┆ 9.351333         ┆ -48.561874       ┆ -98.87677        │
│ 16.717573        ┆ 10.482997        ┆ 4.044011         ┆ 0.89806          ┆ … ┆ 102.099556       ┆ 44.310383        ┆ -16.616224       ┆ -70.65287        │
└──────────────────┴──────────────────┴──────────────────┴──────────────────┴───┴──────────────────┴──────────────────┴──────────────────┴──────────────────┘
```
### Calculation of Sound Field (RMS)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_rms.rs}}
```
>NOTE: The `gpu` option is only available if the `gpu` feature is enabled.</p>
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_rms.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: The time must advance by at least $\SI{25}{us}$.

> NOTE: The values calculated by RMS are **not the RMS of the instantaneous sound field above**. They are a linear superposition that ignores propagation delays and transducer responses.

The RMS of the output sound pressure at each observation point is stored in each column in chronological order (unit is $\SI{25}{us}$).
Each column name is `rms[Pa]@<time>[ns]`.
Each row corresponds to the observation points obtained with `observe_points`.

```
┌────────────┬───────────┬───────┐
│ x[mm]      ┆ y[mm]     ┆ z[mm] │
│ ---        ┆ ---       ┆ ---   │
│ f32        ┆ f32       ┆ f32   │
╞════════════╪═══════════╪═══════╡
│ 66.625267  ┆ 46.713196 ┆ 150.0 │
│ 67.625267  ┆ 46.713196 ┆ 150.0 │
│ 68.625267  ┆ 46.713196 ┆ 150.0 │
│ 69.625267  ┆ 46.713196 ┆ 150.0 │
│ 70.625267  ┆ 46.713196 ┆ 150.0 │
│ …          ┆ …         ┆ …     │
│ 102.625267 ┆ 86.713196 ┆ 150.0 │
│ 103.625267 ┆ 86.713196 ┆ 150.0 │
│ 104.625267 ┆ 86.713196 ┆ 150.0 │
│ 105.625267 ┆ 86.713196 ┆ 150.0 │
│ 106.625267 ┆ 86.713196 ┆ 150.0 │
└────────────┴───────────┴───────┘
```

```
┌───────────────┐
│ rms[Pa]@0[ns] │
│ ---           │
│ f32           │
╞═══════════════╡
│ 97.675339     │
│ 83.525314     │
│ 60.54364      │
│ 34.229084     │
│ 33.827206     │
│ …             │
│ 51.324219     │
│ 75.84668      │
│ 102.852501    │
│ 120.575188    │
│ 125.698715    │
└───────────────┘
```

For more examples, please refer to [autd3-emulator (Rust)](https://github.com/shinolab/autd3-emulator/tree/main/examples) and [pyautd3 (Python)](https://github.com/shinolab/pyautd3/tree/main/example/emulator).
