# Geometry

GeometryはAUTD3デバイスが現実世界でどのように配置されているかを管理している.

[[_TOC_]]

## デバイス/振動子のインデックス

デバイスには接続された順に0から始まるインデックスが割り当てられる.

また, 各デバイスは$249$個の振動子が配置されており, ローカルインデックスが割り振られている ([はじめに/ハードウェア](../getting_started/hardware.md)の「AUTDの表面写真」を参照).

## GeometryのAPI

- `num_devices()`: 有効なデバイスの数を取得
- `num_transducers()`: 有効な全振動子の数を取得
- `center()`: 有効な全振動子の中心を取得

なお, `Geometry`には`Controller`から直接アクセスできる.

<div class="tabs">
<input id="rust_tab_geometry" type="radio" class="tab" name="tab_geometry" checked>
<label class="tab_item" n=4 for="rust_tab_geometry">Rust</label>
<input id="cpp_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="cpp_tab_geometry">C++</label>
<input id="cs_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="cs_tab_geometry">C#</label>
<input id="python_tab_geometry" type="radio" class="tab" name="tab_geometry">
<label class="tab_item" n=4 for="python_tab_geometry">Python</label>

```rust
{{#include ../../../codes/Users_Manual/geometry_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/geometry_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/geometry_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/geometry_3.py}}
```
</div>

### Deviceの取得

`Geometry`は`Device`のコンテナになっており, `Device`が`Transducer`のコンテナになっている.

`Device`を取得するには, インデクサを使用する.
あるいは, イテレータを使用することもできる.

<div class="tabs">
<input id="rust_tab_device" type="radio" class="tab" name="tab_device" checked>
<label class="tab_item" n=4 for="rust_tab_device">Rust</label>
<input id="cpp_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="cpp_tab_device">C++</label>
<input id="cs_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="cs_tab_device">C#</label>
<input id="python_tab_device" type="radio" class="tab" name="tab_device">
<label class="tab_item" n=4 for="python_tab_device">Python</label>

```rust
{{#include ../../../codes/Users_Manual/geometry_4.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/geometry_4.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/geometry_4.cs}}
```

```python
{{#include ../../../codes/Users_Manual/geometry_4.py}}
```
</div>

## DeviceのAPI

- `idx()`: デバイスのインデックス
- `enable`: 有効/無効フラグ. オフにすると, 以降, そのデバイスのデータは更新されなくなる.
  - 更新されなくなるだけで, 出力が止まるわけではないことに注意.
- `sound_speed`: 音速の取得/設定. 単位はmm/s. **位相計算などに使用されるため, 可能な限り現実に即した値を設定することをおすすめする**. デフォルトの音速は$340\times 10^{3}\,\mathrm{mm/s}$となっており, これは, およそ摂氏15度での空気の音速に相当する.
- `set_sound_speed_from_temp(temp)`: 温度`temp` [℃]から音速を設定. なお, `Geometry`にも同名の関数があり, それを使用することですべての有効なデバイスに対して温度から音速を設定できる.
- `translate(t)`: `t`による平行移動
- `rotate(r)`: `r`による回転
- `affine(t, r)`: アフィン変換 (`t`による平行移動と`r`による回転)
- `wavelength()`: デバイスが放出する超音波の波長
- `wavenumber()`: デバイスが放出する超音波の波数
- `rotation()`: デバイスの回転
- `x_direction()`: デバイスのx方向ベクトル
- `y_direction()`: デバイスのy方向ベクトル
- `axial_direction()`: デバイスの軸方向ベクトル (振動子が向く方向)

<div class="tabs">
<input id="rust_tab_device_api" type="radio" class="tab" name="tab_device_api" checked>
<label class="tab_item" n=4 for="rust_tab_device_api">Rust</label>
<input id="cpp_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="cpp_tab_device_api">C++</label>
<input id="cs_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="cs_tab_device_api">C#</label>
<input id="python_tab_device_api" type="radio" class="tab" name="tab_device_api">
<label class="tab_item" n=4 for="python_tab_device_api">Python</label>

```rust
{{#include ../../../codes/Users_Manual/device_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/device_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/device_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/device_0.py}}
```
</div>

### Transducerの取得

`Device`は`Transducer`のコンテナになっており, `Transducer`は各振動子の情報を格納している.

`Transducer`を取得するには, インデクサを使用する.
また, イテレータを使用することもできる.

<div class="tabs">
<input id="rust_tab_transducer" type="radio" class="tab" name="tab_transducer" checked>
<label class="tab_item" n=4 for="rust_tab_transducer">Rust</label>
<input id="cpp_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="cpp_tab_transducer">C++</label>
<input id="cs_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="cs_tab_transducer">C#</label>
<input id="python_tab_transducer" type="radio" class="tab" name="tab_transducer">
<label class="tab_item" n=4 for="python_tab_transducer">Python</label>

```rust
{{#include ../../../codes/Users_Manual/device_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/device_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/device_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/device_1.py}}
```
</div>

## TransducerのAPI

以下の情報を取得できる.

- `idx()`: 振動子の(ローカル)インデックス
- `dev_idx()`: 振動子が属するデバイスのインデックス
- `position()`: 振動子の位置

<div class="tabs">
<input id="rust_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api" checked>
<label class="tab_item" n=4 for="rust_tab_transducer_api">Rust</label>
<input id="cpp_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="cpp_tab_transducer_api">C++</label>
<input id="cs_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="cs_tab_transducer_api">C#</label>
<input id="python_tab_transducer_api" type="radio" class="tab" name="tab_transducer_api">
<label class="tab_item" n=4 for="python_tab_transducer_api">Python</label>

```rust
{{#include ../../../codes/Users_Manual/transducer_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/transducer_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/transducer_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/transducer_0.py}}
```
</div>

