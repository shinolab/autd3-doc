# Transform

`Transform`は`Gain`になんらかの後処理を適用するための機能である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/gain/transform_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/gain/transform_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/gain/transform_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/gain/transform_0.py}}
```

`with_transform`の引数は`Fn(&Device) -> Fn(&Transducer, &Drive) -> Drive`である.
