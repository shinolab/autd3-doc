//~#include<autd3.hpp>
//~int main() {
autd3::Square(150 * autd3::Hz,
              autd3::SquareOption{
                  .low = 0x00,
                  .high = 0xFF,
                  .duty = 0.5f,
                  .sampling_config = autd3::SamplingConfig::freq_4k(),
              });
//~return 0; }