//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
Sine(150 * Hz, SineOption{
                   .intensity = 0xFF,
                   .offset = 0x80,
                   .phase = 0.0f * rad,
                   .clamp = false,
                   .sampling_config = SamplingConfig::FREQ_4K,
               });
//~return 0; }