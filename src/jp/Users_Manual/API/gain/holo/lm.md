# LM
[Source](https://github.com/shinolab/autd3-rs/blob/v30.0.1/autd3-gain-holo/src/nls/lm.rs)

Levenberg-Marquardt法 (LM法) に基づく多焦点`Gain`.
LM法はLevenberg[^levenberg1944]とMarquardt[^marquardt1963]で提案された非線形最小二乗問題の最適化法, 実装はMadsenのテキスト[^madsen2004]に基づく.

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
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.rs}}
```

```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.cpp}}
```

```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.cs}}
```

```python
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.py}}
```
</div>

各パラメータのデフォルトは上記の通り.
パラメータの詳細はテキスト[^madsen2004]を参照されたい.

[^levenberg1944]: Levenberg, Kenneth. "A method for the solution of certain non-linear problems in least squares." Quarterly of applied mathematics 2.2 (1944): 164-168.

[^marquardt1963]: Marquardt, Donald W. "An algorithm for least-squares estimation of nonlinear parameters." Journal of the society for Industrial and Applied Mathematics 11.2 (1963): 431-441.

[^madsen2004]: Madsen, Kaj, Hans Bruun Nielsen, and Ole Tingleff. "Methods for non-linear least squares problems." (2004).
