//~#include <autd3.hpp>
#include "autd3/gain/holo.hpp"

//~using namespace autd3;
using gain::holo::Pa;

//~int main() {
//~const auto x1 = 0.0;
//~const auto y1 = 0.0;
//~const auto z1 = 0.0;
//~const auto x2 = 0.0;
//~const auto y2 = 0.0;
//~const auto z2 = 0.0;
auto g = gain::holo::Greedy(
    std::vector<std::pair<Point3, gain::holo::Amplitude>>{
        {Point3(x1, y1, z1), 5e3 * Pa},
        {Point3(x2, y2, z2), 5e3 * Pa},
    },
    gain::holo::GreedyOption{
        .phase_div = 16,
        .constraint = gain::holo::EmissionConstraint::Uniform(
            std::numeric_limits<EmitIntensity>::max())});
//~  return 0;
//~}