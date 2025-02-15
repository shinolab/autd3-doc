//~#include<iostream>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
const auto m = autd3::Sine(150 * autd3::Hz, autd3::SineOption{});
std::cout << m.sampling_config().freq() << std::endl;  // -> 4kHz
                                                       //~return 0; }