//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
autd3::GainSTM stm(autd3::SamplingConfig(1 * autd3::Hz),
                   {autd3::gain::Null(), autd3::gain::Null()});
//~return 0; }