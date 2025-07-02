//~#include <chrono>
//~#include <vector>
//~#include "autd3.hpp"
//~#include "autd3/link/nop.hpp"
//~int main() {
//~auto autd = autd3::Controller::open({autd3::AUTD3{.pos =
//~autd3::Point3::origin(), .rot = autd3::Quaternion::Identity(),}},
//~autd3::link::Nop{});
autd.send(autd3::Sine(150 * autd3::Hz, autd3::SineOption{}));

const autd3::Point3 center = autd.center() + autd3::Vector3(0., 0., 150.);
autd.send(autd3::FociSTM(
    std::vector{
        center + autd3::Vector3(20., 0., 0.),
        center - autd3::Vector3(20., 0., 0.),
    },
    0.5f * autd3::Hz
    // std::chrono::seconds(2)
    // autd3::SamplingConfig{1.0f * autd3::Hz}
    // autd3::SamplingConfig{std::chrono::seconds(1)}
    ));
//~return 0;
//~}