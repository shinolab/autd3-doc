//~#include<iostream>
//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
FociSTM stm(
    std::vector{
        Point3::origin(),
        Point3::origin(),
    },
    1.0f * Hz);
std::cout << stm.sampling_config().freq() << std::endl;  // -> 2Hz
                                                         //~return 0; }