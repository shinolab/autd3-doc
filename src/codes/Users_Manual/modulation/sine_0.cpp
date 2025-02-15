//~#include<autd3.hpp>
//~int main() {
autd3::Sine(150 * autd3::Hz,
            autd3::SineOption{
                .intensity = 0xFF,
                .offset = 0x80,
                .phase = 0.0f * autd3::rad,
                .clamp = false,
                .sampling_config = autd3::SamplingConfig::freq_4k(),
            });
//~return 0; }