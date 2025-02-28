//~#include<autd3.hpp>
#include <autd3/modulation/fourier.hpp>

//~int main() {
//~using namespace autd3;
modulation::Fourier({Sine(100 * Hz, SineOption{}),
                     Sine(150 * Hz, SineOption{})},
                    modulation::FourierOption{
                        .scale_factor = std::nullopt,
                        .clamp = false,
                        .offset = 0x00,
                    });

//~return 0; }