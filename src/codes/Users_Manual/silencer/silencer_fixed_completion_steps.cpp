//~#include<chrono>
//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
Silencer{FixedCompletionTime{.intensity = std::chrono::microseconds(250),
                             .phase = std::chrono::microseconds(250),
                             .strict_mode = true},
         SilencerTarget::Intensity};
//~return 0; }