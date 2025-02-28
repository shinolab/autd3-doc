//~#include<autd3.hpp>
//~#include<chrono>
//~int main() {
//~using namespace autd3;
//~const auto s =
SamplingConfig(4000.0f * Hz).into_nearest();
// or
//~const auto sp =
SamplingConfig(std::chrono::microseconds(250)).into_nearest();
//~return 0; }