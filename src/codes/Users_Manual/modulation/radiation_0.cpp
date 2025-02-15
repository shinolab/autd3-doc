//~#include<autd3.hpp>
#include <autd3/modulation/radiation_pressure.hpp>

//~int main() {
autd3::modulation::RadiationPressure(autd3::Sine(150 * autd3::Hz,
                                                 autd3::SineOption{}));
//~return 0; }