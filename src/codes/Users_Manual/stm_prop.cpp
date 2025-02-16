//~#include<iostream>
//~#include<autd3.hpp>
//~int main() {
autd3::FociSTM stm(
    std::vector{
        autd3::Point3::origin(),
        autd3::Point3::origin(),
    },
    1.0f * autd3::Hz);
std::cout << stm.sampling_config().freq() << std::endl;  // -> 2Hz
                                                         //~return 0; }