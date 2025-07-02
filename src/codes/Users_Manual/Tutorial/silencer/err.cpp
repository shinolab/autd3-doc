//~#include <ranges>
//~#include <vector>
//~#include "autd3.hpp"
//~#include "autd3/link/nop.hpp"
//~using namespace std::ranges::views;
//~int main() {
//~auto autd = autd3::Controller::open({autd3::AUTD3{.pos =
//~autd3::Point3::origin(), .rot = autd3::Quaternion::Identity(),}},
//~autd3::link::Nop{});
autd.send(autd3::Silencer());

const autd3::Point3 center = autd.center() + autd3::Vector3(0., 0., 150.);
const auto points_num = 40;
const auto radius = 30.0f;
std::vector<autd3::Point3> foci;
std::ranges::copy(iota(0) | take(points_num) | transform([&](auto i) {
                    const auto theta = 2.0f * autd3::pi *
                                       static_cast<float>(i) /
                                       static_cast<float>(points_num);
                    autd3::Point3 p =
                        center + radius * autd3::Vector3(std::cos(theta),
                                                         std::sin(theta), 0);
                    return p;
                  }),
                  std::back_inserter(foci));
autd.send(autd3::FociSTM(foci, 50.0f * autd3::Hz));
//~return 0;
//~}