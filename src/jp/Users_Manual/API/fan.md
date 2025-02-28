# ファン制御
  
AUTD3デバイスにはファンがついており, Auto, Off, Onの3つのファンモードが有る. 

Autoモードでは温度監視ICがICの温度を監視し, 一定温度以上になると自動でファンを起動する.
Offモードではファンは常時オフであり, Onモードでは常時オンになる. 

モードの切替は, ファン横のジャンパスイッチで行う. 少しわかりにくいが, 以下の図のようにファン側をショートするとAuto, 真ん中でOff, 右側でOnとなる.

<figure>
    <img src="../../fig/Users_Manual/fan.jpg"/>
    <figcaption>AUTDファン制御用のジャンパスイッチ</figcaption>
</figure>

Autoモードの場合は温度が高くなると自動的にファンが起動する.

Autoモードの場合, `ForceFan`でファンを強制的に起動できる.

<div class="tabs">
<input id="rust_tab" type="radio" class="tab" name="tab" checked>
<label class="tab_item" n=4 for="rust_tab">Rust</label>
<input id="cpp_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cpp_tab">C++</label>
<input id="cs_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="cs_tab">C#</label>
<input id="python_tab" type="radio" class="tab" name="tab">
<label class="tab_item" n=4 for="python_tab">Python</label>

```rust,edition2024
{{#include ../../../codes/Users_Manual/fan.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/fan.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/fan.cs}}
```

```python
{{#include ../../../codes/Users_Manual/fan.py}}
```
</div>

`ForceFan`コンストラクタの引数は`Fn(&Device) -> bool`で, デバイス毎にファンを強制駆動するかどうかを指定する.
