//~#include<vector>
//~#include<autd3.hpp>
#include <autd3/modulation/custom.hpp>

//~int main() {
autd3::modulation::Custom(std::vector<uint8_t>{0xFF, 0x00}, 4000u * autd3::Hz);
//~return 0; }