//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
auto stm =
    autd3::GainSTM(1.0f * autd3::Hz, {autd3::gain::Null(), autd3::gain::Null()})
        .with_mode(autd3::GainSTMMode::PhaseFull);
//~return 0; }