//~#include<autd3.hpp>
//~#include "autd3/modulation/audio_file.hpp"
//~int main() {
//~const auto path = "path/to/foo.wav";
const autd3::modulation::audio_file::Wav m(
    path, 4u * autd3::kHz,
    autd3::modulation::SincInterpolation(autd3::modulation::BlackMan{32}));
//~return 0; }