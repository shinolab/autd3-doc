//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
const float sound_speed = autd.environment.sound_speed;
autd.environment.sound_speed = 340e3;
autd.environment.set_sound_speed_from_temp(15.);
const auto wavelength = autd.environment.wavelength();
const auto wavenumber = autd.environment.wavenumber();
//~return 0; }