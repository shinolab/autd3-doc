//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
const autd3::Point3 center(0, 0, 150);
const auto points_num = 200;
const auto radius = 30.0f;
std::vector<autd3::Focus> gains;
std::ranges::copy(iota(0) | take(points_num) | transform([&](auto i) {
                    const auto theta = 2.0f * autd3::pi *
                                       static_cast<float>(i) /
                                       static_cast<float>(points_num);
                    return autd3::Focus(
                        center + radius * autd3::Vector3(std::cos(theta),
                                                         std::sin(theta), 0),
                        autd3::FocusOption{});
                  }),
                  std::back_inserter(gains));
autd3::GainSTM stm(gains, 1.0f * autd3::Hz,
                   autd3::GainSTMOption{
                       .mode = autd3::GainSTMMode::PhaseIntensityFull});
//~return 0; }