#include "autd3/link/twincat.hpp"

//~int main() {
autd3::link::RemoteTwinCAT("172.16.99.111.1.1",
                           autd3::link::RemoteTwinCATOption{
                               .server_ip = "172.16.99.104",
                               .client_ams_net_id = "172.16.99.62.1.1"});
//~return 0; }