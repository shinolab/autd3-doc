~using AUTD3Sharp;
using AUTD3Sharp.Link;

new RemoteTwinCAT(
        serverAmsNetId: "172.16.99.111.1.1",
        option: new RemoteTwinCATOption
        {
                ServerIp = "172.16.99.104",
                ClientAmsNetId = "172.16.99.62.1.1"
        }
);