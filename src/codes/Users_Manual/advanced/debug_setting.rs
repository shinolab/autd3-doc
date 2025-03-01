# use autd3::prelude::*;
# fn main() {
# let _ =
DebugSettings::new(|_dev, gpio| {
    if gpio == GPIOOut::O0 {
        DebugType::BaseSignal
    } else {
        DebugType::None
    }
});
# }