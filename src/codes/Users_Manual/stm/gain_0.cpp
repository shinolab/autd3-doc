//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
//~using namespace autd3;
const Point3 center(0, 0, 150);
const auto points_num = 200;
const auto radius = 30.0f;
std::vector<Focus> gains;
std::ranges::copy(iota(0) | take(points_num) | transform([&](auto i) {
                    const auto theta = 2.0f * pi * static_cast<float>(i) /
                                       static_cast<float>(points_num);
                    return Focus(center + radius * Vector3(std::cos(theta),
                                                           std::sin(theta), 0),
                                 FocusOption{});
                  }),
                  std::back_inserter(gains));
GainSTM(gains, 1.0f * Hz,
        GainSTMOption{.mode = GainSTMMode::PhaseIntensityFull});
//~return 0; }