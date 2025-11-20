//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
//~using namespace autd3;
//~auto autd = Controller::open({AUTD3{
//~                                 .pos = Point3::origin(),
//~                                 .rot = Quaternion::Identity(),
//~                             }},
//~                             link::Nop{});
const Point3 center = autd.center() + Vector3(0, 0, 150);
constexpr auto points_num = 200;
constexpr auto radius = 30.0f;
GainSTM(iota(0) | take(points_num) | transform([&](auto i) {
          const auto theta = 2.0f * pi * static_cast<float>(i) /
                             static_cast<float>(points_num);
          return Focus(
              center + radius * Vector3(std::cos(theta), std::sin(theta), 0),
              FocusOption{});
        }) | std::ranges::to<std::vector<Focus> >(),
        1.0f * Hz, GainSTMOption{.mode = GainSTMMode::PhaseIntensityFull});
//~return 0; }