//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
autd3::SamplingConfig(10);
// or
autd3::SamplingConfig(4000u * autd3::Hz);
// or
autd3::SamplingConfig(std::chrono::microseconds(250));
//~return 0; }