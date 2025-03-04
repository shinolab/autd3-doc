# 複数デバイスの接続

AUTD3は複数のデバイスをデイジーチェーン接続して大きな一つのアレイを構成することができる.
SDKは複数台を接続したとしても, 透過的に使用できるように設計されている.


SDKで複数台のデバイスを使用する場合は`Controller::open`関数の第1引数で**接続したデバイスの順に**`AUTD3`構造体を指定する必要がある.
ハードウェアの接続方法は[はじめに/ハードウェア](../getting_started/hardware.md)を参照されたい.

以下では, 2つのデバイスを接続する場合の手順を示す.

[[_TOC_]]

## 並進のみ

<figure>
  <img src="../../fig/Users_Manual/hor_left_ori_left_1.png"/>
</figure>

例えば, 上図のように配置・接続しており, 図左側のデバイスが1台目, 右側のデバイスが2台目だとする.
さらに, グローバル座標を1台目のローカル座標と同じようにとるとすると, コードは以下の通りになる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

ここで, `pos`はグローバル座標におけるデバイスの位置を表す.
なお, `AUTD3::DEVICE_WIDTH`はデバイスの (基板外形を含めた) 横幅である.

## グローバル座標の設定

SDKで使用するグローバル座標の原点や向きは, ユーザーが自由に設定できる.

<figure>
  <img src="../../fig/Users_Manual/hor_right_ori_left_1.png"/>
</figure>

例えば, 上図のように, グローバル座標を2台目のローカル座標と同じようにとると, コードは以下の通りになる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_1.py}}
```
{{ #endtab }}
{{ #endtabs }}

## 並進と回転

デバイスの回転を指定する場合は`rot`で指定する.
ここで回転はオイラー角, または, クオータニオンで指定する.

<figure>
  <img src="../../fig/Users_Manual/vert.png"/>
</figure>

例えば, 上図のように配置されており, 下が1台目, 左が2台目で, グローバル座標を1台目のローカル座標と同じだとすると, コードは以下の通りになる.

{{ #tabs }}
{{ #tab name=Rust }}
```rust,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../codes/Users_Manual/Tutorial/multiple/geometry_2.py}}
```
{{ #endtab }}
{{ #endtabs }}

> NOTE: Rust版のみ, 12種類全てのオイラー角が使用できる.
> それ以外の言語ではXYZ, ZYZのみ.
