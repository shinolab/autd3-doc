//~#include<autd3.hpp>
#include "autd3/link/visualizer.hpp"

//~int main() {
auto autd = autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
                .open(autd3::link::Visualizer::builder());

autd3::Vector3 center = autd.geometry().center() + autd3::Vector3(0, 0, 150);
autd3::gain::Focus g(center);
autd.send(g);

autd3::link::PlotConfig config;
config.fname = "phase.png";
autd.link().plot_phase(config, autd3::Segment::S0, 0);
//~return 0; }