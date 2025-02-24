//~#include<autd3.hpp>
#include "autd3/modulation/audio_file.hpp"

//~int main() {
const auto path = "path/to/foo.csv";
autd3::modulation::audio_file::Csv(path, 4000.0f * autd3::Hz,
                                   autd3::modulation::audio_file::CsvOption{
                                       .delimiter = ',',
                                   });
//~return 0; }