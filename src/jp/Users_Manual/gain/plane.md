# Plane

`Plane`は平面波を出力する.

```rust,edition2021
{{#include ../../../codes/Users_Manual/gain/plane_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/gain/plane_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/gain/plane_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/gain/plane_0.py}}
```

コンストラクタには平面波の進行方向を指定する.

## 振幅/位相オフセットの指定

`with_intensity`, `with_phase_offset`にて, 出力振幅と位相オフセットを$\SI{8}{bit}$で指定できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/gain/plane_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/gain/plane_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/gain/plane_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/gain/plane_1.py}}
```
