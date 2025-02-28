//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
Focus(Point3(x, y, z),
      FocusOption{
          .intensity = std::numeric_limits<EmitIntensity>::max(),
          .phase_offset = Phase::zero(),
      });
//~return 0; }