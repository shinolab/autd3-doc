# use autd3::prelude::*;
use autd3_modulation_audio_file::{Csv, CsvOption};

# fn main() {
# let _ = 
Csv {
    path: "path/to/foo.csv",
    sampling_config: 4000 * Hz,
    option: CsvOption { deliminator: b',' },
};
# }