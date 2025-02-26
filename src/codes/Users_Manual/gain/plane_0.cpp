//~#include<autd3.hpp>
//~int main() {
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
autd3::Plane(autd3::Vector3(nx, ny, nz),
             autd3::PlaneOption{
                 .intensity = std::numeric_limits<autd3::EmitIntensity>::max(),
                 .phase_offset = autd3::Phase::zero(),
             });
//~return 0; }