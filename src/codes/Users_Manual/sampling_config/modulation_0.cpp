//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
SamplingConfig(10);
// or
SamplingConfig(4000.0f * Hz);
// or
SamplingConfig(std::chrono::microseconds(250));
//~return 0; }