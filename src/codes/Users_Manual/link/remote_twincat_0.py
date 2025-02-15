from pyautd3.link.twincat import RemoteTwinCAT, RemoteTwinCATOption

RemoteTwinCAT(
    server_ams_net_id="172.16.99.111.1.1",
    option=RemoteTwinCATOption(
        server_ip="172.16.99.104",
        client_ams_net_id="172.16.99.62.1.1",
    ),
)