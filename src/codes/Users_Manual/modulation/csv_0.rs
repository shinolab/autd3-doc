# use autd3::prelude::*;
use autd3_modulation_audio_file::{Csv, CsvOption};

# fn main() {
# let _ = 
Csv::new(
    "path/to/foo.csv",
    4000.0 * Hz,
    CsvOption { delimiter: b',', has_headers: false },
);
# }