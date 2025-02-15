//~#include<optional>
//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd3::Group(
    [](const auto& dev) {
      return [](const auto& tr) -> std::optional<const char*> {
        if (tr.idx() <= 100) return "null";
        return "focus";
      };
    },
    std::unordered_map<const char*, std::shared_ptr<autd3::Gain>>{
        {"focus", std::make_shared<autd3::Focus>(autd3::Point3(x, y, z),
                                                 autd3::FocusOption{})},
        {"null", std::make_shared<autd3::Null>()}});
//~return 0; }