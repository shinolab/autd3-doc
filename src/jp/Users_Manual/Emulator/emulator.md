# エミュレータ

`Emulator`を使用すると, `Simulator`よりも詳細な出力位相/パルス幅, 出力電圧, 出力音波, および, 音場の計算が行える.

> NOTE: 現在, `Emulator`はRust, 及び, Pythonからのみ使用可能である.
> C++, C#へ移植する予定はない.

[[_TOC_]]

## Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-emulator
```
{{ #endtab }}
{{ #tab name=Python }}
```shell
pip install pyautd3_emulator
```
{{ #endtab }}
{{ #endtabs }}

## APIs

`Emulator`が出力するデータはPolarsのDataFrameである.
詳しくは, [Polarsのドキュメント](https://pola.rs/)を参照されたい.

### 振動子テーブル

振動子の一覧を表示する.

各列には, デバイスインデックス, 振動子の(ローカル)インデックス, 位置, 極方向が格納される.

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

### 出力位相/パルス幅の計算

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

> NOTE: `tick`で指定する時間間隔は, $\SI{25}{us}$の倍数である必要がある.

各時刻 ($\SI{25}{us}$単位) における, 位相/パルス幅が各列に格納される.
各列の名前は`<phase/pulse_width>@<時刻>[ns]`である.

各行は[振動子テーブル](#振動子テーブル)の行と対応している.

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

### 出力電圧

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

各時刻 ($\SI{25}{us}/256$単位) における, 出力電圧が各列に格納される.
各列の名前は`voltage[V]@<時刻>[25us/256]`である.

各行は[振動子テーブル](#振動子テーブル)の行と対応している.

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

### 出力音圧

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

各時刻 ($\SI{25}{us}/256$単位) における, 規格化された出力音圧が各列に格納される.
各列の名前は`p[a.u.]@<時刻>[25us/256]`である.

各行は[振動子テーブル](#振動子テーブル)の行と対応している.

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

### 音場の計算 (瞬時値)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_field.rs}}
```
> NOTE: `gpu`オプションは, `gpu` featureを有効にしている場合のみ使用可能である.
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_field.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: 計測点を指定する方法として, Rust版は, `RangeXYZ`以外に, 列挙順の異なる`RangeZXY`等や, 2次元専用の`RangeXY`等, 1次元専用の`RangeX`等が使用できる.
> あるいは, 任意の点を指定するために, `Vec<Vector3>`が使用できる.
> Python版は, `RangeXYZ`のみが使用できる.

`print_progress`オプションを有効にすると計算の進捗が表示される.
また, `gpu`オプションを有効にすると, 計算がGPU上で実行される.

膨大なメモリが消費される可能性があるため, `next`関数によって, 一部時刻のみを取得するようになっている.
なお, `skip`関数を使用することで, 指定した時間だけスキップすることができる.

各観測点における, 出力音圧が時系列順 (単位は`time_step`で指定) に各列に格納される.
各列の名前は, `p[Pa]@<時刻>[ns]`である.
各行は, `observe_points`で取得できる観測点と対応している.

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

### 音場の計算 (RMS)

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/emulator/emulator_rms.rs}}
```
> NOTE: `gpu`オプションは, `gpu` featureを有効にしている場合のみ使用可能である.
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/emulator/emulator_rms.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: 最低, $\SI{25}{us}$は時刻を進める必要がある.

> NOTE: RMSで計算される値は, **上記の瞬時音場のRMSではない**. 伝搬遅延や振動子の応答を無視した線形重ね合わせである.

各観測点における, 出力音圧のRMSが時系列順 (単位は$\SI{25}{us}$) で各列に格納される.
各列の名前は, `rms[Pa]@<時刻>[ns]`である.
各行は, `observe_points`で取得できる観測点と対応している.

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

さらなる, Exampleは[autd3-emulator (Rust)](https://github.com/shinolab/autd3-emulator/tree/main/examples), 及び, [pyautd3 (Python)](https://github.com/shinolab/pyautd3/tree/main/example/emulator)を参照されたい.
