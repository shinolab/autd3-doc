//~#include<chrono>
//~#include<autd3.hpp>
//~int main() {
autd3::Silencer{
    autd3::FixedCompletionTime{.intensity = std::chrono::microseconds(250),
                               .phase = std::chrono::microseconds(250),
                               .strict_mode = true},
    autd3::SilencerTarget::Intensity};
//~return 0; }