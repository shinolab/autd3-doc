//~#include<autd3.hpp>
//~#include "autd3/modulation/audio_file/csv.hpp"
//~#include "autd3/modulation/audio_file.hpp"
//~int main() {
//~const auto path = "path/to/foo.csv";
const autd3::modulation::audio_file::Csv m(
    path, 2.0f * autd3::kHz, 4u * autd3::kHz,
    autd3::modulation::SincInterpolation(autd3::modulation::BlackMan{32}));
//~return 0; }