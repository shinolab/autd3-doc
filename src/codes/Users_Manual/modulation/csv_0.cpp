//~#include<autd3.hpp>
//~#include "autd3/modulation/audio_file/csv.hpp"
#include "autd3/modulation/audio_file.hpp"

//~int main() {
const auto path = "path/to/foo.csv";
const autd3::modulation::audio_file::Csv m(path, 4000u * autd3::Hz);
//~return 0; }