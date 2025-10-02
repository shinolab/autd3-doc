First, create a project and add the `autd3` library as a dependency.
Also, add the `autd3-link-ethercrab` library for communication with the device.

```shell
cargo new --bin autd3-sample
cd autd3-sample
cargo add autd3
cargo add autd3-link-ethercrab
```

Next, edit the `src/main.rs` file as follows.
This is the source code for applying AM modulation of $\SI{150}{Hz}$ to a single focal point.

```rust,should_panic,name=main.rs,edition2024
{{#include ../../../codes/Users_Manual/Tutorial/single/main.rs}}
```

Then, run it.

```shell
cargo run --release
```

## Notes for Linux and macOS Users

On Linux and macOS, administrator privileges could be required.
In that case, run:
```shell
cargo build --release && sudo ./target/release/autd3_sample
```
