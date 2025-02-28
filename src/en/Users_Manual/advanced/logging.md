# Enabling Logging

## Rust

Since [tracing](https://github.com/tokio-rs/tracing) is used for logging, you can enable log output as follows.

```rust,edition2024
tracing_subscriber::fmt()
    .with_max_level(tracing::Level::INFO)
    .init();
```

## C++/C#/Python

You can enable log output by setting the `RUST_LOG` environment variable to `autd3=<LEVEL>` and calling `tracing_init`.

You can specify one of the following for `<LEVEL>`. The lower you go, the more detailed the log output.
- `ERROR`
- `WARN`
- `INFO`
- `DEBUG`
- `TRACE`

```cpp
#include <stdlib.h>

#ifdef WIN32
_putenv_s("RUST_LOG", "autd3=INFO");
#else
setenv("RUST_LOG", "autd3=INFO", false);
#endif

autd3::tracing_init();
```

```cs
System.Environment.SetEnvironmentVariable("RUST_LOG", "autd3=INFO");

AUTD3Sharp.Tracing.Init();
```

```python
from pyautd3 import tracing_init

os.environ["RUST_LOG"] = "autd3=INFO"

tracing_init()
```

## Unity

In Unity, you can enable log output by specifying the path to the log file as an argument to `Tracing.Init`.

```cs
System.Environment.SetEnvironmentVariable("RUST_LOG", "autd3=INFO");

AUTD3Sharp.Tracing.Init("<path to log file>");
```

Also, if you are using `AUTD3Sharp.Link.SOEM`, enable `SOEM` logging **first**.

```cs
AUTD3Sharp.Link.SOEM.Tracing.Init("<path to log file>");
AUTD3Sharp.Tracing.Init("<path to log file>");
```
