//~#include<autd3.hpp>
#include "autd3/link/simulator.hpp"

//~int main() {
//~auto autd = autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
//~                .open(
autd3::link::Simulator::builder("127.0.0.1:8080")
    //~                    );
    //~return 0; }