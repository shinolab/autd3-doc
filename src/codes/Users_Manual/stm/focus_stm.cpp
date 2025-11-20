//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
//~using namespace autd3;
const Point3 center(0, 0, 150);
constexpr auto points_num = 200;
constexpr auto radius = 30.0f;
FociSTM(iota(0) | take(points_num) | transform([&](auto i) {
          const auto theta = 2.0f * pi * static_cast<float>(i) /
                             static_cast<float>(points_num);
          Point3 p =
              center + radius * Vector3(std::cos(theta), std::sin(theta), 0);
          return p;
        }) | std::ranges::to<std::vector<Point3>>(),
        1.0f * Hz);
//~return 0; }