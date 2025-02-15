//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
const autd3::Point3 center(0, 0, 150);
const auto points_num = 200;
const auto radius = 30.0f;
std::vector<autd3::ControlPoints<2>> foci;
std::ranges::copy(
    iota(0) | take(points_num) | transform([&](auto i) {
      const auto theta = 2.0f * autd3::pi * static_cast<float>(i) /
                         static_cast<float>(points_num);
      autd3::Vector3 p =
          radius * autd3::Vector3(std::cos(theta), std::sin(theta), 0);
      return autd3::ControlPoints<2>{
          .points =
              std::array{
                  autd3::ControlPoint{.point = center + p,
                                      .phase_offset = autd3::Phase::zero()},
                  autd3::ControlPoint{.point = center - p,
                                      .phase_offset = autd3::Phase::zero()}},
          .intensity = std::numeric_limits<autd3::EmitIntensity>::max()};
    }),
    std::back_inserter(foci));
autd3::FociSTM stm(foci, 1.0f * autd3::Hz);
//~return 0; }