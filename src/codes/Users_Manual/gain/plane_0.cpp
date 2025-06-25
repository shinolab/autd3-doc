//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
Plane(Vector3(nx, ny, nz),
      PlaneOption{
          .intensity = std::numeric_limits<Intensity>::max(),
          .phase_offset = Phase::zero(),
      });
//~return 0; }