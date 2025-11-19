//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
Square(150 * Hz, SquareOption{
                     .low = 0x00,
                     .high = 0xFF,
                     .duty = 0.5f,
                     .sampling_config = SamplingConfig::FREQ_4K,
                 });
//~return 0; }