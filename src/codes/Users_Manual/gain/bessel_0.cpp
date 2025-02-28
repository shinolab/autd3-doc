//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
//~const auto theta = 0.0;
Bessel(Point3(x, y, z), Vector3(nx, ny, nz), theta* rad,
       BesselOption{
           .intensity = std::numeric_limits<EmitIntensity>::max(),
           .phase_offset = Phase::zero(),
       });
//~return 0; }