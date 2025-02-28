//~#include<autd3.hpp>
#include "autd3/modulation/audio_file.hpp"

//~int main() {
//~using namespace autd3;
const auto path = "path/to/foo.csv";
modulation::audio_file::Csv(path, 4000.0f * Hz,
                            modulation::audio_file::CsvOption{
                                .delimiter = ',',
                            });
//~return 0; }