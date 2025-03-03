# Holo

`Holo`は多焦点を生成するための`Gain`である.

## Install

<div class="tabs">
<input id="rust_tab_install" type="radio" class="tab" name="tab_install" checked>
<label class="tab_item" n=5 for="rust_tab_install">Rust</label>
<input id="cpp_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cpp_tab_install">C++</label>
<input id="cs_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="cs_tab_install">C#</label>
<input id="unity_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="unity_tab_install">Unity</label>
<input id="python_tab_install" type="radio" class="tab" name="tab_install">
<label class="tab_item" n=5 for="python_tab_install">Python</label>

```rust,name=Shell
cargo add autd3-gain-holo
```

```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::gain::holo)
```

<div class="tab_content" id="cs_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="unity_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>

<div class="tab_content" id="python_code_content">
  <p>
    メインライブラリに含まれている.
  </p>
</div>
</div>

## APIs

多焦点を生成するアルゴリズムが幾つか提案されており, SDKには以下のアルゴリズムが実装されている.

* `Naive` - 単一焦点解の重ね合わせ
* `GS` - Gershberg-Saxon, Marzoらの論文[^marzo2019]に基づく
* `GSPAT` - Gershberg-Saxon for Phased Arrays of Transducers, Plasenciaらの論文[^plasencia2020]に基づく
* `LM` - Levenberg-Marquardt, LM法はLevenberg[^levenberg1944]とMarquardt[^marquardt1963]で提案された非線形最小二乗問題の最適化法, 実装はMadsenのテキスト[^madsen2004]に基づく.
* `Greedy` - Greedy algorithm and Brute-force search, 鈴木らの論文[^suzuki2021]に基づく

また, 各手法は計算Backendを選べるようになっている. (`Greedy`のみBackendの指定はない.)
SDKには以下の`Backend`が用意されている

* `NalgebraBackend` - [Nalgebra](https://nalgebra.org/)を使用
* `CUDABackend` - CUDAを使用, GPUで実行 (Rust版のみ)
* `ArrayFireBackend` - [ArrayFire](https://arrayfire.com/)を使用 (Rust版のみ)

> NOTE: `CUDABackend`や`ArrayFireBackend`は高速化を目的としているが, ほとんどの場合, `NalgebraBackend`で十分である. 使用時は, 必ずベンチマークを取ること.

<div class="tabs">
<input id="rust_tab_api" type="radio" class="tab" name="tab_api" checked>
<label class="tab_item" n=4 for="rust_tab_api">Rust</label>
<input id="cpp_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cpp_tab_api">C++</label>
<input id="cs_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="cs_tab_api">C#</label>
<input id="python_tab_api" type="radio" class="tab" name="tab_api">
<label class="tab_item" n=4 for="python_tab_api">Python</label>

```rust
{{#include ../../../../codes/Users_Manual/gain/holo_0.rs}}
```

```cpp
{{#include ../../../../codes/Users_Manual/gain/holo_0.cpp}}
```

```cs
{{#include ../../../../codes/Users_Manual/gain/holo_0.cs}}
```

```python
{{#include ../../../../codes/Users_Manual/gain/holo_0.py}}
```
</div>

## 振幅制約と最適化パラメータ

各アルゴリズムの計算結果の振幅は最終的に振動子が出力できる範囲に制限する必要がある.
これはオプションの`EmissionConstraint`で制御でき, 以下の4つのいずれかを指定する必要がある.

- Normalize: 振幅の最大値ですべての振動子の振幅を割り, 規格化する.
- Uniform: すべての振動子の振幅を指定した値にする.
- Clamp: 振幅を指定の範囲にクランプする.
- Multiply: 規格化後, 所定の値を乗算する.

また, 各アルゴリズムごとに追加のパラメータが存在する.

各パラメータの詳細はそれぞれの論文を参照されたい.

[^marzo2019]: Marzo, Asier, and Bruce W. Drinkwater. "Holographic acoustic tweezers." Proceedings of the National Academy of Sciences 116.1 (2019): 84-89.

[^plasencia2020]: Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers." ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.

[^levenberg1944]: Levenberg, Kenneth. "A method for the solution of certain non-linear problems in least squares." Quarterly of applied mathematics 2.2 (1944): 164-168.

[^marquardt1963]: Marquardt, Donald W. "An algorithm for least-squares estimation of nonlinear parameters." Journal of the society for Industrial and Applied Mathematics 11.2 (1963): 431-441.

[^madsen2004]: Madsen, Kaj, Hans Bruun Nielsen, and Ole Tingleff. "Methods for non-linear least squares problems." (2004).

[^suzuki2021]: Suzuki, Shun, et al. "Radiation Pressure Field Reconstruction for Ultrasound Midair Haptics by Greedy Algorithm with Brute-Force Search." IEEE Transactions on Haptics (2021).
