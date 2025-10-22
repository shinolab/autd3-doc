#include <optional>

#include "autd3/link/remote.hpp"

//~int main() {
//~using namespace autd3;
link::Remote("127.0.0.1:8080", link::RemoteOption{.timeout = std::nullopt});
//~return 0; }