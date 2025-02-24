//~#include<autd3.hpp>
//~#include<chrono>
//~int main() {
//~const auto s =
autd3::SamplingConfig(4000.0f * autd3::Hz).into_nearest();
// or
//~const auto sp =
autd3::SamplingConfig(std::chrono::microseconds(250)).into_nearest();
//~return 0; }