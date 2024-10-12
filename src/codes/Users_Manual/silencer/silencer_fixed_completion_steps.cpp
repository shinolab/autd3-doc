//~#include<chrono>
//~#include<autd3.hpp>
//~int main() {
const auto config = autd3::Silencer{
    autd3::FixedCompletionTime{.intensity = std::chrono::microseconds(250),
                               .phase = std::chrono::microseconds(250)}};
//~return 0; }