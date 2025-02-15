//~#include<autd3.hpp>
#include <autd3/modulation/fourier.hpp>

//~int main() {
autd3::modulation::Fourier({autd3::Sine(100 * autd3::Hz, autd3::SineOption{}),
                            autd3::Sine(150 * autd3::Hz, autd3::SineOption{})},
                           autd3::modulation::FourierOption{
                               .scale_factor = std::nullopt,
                               .clamp = false,
                               .offset = 0x00,
                           });

//~return 0; }