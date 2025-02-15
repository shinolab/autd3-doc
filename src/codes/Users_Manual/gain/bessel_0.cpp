//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
//~const auto theta = 0.0;
autd3::Bessel(autd3::Point3(x, y, z), autd3::Vector3(nx, ny, nz),
              theta* autd3::rad,
              autd3::BesselOption{
                  .intensity = std::numeric_limits<autd3::EmitIntensity>::max(),
                  .phase_offset = autd3::Phase::zero(),
              });
//~return 0; }