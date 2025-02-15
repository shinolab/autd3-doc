//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd.group_send(
    [](const autd3::Device& dev) -> std::optional<const char*> {
      if (dev.idx() == 0) {
        return "null";
      } else if (dev.idx() == 1) {
        return "focus";
      } else {
        return std::nullopt;
      }
    },
    std::unordered_map<const char*, std::shared_ptr<autd3::driver::Datagram>>{
        {"focus",
         std::make_shared<autd3::Focus>(autd3::Focus(autd3::Point3(x, y, z),
                                                     autd3::FocusOption{}))},
        {"null", std::make_shared<autd3::Null>()}});
//~return 0; }