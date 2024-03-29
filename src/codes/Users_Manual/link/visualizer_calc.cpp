#include "autd3/link/visualizer.hpp"

auto autd = autd3::Controller::builder()
                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
                .open(autd3::link::Visualizer::builder());

autd3::Vector3 center = autd.geometry().center() + autd3::Vector3(0, 0, 150);
autd3::gain::Focus g(center);
autd.send(g);

std::vector points{center};
const auto p = autd.link().calc_field(points, autd.geometry(), Segment::S0, 0);
std::cout << "Acoustic pressure at (" << center.x() << ", " << center.y()
          << ", " << center.z() << ") = " << p[0] << std::endl;