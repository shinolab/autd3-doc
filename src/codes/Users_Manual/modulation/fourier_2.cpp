//~#include<autd3.hpp>
//~#include <autd3/modulation/fourier.hpp>
//~int main() {
const auto m = autd3::modulation::Fourier(
    {autd3::modulation::Sine(100 * autd3::Hz),
     autd3::modulation::Sine(150 * autd3::Hz)
         .with_phase(autd3::pi / 2.0f * autd3::rad)});
//~return 0; }