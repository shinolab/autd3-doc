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
┌────────────────┬────────────────┬───────────────┬───────────────┬───┬───────────────┬───────────────┬───────────────┬───────────────┐
│ pulse_width@0[ ┆ pulse_width@25 ┆ pulse_width@5 ┆ pulse_width@7 ┆ … ┆ pulse_width@9 ┆ pulse_width@9 ┆ pulse_width@9 ┆ pulse_width@9 │
│ ns]            ┆ 000[ns]        ┆ 0000[ns]      ┆ 5000[ns]      ┆   ┆ 900000[ns]    ┆ 925000[ns]    ┆ 950000[ns]    ┆ 975000[ns]    │
│ ---            ┆ ---            ┆ ---           ┆ ---           ┆   ┆ ---           ┆ ---           ┆ ---           ┆ ---           │
│ u8             ┆ u8             ┆ u8            ┆ u8            ┆   ┆ u8            ┆ u8            ┆ u8            ┆ u8            │
╞════════════════╪════════════════╪═══════════════╪═══════════════╪═══╪═══════════════╪═══════════════╪═══════════════╪═══════════════╡
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ …              ┆ …              ┆ …             ┆ …             ┆ … ┆ …             ┆ …             ┆ …             ┆ …             │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
│ 4              ┆ 8              ┆ 12            ┆ 16            ┆ … ┆ 25            ┆ 26            ┆ 27            ┆ 29            │
└────────────────┴────────────────┴───────────────┴───────────────┴───┴───────────────┴───────────────┴───────────────┴───────────────┘
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

The output voltage at each time ($\SI{25}{us}/256$ unit) is stored in each column.
Each column name is `voltage[V]@<time>[25us/256]`.

Each row corresponds to the rows in the [Transducer Table](#transducer-table).

```
┌────────────────┬────────────────┬───────────────┬───────────────┬───┬───────────────┬───────────────┬───────────────┬───────────────┐
│ voltage[V]@0[2 ┆ voltage[V]@1[2 ┆ voltage[V]@2[ ┆ voltage[V]@3[ ┆ … ┆ voltage[V]@10 ┆ voltage[V]@10 ┆ voltage[V]@10 ┆ voltage[V]@10 │
│ 5us/256]       ┆ 5us/256]       ┆ 25us/256]     ┆ 25us/256]     ┆   ┆ 236[25us/256] ┆ 237[25us/256] ┆ 238[25us/256] ┆ 239[25us/256] │
│ ---            ┆ ---            ┆ ---           ┆ ---           ┆   ┆ ---           ┆ ---           ┆ ---           ┆ ---           │
│ f32            ┆ f32            ┆ f32           ┆ f32           ┆   ┆ f32           ┆ f32           ┆ f32           ┆ f32           │
╞════════════════╪════════════════╪═══════════════╪═══════════════╪═══╪═══════════════╪═══════════════╪═══════════════╪═══════════════╡
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ …              ┆ …              ┆ …             ┆ …             ┆ … ┆ …             ┆ …             ┆ …             ┆ …             │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
│ 12.0           ┆ 12.0           ┆ 12.0          ┆ 12.0          ┆ … ┆ -12.0         ┆ -12.0         ┆ -12.0         ┆ -12.0         │
└────────────────┴────────────────┴───────────────┴───────────────┴───┴───────────────┴───────────────┴───────────────┴───────────────┘
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

The normalized output sound pressure at each time ($\SI{25}{us}/256$ unit) is stored in each column.
Each column name is `p[a.u.]@<time>[25us/256]`.

Each row corresponds to the rows in the [Transducer Table](#transducer-table).

```
┌────────────────┬────────────────┬───────────────┬───────────────┬───┬───────────────┬───────────────┬───────────────┬───────────────┐
│ p[a.u.]@0[25us ┆ p[a.u.]@1[25us ┆ p[a.u.]@2[25u ┆ p[a.u.]@3[25u ┆ … ┆ p[a.u.]@10236 ┆ p[a.u.]@10237 ┆ p[a.u.]@10238 ┆ p[a.u.]@10239 │
│ /256]          ┆ /256]          ┆ s/256]        ┆ s/256]        ┆   ┆ [25us/256]    ┆ [25us/256]    ┆ [25us/256]    ┆ [25us/256]    │
│ ---            ┆ ---            ┆ ---           ┆ ---           ┆   ┆ ---           ┆ ---           ┆ ---           ┆ ---           │
│ f32            ┆ f32            ┆ f32           ┆ f32           ┆   ┆ f32           ┆ f32           ┆ f32           ┆ f32           │
╞════════════════╪════════════════╪═══════════════╪═══════════════╪═══╪═══════════════╪═══════════════╪═══════════════╪═══════════════╡
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ …              ┆ …              ┆ …             ┆ …             ┆ … ┆ …             ┆ …             ┆ …             ┆ …             │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
│ 0.0            ┆ -0.000527      ┆ -0.000817     ┆ -0.000865     ┆ … ┆ -0.411363     ┆ -0.389469     ┆ -0.367366     ┆ -0.345066     │
└────────────────┴────────────────┴───────────────┴───────────────┴───┴───────────────┴───────────────┴───────────────┴───────────────┘
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
│ 22.331444        ┆ 15.113414        ┆ 11.268572        ┆ 3.648403         ┆ … ┆ 167.86937        ┆ 144.105682       ┆ 115.743851       ┆ 79.71566         │
│ 23.059395        ┆ 17.771036        ┆ 14.700949        ┆ 6.728968         ┆ … ┆ 129.20639        ┆ 102.939316       ┆ 73.772278        ┆ 40.195816        │
│ 23.036217        ┆ 20.603218        ┆ 15.886523        ┆ 9.236392         ┆ … ┆ 72.646172        ┆ 50.596272        ┆ 26.145405        ┆ -0.767438        │
│ 21.584925        ┆ 20.037151        ┆ 16.766323        ┆ 12.116624        ┆ … ┆ 6.95821          ┆ -7.790637        ┆ -21.844841       ┆ -34.399242       │
│ 17.394489        ┆ 18.289755        ┆ 16.776503        ┆ 13.057217        ┆ … ┆ -61.41378        ┆ -64.008453       ┆ -62.781563       ┆ -57.108852       │
│ …                ┆ …                ┆ …                ┆ …                ┆ … ┆ …                ┆ …                ┆ …                ┆ …                │
│ 14.815317        ┆ 14.747643        ┆ 13.346919        ┆ 9.872995         ┆ … ┆ -72.806496       ┆ -84.871483       ┆ -92.019981       ┆ -93.667465       │
│ 17.50769         ┆ 15.932329        ┆ 12.446443        ┆ 8.104702         ┆ … ┆ -27.582397       ┆ -60.443016       ┆ -89.675652       ┆ -113.377426      │
│ 18.189577        ┆ 15.313375        ┆ 11.066986        ┆ 5.55983          ┆ … ┆ 20.950169        ┆ -27.42453        ┆ -72.527397       ┆ -114.272224      │
│ 18.886011        ┆ 12.433009        ┆ 7.827704         ┆ 3.812024         ┆ … ┆ 67.13327         ┆ 10.793316        ┆ -47.206505       ┆ -97.70639        │
│ 16.812843        ┆ 10.601947        ┆ 4.084629         ┆ 0.993495         ┆ … ┆ 103.386879       ┆ 45.764156        ┆ -15.166505       ┆ -69.37468        │
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
