~using System.Net;
using AUTD3Sharp.Link;

new Remote(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8080), new RemoteOption
{
    Timeout = null,
});