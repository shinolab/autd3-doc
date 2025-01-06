//~#include<autd3.hpp>
#include <autd3_link_soem.hpp>

//~int main() {
//~auto autd = autd3::ControllerBuilder({autd3::AUTD3(autd3::Point3::origin())})
//~                .open(
autd3::link::RemoteSOEM::builder("172.16.99.104:8080")
    //~                    );
    //~return 0; }