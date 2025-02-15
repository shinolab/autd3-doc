//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd3::Focus(autd3::Point3(x, y, z),
             autd3::FocusOption{
                 .intensity = std::numeric_limits<autd3::EmitIntensity>::max(),
                 .phase_offset = autd3::Phase::zero(),
             });
//~return 0; }