//~#include<iostream>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
const auto m = Sine(150 * Hz, SineOption{});
std::cout << m.sampling_config().freq() << std::endl;  // -> 4kHz
                                                       //~return 0; }