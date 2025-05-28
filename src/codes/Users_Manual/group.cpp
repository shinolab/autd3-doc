//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd3::Group(
    [](const Device& dev) -> std::optional<const char*> {
      if (dev.idx() == 0) {
        return "null";
      } else if (dev.idx() == 1) {
        return "focus";
      } else {
        return std::nullopt;
      }
    },
    std::unordered_map<const char*, std::shared_ptr<driver::Datagram>>{
        {"focus",
         std::make_shared<Focus>(Focus(Point3(x, y, z), FocusOption{}))},
        {"null", std::make_shared<Null>()}});
//~return 0; }