//~#include<optional>
//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
gain::Group(
    [](const auto& dev) {
      return [](const auto& tr) -> std::optional<const char*> {
        if (tr.idx() <= 100) return "null";
        return "focus";
      };
    },
    std::unordered_map<const char*, std::shared_ptr<Gain>>{
        {"focus", std::make_shared<Focus>(Point3(x, y, z), FocusOption{})},
        {"null", std::make_shared<Null>()}});
//~return 0; }