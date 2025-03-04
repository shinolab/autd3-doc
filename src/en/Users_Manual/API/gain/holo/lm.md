# LM

`Gain` for multiple focal points based on the Levenberg-Marquardt method (LM method).
The LM method is an optimization method for nonlinear least squares problems proposed by Levenberg[^levenberg1944] and Marquardt[^marquardt1963], and the implementation is based on Madsen's text[^madsen2004].

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../../codes/Users_Manual/gain/holo/lm.py}}
```
{{ #endtab }}
{{ #endtabs }}

The defaults for each parameter are as above.
For details on the parameters, refer to the text[^madsen2004].

[^levenberg1944]: Levenberg, Kenneth. "A method for the solution of certain non-linear problems in least squares." Quarterly of applied mathematics 2.2 (1944): 164-168.

[^marquardt1963]: Marquardt, Donald W. "An algorithm for least-squares estimation of nonlinear parameters." Journal of the society for Industrial and Applied Mathematics 11.2 (1963): 431-441.

[^madsen2004]: Madsen, Kaj, Hans Bruun Nielsen, and Ole Tingleff. "Methods for non-linear least squares problems." (2004).
