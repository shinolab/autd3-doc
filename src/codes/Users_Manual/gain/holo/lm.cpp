//~#include<autd3.hpp>
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
const auto backend = std::make_shared<gain::holo::NalgebraBackend>();
auto g = gain::holo::LM(
    std::vector<std::pair<Point3, gain::holo::Amplitude>>{
        {Point3(x1, y1, z1), 5e3 * Pa},
        {Point3(x2, y2, z2), 5e3 * Pa},
    },
    gain::holo::LMOption{
        .eps_1 = 1e-8,
        .eps_2 = 1e-8,
        .tau = 1e-3,
        .k_max = 5,
        .initial = {},
        .constraint = gain::holo::EmissionConstraint::Clamp(
            std::numeric_limits<Intensity>::min(),
            std::numeric_limits<Intensity>::max()),
    },
    backend);
//~return 0; }