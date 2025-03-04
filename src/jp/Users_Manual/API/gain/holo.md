# Holo

`Holo`は多焦点を生成するための`Gain`である.

## Install


{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-gain-holo
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::gain::holo)
```
{{ #endtab }}
{{ #tab name=C# }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Unity }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Python }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #endtabs }}

## APIs

多焦点を生成するアルゴリズムが幾つか提案されており, SDKには以下のアルゴリズムが実装されている.

* [`Naive`](./holo/naive.md) - 単一焦点解の重ね合わせ
* [`GS`](./holo/gs.md) - Gershberg-Saxon
* [`GSPAT`](./holo/gspat.md) - Gershberg-Saxon for Phased Arrays of Transducers
* [`LM`](./holo/lm.md) - Levenberg-Marquardt
* [`Greedy`](./holo/greedy.md) - Greedy algorithm and Brute-force search

また, 各手法は計算Backendを選べるようになっている. (`Greedy`のみBackendの指定はない.)
SDKには以下の`Backend`が用意されている

* `NalgebraBackend` - [Nalgebra](https://nalgebra.org/)を使用
* `CUDABackend` - CUDAを使用, GPUで実行 (Rust版のみ)
* `ArrayFireBackend` - [ArrayFire](https://arrayfire.com/)を使用 (Rust版のみ)

> NOTE: `CUDABackend`や`ArrayFireBackend`は高速化を目的としているが, ほとんどの場合, `NalgebraBackend`で十分である. 使用時は, 必ずベンチマークを取ること.

## 振幅制約

各アルゴリズムの計算結果の振幅は最終的に振動子が出力できる範囲に制限する必要がある.
これはオプションの`EmissionConstraint`で制御でき, 以下の4つのいずれかを指定する必要がある.

- Normalize: 振幅の最大値ですべての振動子の振幅を割り, 規格化する.
- Uniform: すべての振動子の振幅を指定した値にする.
- Clamp: 振幅を指定の範囲にクランプする.
- Multiply: 規格化後, 所定の値を乗算する.
